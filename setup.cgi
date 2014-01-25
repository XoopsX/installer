#!/bin/sh

ME=$(basename $0)
echo -e "Location: ./${ME}\n"
curl -kL -o "${ME}.tmp" http://xoopsx.github.io/installer/install.cgi
BASH_PATH=$(which bash)
sed -i "" -e "1s%^\#\!/bin/bash%\#\!${BASH_PATH}%" "${ME}.tmp"
chmod 0700 ${ME}.tmp
mv "${ME}.tmp" ${ME}
exit 0