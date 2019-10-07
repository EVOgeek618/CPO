#!/bin/bash
mkdir project
cd project
git init
git clone https://github.com/popcorn-official/popcorn-desktop.git
chmod -R ugo+rwx popcorn-desktop
cd popcorn-desktop
sudo apt install libssl1.0-dev
sudo apt install nodejs-dev
sudo apt install node-gyp
sudo apt install npm
npm install
sed -i 's/0.33.4/0.35.3/' gulpfile.js
gulp build
gulp run
