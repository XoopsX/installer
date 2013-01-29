XOOPS X (ten) Installer
=======================

## On the shell (sh, bash)

```bash
cd [DOCUMENT ROOT]
T="../xoops_trust_path";curl -kL github.com/XoopsX/installer/raw/master/install.sh|sed "s#<T>#$T#"|sh
```

## On the shell (csh)

```csh
cd [DOCUMENT ROOT]
set T="../xoops_trust_path";curl -kL github.com/XoopsX/installer/raw/master/install.sh|sed "s#<T>#$T#"|sh
```

## On the web

* Upload "[install.cgi](https://github.com/XoopsX/installer/raw/master/install.cgi)" into [DOCUMENT ROOT] & chmod +x install.cgi
* Access to `install.cgi` or `install.cgi?../xoops_trust_path` with your web browser
