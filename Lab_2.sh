#!/bin/bash
mkdir project
cd project
git init
git clone https://github.com/popcorn-official/popcorn-desktop.git
cd popcorn-desktop
sudo apt install libssl1.0-dev
sudo apt install nodejs-dev
sudo apt install node-gyp
sudo apt install npm
chmod ugo+rwx ./make_popcorn.sh
./make_popcorn.sh
