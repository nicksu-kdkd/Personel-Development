#!/bin/bash
## This script will check the environment for PXE and automatically install and config the needed servers or files.
## Before you run this script , please pay attention to the below constants , and do place the installation media
## the iso file in the /ISO , and named as centos.iso or any as you want , but do remember to update this script
## Author: Nick Su
## Date:   19/05/2015
## Email:  nicksu383@gmail.com
## Version: 1.0


sharePath="/export"	# The path to export the ISO
TFTPpoint="/var/lib/tftpboot"   # The path for tftp export
ISO="/ISO/centos.iso"  # The path contain the ISO for installation

# define a function to check the package installation
function check_install(){
	rpm -q $1 &> /dev/null
	if [ $? -ne 0 ];then
		echo "$1 is not installed , we will install it for you"
		yum -y install $1 &> /dev/null
		if [ $? -eq 0 ];then
			echo "$1 installation successful"
			return 0
		else
			echo "$1 installation failed , please check log"
			return 1
		fi
	else
		echo "$1 already installed"
		return 0
	fi
}

# check the directories exist or not
[ -d "$sharePath" ] || mkdir "$sharePath" &> /dev/null
[ -d "$TFTPpoint" ] || mkdir -p "$TFTPpoint/pxelinux.cfg" &> /dev/null

# pxelinux.0 file act as the boot loader , it comes from the syslinux package
if [ ! -f "$TFTPpoint/pxelinux.0" ];then
	yum -y install syslinux &> /dev/null && find /usr/share -type f -name "pxelinux.0" -exec cp {} $TFTPpoint \; &> /dev/null && echo "pxelinux.0 ready"
else
	find /usr/share -type f -name "pxelinux.0" -exec cp {} $TFTPpoint \; &> /dev/null && echo "pxelinux.0 ready"
fi

# check the ISO file and mount as NFS source
[ -f $ISO ] && mount -o loop $ISO $sharePath &> /dev/null 

for i in initrd.img vesamenu.c32 vmlinuz;do
	find $sharePath -type f -name "$i" -exec cp {} $TFTPpoint \; &>/dev/null
	[ $? -eq 0 ]&& echo "$i ready"
done

find $sharePath -type f -name "isolinux.cfg" -exec cp {} $TFTPpoint/pxelinux.cfg/default \; &>/dev/null && echo "default file ready"

# 4 packages needed for PXE , nfs-utils tftp-server dhcp and xinetd
# check the dhcp and config file
check_install "dhcp"&&cat >/etc/dhcp/dhcpd.conf<<-EOF
	subnet 192.168.1.0 netmask 255.255.255.0 {  
        range 192.168.1.20 192.168.1.30;
	allow bootp;
	next-server 192.168.1.10;
	filename "/pxelinux.0";
	}
	EOF

# check the tftp-server and xinetd
if [[ $(check_install "tftp-server") && $(check_install "xinetd") ]];then
	[ -f /etc/xinetd.d/tftp ] && sed -i '/disable/ s/yes/no/' /etc/xinetd.d/tftp
fi

# check the nfs service 
check_install "nfs-utils" && echo "$sharePath 192.168.1.0/24(ro)" > /etc/exports 

# start the tftp service and check the status
if [ $(netstat -a|grep -i tftp|wc -l) -gt 0 ];then
	echo "TFTP service is running now"
else
	/etc/init.d/xinetd restart &> /dev/null
	[ $? -eq 0 ] && echo "TFTP service is running now" || echo "Something wrong with TFTP"
fi

# start the dhcp service 
# turn off the SELINUX and iptables
setenforce 0 && sed -i '/SELINUX/ s/enforcing/disabled/' /etc/sysconfig/selinux &> /dev/null
/etc/init.d/iptables stop &> /dev/null
if [ $(/etc/init.d/dhcpd status|grep running|wc -l) -gt 0 ];then
	echo "DHCP service is running now"
else
	/etc/init.d/dhcpd restart &> /dev/null
	[ $? -eq 0 ] && echo "The DHCP service is ruuning now" || echo "Something wrong with DHCP"
fi

# start the NFS 
/etc/init.d/rpcbind restart &> /dev/null
if [ $(exportfs | grep "$sharePath" | wc -l) -gt 0 ];then
	echo "The NFS is running now"
else
	/etc/init.d/nfs restart &> /dev/null && exportfs -a &> /dev/null && echo "The NFS is running now" || echo "Something wrong with NFS"
fi

echo "All the prepartion tasks are done , you can start your client now"
