#!/bin/sh

main() {
	TRUST=$1
	if [ ! $TRUST ]; then
		TRUST="../xoops_trust_path"
	fi
#	wget --no-check-certificate -O corepack.tar.gz https://github.com/XoopsX/legacy/tarball/CorePack
	curl -kL -o corepack.tar.gz https://github.com/XoopsX/legacy/tarball/CorePack
	tar zxf corepack.tar.gz
	mkdir ${TRUST}
	cp -rf XoopsX-legacy-*/html/* ./
	cp -f XoopsX-legacy-*/html/.* ./
	cp -rf XoopsX-legacy-*/xoops_trust_path/* ${TRUST}
	cp -f XoopsX-legacy-*/xoops_trust_path/.* ${TRUST}
	rm corepack.tar.gz
	rm -rf XoopsX-legacy-*/
	chmod 606 mainfile.php
	chmod 707 uploads
	chmod 707 ${TRUST}/cache
	chmod 707 ${TRUST}/templates_c
	chmod 707 ${TRUST}/uploads
	chmod 707 ${TRUST}/uploads/xupdate
	chmod 707 ${TRUST}/modules/protector/configs
	echo "----------------------------------------"
	if [ -d "./install" -a -d $TRUST ]; then
		echo "All the processings were completed. Please acsess to your XOOPS site."
	else
		echo "\nERROR!"
	fi
}
main "<T>"
