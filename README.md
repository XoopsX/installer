XOOPS X (ten) Installer
=======================

## On the shell (sh, bash)

<pre>
cd [DOCUMENT ROOT]
T="../xoops_trust_path";curl -kL github.com/XoopsX/installer/raw/master/install.sh|sed "s#&lt;T&gt;#$T#"|sh
</pre>
</code>

## On the shell (csh)

<pre>
cd [DOCUMENT ROOT]
set T="../xoops_trust_path";curl -kL github.com/XoopsX/installer/raw/master/install.sh|sed "s#&lt;T&gt;#$T#"|sh
</pre>
</code>

## On the web

* Upload "[install.cgi](https://github.com/XoopsX/installer/raw/master/install.cgi)" into [DOCUMENT ROOT] & chmod +x install.cgi
* Access to install.cgi with web browser
