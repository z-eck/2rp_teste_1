#!/usr/bin/python

import os

# instalacao java

os.system('sudo apt-get install java-11-openjdk-devel')
os.system('sudo apt-get install java-11-openjdk')
os.system('sudo wget https://download.oracle.com/java/18/latest/jdk-18_linux-aarch64_bin.rpm')
os.system('sudo localinstall jre-18-linux-x64.rpm')
os.system('java -version')

# instalacao do Zeppelin - Via wget

# os.system('sudo wget https://dlcdn.apache.org/zeppelin/zeppelin-0.10.1/zeppelin-0.10.1-bin-all.tgz')

# instalacao do Zeppelin - via docker

os.system('docker run -p 8888:8080 --rm --name zeppelin apache/zeppelin:0.10.1')