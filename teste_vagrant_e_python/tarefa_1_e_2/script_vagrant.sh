#!/bin/bash

sudo apt install vagrant
sudo apt install virtualbox

vagrant init centos/7

vagrant plugin install vagrant-disksize

# Utilizar do Vim para a configuração do Vagrantfile.
# config.disksize.size = "50GB"
# config.vm.provider "virtualbox" do |v|
#     v.name = "teste-zeppelin"
#     v.cpus = 2
#     v.memory = 4096
#   end

vagrant up

vagrant ssh