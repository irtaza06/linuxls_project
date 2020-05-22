#!/bin/bash
docker build . --tag='linuxls:v1'
docker stop 'linuxls_container'
docker rm 'linuxls_container'
docker run -p 5000:80 --name 'linuxls_container' linuxls:v1
