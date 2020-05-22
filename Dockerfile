FROM ubuntu:20.04
RUN apt-get update  
RUN apt-get install -y tzdata=2020a-0ubuntu0.20.04 --no-install-recommends 
RUN apt-get install -y apt-utils=2.0.2ubuntu0.1 vim=2:8.1.2269-1ubuntu5 curl=7.68.0-1ubuntu2 --no-install-recommends 
RUN apt-get install -y apache2=2.4.41-4ubuntu3 apache2-utils=2.4.41-4ubuntu3 --no-install-recommends 
RUN apt-get -y install python3=3.8.2-0ubuntu2 libapache2-mod-wsgi-py3=4.6.8-1ubuntu3 --no-install-recommends 
RUN ln /usr/bin/python3 /usr/bin/python 
RUN apt-get -y install python3-pip=20.0.2-5ubuntu1 --no-install-recommends 
RUN ln /usr/bin/pip3 /usr/bin/pip
#RUN pip install --upgrade pip 

ENV PYTHONUNBUFFERED 1

COPY ./www /var/www/html
WORKDIR /var/www/html/linuxls_website
RUN pip3 install -r requirements.txt 
COPY ./config.json /etc/config.json
COPY ./linuxls_website.conf /etc/apache2/sites-available/000-default.conf


RUN chown :www-data /var/www/html/linuxls_website/db.sqlite3 
RUN chmod 664 /var/www/html/linuxls_website/db.sqlite3


RUN chown :www-data /var/www/html/linuxls_website/
RUN chmod 775 /var/www/html/linuxls_website/

RUN chown -R :www-data /var/www/html/linuxls_website/media/ 
RUN chmod -R 775  /var/www/html/linuxls_website/media/

#RUN chmod 775 /var/www/html/linuxls_website/linuxls_website
EXPOSE 80 3500 
CMD ["apache2ctl", "-D", "FOREGROUND"]
