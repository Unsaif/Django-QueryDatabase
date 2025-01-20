# To build the docker image:
# docker build -t vmh/querydb .
#
# To run the docker image exposing port 8001:
# docker run --network="host" -p 8001:8001 --rm -it vmh/querydb
# 
# --network="host" makes the host OS ports available inside 
# the container so that MySQL can be accessed from localhost
#
# To verify operation, from host OS visit http://localhost:8001
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

# FROM ubuntu:18.04
# ARG DEBIAN_FRONTEND=noninteractive
# RUN apt-get clean
# RUN apt-get update
# RUN apt-get install -y unzip python3-pip mysql-client libmysqlclient-dev
# RUN apt-get install -y python3-dev python3-mysqldb 
# RUN pip3 install Cython==0.29.36
# RUN pip3 install numpy==1.19.5
# RUN pip3 install pymysql django
# RUN pip3 install mysqlclient==2.0.3
# RUN pip3 install pandas requests
# WORKDIR /querydb
# COPY . .
# # Run on port 8001 because 8000 already in use by VMH API
# CMD python3 manage.py runserver 0.0.0.0:8001

FROM ubuntu:18.04
ARG DEBIAN_FRONTEND=noninteractive

# Update system and install required packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    mysql-client \
    libmysqlclient-dev \
    unzip \
    netcat

# Install compatible versions of packages
RUN pip3 install Cython==0.29.36
RUN pip3 install numpy==1.19.5
RUN pip3 install pandas==1.1.5 requests==2.27.1 pymysql==0.9.3 django==3.2.20
RUN pip3 install mysqlclient==2.0.3

# Set working directory
WORKDIR /querydb
COPY . .

# Expose port 8001 for the Django app
EXPOSE 8001

# Run the server on port 8001
# CMD python3 manage.py runserver 0.0.0.0:8001

COPY start.sh /start.sh

# Make the script executable
RUN chmod +x /start.sh

# Use the script as the container's entry point
CMD ["/start.sh"]



