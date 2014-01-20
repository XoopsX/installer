#!/bin/sh

main() {
	TRUST=$1
	if [ ! $TRUST ]; then
		TRUST="../xoops_trust_path"
	fi
	mkdir ${TRUST}
	if [ -d $TRUST ]; then
		curl -kL -o corepack.tar.gz https://github.com/XoopsX/legacy/tarball/stable
		PREFIX=`tar tf corepack.tar.gz | head -1`
		tar zxf corepack.tar.gz ${PREFIX}xoops_trust_path
		cp -rf ${PREFIX}xoops_trust_path/* ${TRUST}
		cp -f ${PREFIX}xoops_trust_path/.* ${TRUST}
		rm -rf ${PREFIX}
		tar zxf corepack.tar.gz ${PREFIX}html
		cp -rf ${PREFIX}html/* ./
		cp -f ${PREFIX}html/.* ./
		rm -rf ${PREFIX}
		rm corepack.tar.gz
		chmod 606 mainfile.php
		chmod 707 uploads
		chmod 707 ${TRUST}/cache
		chmod 707 ${TRUST}/templates_c
		chmod 707 ${TRUST}/uploads
		chmod 707 ${TRUST}/uploads/xupdate
		chmod 707 ${TRUST}/modules/protector/configs
		echo "----------------------------------------"
		if [ -d "./install" ]; then
			echo "All the processings were completed. Please acsess to your XOOPS site."
		else
			echo "\nERROR: install directory was not found."
		fi
	else
		echo "\nERROR: \"${TRUST}\" cannot be created."
	fi
}
main "<T>"
