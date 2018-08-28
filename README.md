# pymongo

pip install flask

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

/*14.04 ubuntu*/
echo "deb [ arch=amd64 ] http://repo.mongodb.com/apt/ubuntu trusty/mongodb-enterprise/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-enterprise.list

sudo apt-get install update
sudo apt-get install -y mongodb-enterprise


https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/
 

$ python -m pip install pymongo==3.5.1
