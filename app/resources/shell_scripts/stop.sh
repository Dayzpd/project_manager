#!/bin/bash
su - $2
expect "Password: "
send $3
sudo docker stop $1
