#!/bin/bash

# extract instance IP, known its sequential ID
function instance_ip {
	docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' dontask_web_$1
}

# last octet from the IP
function last_octet {
	instance_ip $1|awk -F\. '{print $4}'
}

function worker_id {
	expr $(last_octet $1) % 4
}

for i in 1 2 3 4;
do
	w_id=$(worker_id $i)
	echo "INSTANCE dontask_web_$i maps to <JSESSION>.worker$w_id"
	perl -pi -e "s/JSESSION$i/worker$w_id/g" nginx.conf
done

docker-compose restart nginx
git checkout nginx.conf
