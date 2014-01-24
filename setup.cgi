#!/bin/sh

echo -e "Location: ./$(basename $0)\n"
curl -kL -o setup.tmp http://xoopsx.github.io/installer/install.cgi
BASH_PATH=$(which bash)
sed -i "" -e "1s%^\#\!/bin/bash%\#\!${BASH_PATH}%" setup.tmp
mv setup.tmp setup.cgi
chmod 0700 setup.cgi
