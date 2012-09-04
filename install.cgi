#!/bin/sh

rm ./install.cgi
echo -e "Content-Type: text/html; charset=UTF-8\n"
echo "<html><head></head><body>"
echo "Getting XOOPS X (ten) and extracting...<br>"
if [ $@ ]; then
	TRUST=$@
else
	TRUST="../xoops_trust_path"
fi
echo "<pre>"
curl -kL github.com/nao-pon/xoopsx_installer/raw/master/installer.sh|sed "s#<T>#$TRUST#"|sh|cat
echo "</pre>"
echo "<br><a href="./install/index.php">Goto your XOOPS installer</a>"
echo "</body></html>"
