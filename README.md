XOOPS X (ten) Installer
=======================

## On the shell

<pre>
cd [DOCUMENT ROOT]
sh T="../xoops_trust_path";curl -kL github.com/XoopsX/installer/raw/master/install.sh|sed "s#&lt;T&gt;#$T#"|sh
</pre>
</code>

## On the web

* Upload install.cgi into [DOCUMENT ROOT] & chmod +x install.cgi
* Access to install.cgi with web browser
