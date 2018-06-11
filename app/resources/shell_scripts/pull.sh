su - $2
expect "Password: "
send $3
cd /srv/www/$1
sudo git pull origin master
