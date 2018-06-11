#!/bin/bash
su - $2
expect "Password: "
send $3
sudo docker build -t $1 /srv/www/$1
