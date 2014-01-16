XOOPS X (ten) Installer
=======================

## On the web

* Get "[install.cgi](http://xoopsx.github.io/installer/install.cgi)".
* Check `bash` path of your server and Supposing path of `bash` is different, you should correct that path of the 1st line of "install.cgi".
* And upload "[install.cgi](http://xoopsx.github.io/installer/install.cgi)" into [DOCUMENT ROOT]
* And chmod +x install.cgi
* Access to `install.cgi` or `install.cgi` with your web browser
* And input your "XOOPS_TRUST_PATH"

## On the shell (sh, bash)

```bash
cd [DOCUMENT ROOT]
T="../xoops_trust_path";curl xoopsx.github.io/installer/install.sh|sed "s#<T>#$T#"|sh
```

## On the shell (csh)

```csh
cd [DOCUMENT ROOT]
set T="../xoops_trust_path";curl xoopsx.github.io/installer/install.sh|sed "s#<T>#$T#"|sh
```
