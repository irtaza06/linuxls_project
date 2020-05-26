#!/bin/bash
docker build . --tag='linuxls:blue'
docker stop 'linuxls_blue_container'
docker rm 'linuxls_blue_container'
docker run -p 5000:80 --name 'linuxls_blue_container' linuxls:blue
