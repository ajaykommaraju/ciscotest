# ciscotest
#command to build the docker image
Ajays-MacBook:ciscotest Ajay_Kommaraju$ docker build -t python-app .

#command to spin the container with the image
Ajays-MacBook:ciscotest Ajay_Kommaraju$ docker container run -dit --name python-app python-app:latest

#command to connect to running container
Ajays-MacBook:ciscotest Ajay_Kommaraju$ docker exec -it python-app /bin/bash

root@c30f7265d866:/# ls

bin  boot  dev	etc  find_the_vendor_mac.py  home  lib	lib64  media  mnt  opt	proc  root  run  sbin  srv  sys  tmp  usr  var

#command to run the script
root@c30f7265d866:/# python find_the_vendor_mac.py

please enter the mac address you want to search:6c:40:08:98:9f:d8

The company name who owns this MAC Address is: Apple, Inc
