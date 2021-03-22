# To build the docker image:
# docker build -t vmh/querydb .
#
# To run the docker image exposing port 8000:
# docker run --network="host" -p 8000:8000 --rm -it vmh/querydb
# 
# --network="host" makes the host OS ports available inside 
# the container so that MySQL can be accessed from localhost
#
# To verify operation, from host OS visit http://localhost:8000
#
# To configure Apache2 as a reverse-proxy for this server on regular web
# port use the following virtual host configuration file:
#<VirtualHost *:80>
#	ServerName api.my.domain
#	ErrorLog ${APACHE_LOG_DIR}/error.log
#	CustomLog ${APACHE_LOG_DIR}/access.log combined
#	ProxyRequests On
#	ProxyPass / http://localhost:8000/
#	ProxyPassReverse / http://localhost:8000/
#</VirtualHost>
#

FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get clean
RUN apt-get update
RUN apt-get install -y unzip python3-pip python3-django mysql-client libmysqlclient-dev
RUN pip3 install pymysql
WORKDIR /querydb
COPY . .
