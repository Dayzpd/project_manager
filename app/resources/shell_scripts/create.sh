#!/bin/bash
su - $3
expect "Password: "
send $4
sudo mkdir /srv/www/$1
sudo git init
sudo git remote add origin $2
