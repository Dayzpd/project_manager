#!/bin/bash
su - $3
expect "Password: "
send $4
sudo docker run -d --restart=always --name $1 -p 127.0.0.1:$2:80 -t $1
