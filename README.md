# search-engine-tutorial

## installation

1. mysql
```
apt-get install mysql-server -y
service mysql restart
mysql_secure_installation
```
```
root@88f2909b2200:~# mysql_secure_installation

...
Press y|Y for Yes, any other key for No: y
...
Please enter 0 = LOW, 1 = MEDIUM and 2 = STRONG: 0
...
New password: 123456789
Re-enter new password: Boost111@
...

Do you wish to continue with the password provided?(Press y|Y for Yes, any other key for No) : y
...
Remove anonymous users? (Press y|Y for Yes, any other key for No) : y
...
Disallow root login remotely? (Press y|Y for Yes, any other key for No) : No
...
Remove test database and access to it? (Press y|Y for Yes, any other key for No) : No
...
Reload privilege tables now? (Press y|Y for Yes, any other key for No) : y
```


2. elasticsearch
```
apt-get update && apt-get install -y gnupg2
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee /etc/apt/sources.list.d/elastic-7.x.list
apt-get update && apt-get install elasticsearch
service elasticsearch start
cd /usr/share/elasticsearch
bin/elasticsearch-plugin install analysis-nori
service elasticsearch restart

```
