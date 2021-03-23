# Django-QueryDatabase

## Running on king.nuigalway.ie

Database 'american_gut_database' has been loaded into the main king.nuigalway.ie MySQL server. The database be accessed by user 'timhu'. An alternative configuration file queryDatabase/settings.py is checked into branch king-config which has the right credentials/settings to connect to the MySQL database on king.

A minor change to the database dump file (related to character encoding) was needed before it would import:

```
sed -i 's/utf8mb4_0900_ai_ci/utf8_general_ci/g' dump.sql
sed -i 's/CHARSET=utf8mb4 /CHARSET=utf8 /g' dump.sql
```

Importing is done with this command:

```
cat dump.sql | mysql --user=timhu -p american_gut_database
```

Instructions on building and running the Docker container is contained in the Dockefile.

To make the site available to the outside world a DNS record for a host name must be configured as either a 'A' record to 140.203.202.148 or a 'CNAME' to king.nuigalway.ie. I've [JD] used one of my own domains for this until a better domain is found.

Create the file /etc/apache2/sites-available/querydb.vmh.conf with content:

```
<VirtualHost *:80>
	ServerName querydb.vmh.strix.ie
	ErrorLog ${APACHE_LOG_DIR}/error-querydb.log
	CustomLog ${APACHE_LOG_DIR}/access-querydb.log combined
  ProxyRequests On
  ProxyPass / http://localhost:8001/
  ProxyPassReverse / http://localhost:8001/
</VirtualHost>
```

Enable the site:
```
e2ensite querydb.vmh
```

Restart apache2 server:

 ```
 service apache2 restart
 ```
 
