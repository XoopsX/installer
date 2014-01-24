XOOPS X (ten) Installer
=======================

## On the web

* Get "[setup.cgi](http://xoopsx.github.io/installer/setup.cgi)" & upload into your [DOCUMENT ROOT].
* And chmod 0700 setup.cgi
* Access to `[YOUR SERVER URL]/setup.cgi` with your web browser
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
