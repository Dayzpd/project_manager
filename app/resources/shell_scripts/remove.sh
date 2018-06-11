#!/bin/bash
su - $2
expect "Password: "
send $3
sudo docker rm $1
