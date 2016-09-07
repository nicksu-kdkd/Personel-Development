#!/bin/bash

dpath='/tmp'
giturl='https://github.com/shadowsocks/shadowsocks-libev.git'
installDir='/opt/shadowsocks-server'
packagesList='git gcc make asciidoc zlib-devel openssl-devel xmlto'
ssconf='/etc/shadowsocks/shadowsocks.conf'
serverPort=9010
password='i3core1024m'
method='rc4-md5'
fastOpen='true'
ss_server="$installDir/bin/ss-server"
ipAddr=`curl -4 -s http://icanhazip.com/`

# create the require dir
mkdir $installDir ${ssconf%/*}

# install the require compile packages
yum -y install $packagesList

# check the require packages installed or not
for i in `echo $packagesList|tr " " "\n"`;do
	rpm -q $i &> /dev/null || echo "$i require installed" && break
done

# pull the shadowsocks-libev source to $dpath
cd $dpath && git clone $giturl

# install shadowsocks-libev
cd "$dpath"/shadowsocks-libev && ./configure --prefix=$installDir && make && make install && make clean

# after shadowsocks-libev installed , setup the server
cat << EOF > $ssconf
{
	"server":"0.0.0.0",
	"server_port":$serverPort,
	"local_address":"127.0.0.1",
	"local_port":1080,
	"password":"$password",
	"timeout":300,
	"method":"$method",
	"fast_open":"$fastOpen"
}
EOF


# allow the input request from dport $serverPort TCP in iptables
iptables -I INPUT 1 -p tcp --dport $serverPort -j ACCEPT
iptables-save


# start the shadowsocks server
[ -x $ss_server ] && echo $ipAddr && $ss_server -c $ssconf
