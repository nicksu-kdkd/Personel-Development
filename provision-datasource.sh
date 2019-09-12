#!/bin/bash
usage() { echo "Usage: $0 [-u <url>] [-p <port>] [-t <token>] [-n <datasource_name>] [-e <datasource_type>] [-r <datasource_url>] [-s <datasource_user>] [-w <datasource_password>] [-d <datasource_database>]" 1>&2; exit 1; }

while getopts ":u:p:t:n:e:r:s:w:d:" o; do
    case "${o}" in
        u)
            URL=${OPTARG}
            ;;
        p)
            PORT=${OPTARG}
            ;;
        t)
			TOKEN=${OPTARG}
			;;
		n)
			DS_NAME=${OPTARG}
			;;
		e)
			DS_TYPE=${OPTARG}
			;;
		r)
			DS_URL=${OPTARG}
			;;
		s)
			DS_USER=${OPTARG}
			;;
		w)
			DS_PW=${OPTARG}
			;;
		d)
			DS_DB=${OPTARG}
			;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

if [ -z "${URL}" ] || [ -z "${PORT}" ] || [ -z "${TOKEN}" ] ; then
    usage
fi


# Provision datasource
case "$DS_TYPE" in
	mysql)
			curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" "${URL}:${PORT}/api/datasources" -d "{\"name\":\"${DS_NAME}\",\"type\":\"${DS_TYPE}\",\"url\":\"${DS_URL}\",\"database\":\"${DS_DB}\",\"user\":\"${DS_USER}\",\"password\":\"${DS_PW}\"}"
			;;
	graphite)
			curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" "${URL}:${PORT}/api/datasources" -d "{\"name\":\"${DS_NAME}\",\"type\":\"${DS_TYPE}\",\"url\":\"${DS_URL}\",\"access\":\"direct\",\"basicAuth\":false}"
			;;
esac