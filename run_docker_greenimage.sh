#!/bin/bash
docker build . --tag='linuxls:green'
docker stop 'linuxls_green_container'
docker rm 'linuxls_green_container'
docker run -p 5000:80 --name 'linuxls_green_container' linuxls:green
