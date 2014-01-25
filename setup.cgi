#!/bin/sh
ME=$(basename $0)
echo -e "Location: ./${ME}\n"
BASH_PATH=$(which bash)
if [ $BASH_PATH ]; then
    curl -kL -o "${ME}.tmp" http://xoopsx.github.io/installer/install.cgi
    sed -i "" -e "1s%^\#\!/bin/bash%\#\!${BASH_PATH}%" "${ME}.tmp"
else
    cat << EOT > "${ME}.tmp"
#!/bin/sh
echo -e "Content-Type: text/plain; charset=UTF-8\n"
echo "Error: 'bash' not found on your server."
EOT
fi
chmod 0700 ${ME}.tmp
mv "${ME}.tmp" ${ME}
exit 0