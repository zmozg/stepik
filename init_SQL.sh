DB_NAME = "ask"
DB_USER_NAME = "box"

# MYSQL

#delete old settings
#sudo rm -f /etc/mysql/conf.d/mysql.conf
#Start MYSQL
sudo /etc/init.d/mysql start
#Create DataBase
sudo mysql -u root -e "create database if not exists $DB_NAME;"
#Create db_user with privileges to manage this database
sudo mysql -u root -e "grant all privileges on $DB_NAME.* to\
    '$DB_USER_NAME'@'localhost' with grant option;"


# add migrations self
