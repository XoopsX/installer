#!/bin/sh

function urldecode() {
     cat > /tmp/urldecode.sed << \EOF
s/%25/%/gi
s/%20/ /gi
s/%09/ /gi
s/%21/!/gi
s/%22/"/gi
s/%23/#/gi
s/%24/\$/gi
s/%26/\&/gi
s/%27/'\''/gi
s/%28/(/gi
s/%29/)/gi
s/%2a/\*/gi
s/%2b/+/gi
s/%2c/,/gi
s/%2d/-/gi
s/%2e/\./gi
s/%2f/\//gi
s/%3a/:/gi
s/%3b/;/gi
s/%3d/=/gi
s/%3e//gi
s/%3f/?/gi
s/%40/@/gi
s/%5b/\[/gi
s/%5c/\\/gi
s/%5d/\]/gi
s/%5e/\^/gi
s/%5f/_/gi
s/%60/`/gi
s/%7b/{/gi
s/%7c/|/gi
s/%7d/}/gi
s/%7e/~/gi
s/%09/      /gi
EOF
     echo $1 | sed -f /tmp/urldecode.sed 
     rm -f /tmp/urldecode.sed
}

function showForm() {
    cat <<EOT
    <h1 class="page-header">"xoops_trust_path" Settting</h1>
    <form method="get" class="form-horizontal">
        <div class="control-group">
            <label class="control-label" for="TRUST">xoops_trust_path : </label>
            <div class="controls">
                <input id="TRUST"  name="TRUST" class="span6" style="height:30px" type="text" value="$1">
                <p class="help-block">Please set server path of your "xoops_trust_path".</p>
            </div>
        </div>
        <div class="control-group">
            <label class="control-label" for="https_proxy">HTTPS Proxy Config : </label>
            <div class="controls">
                <input id="HTTPS_PROXY" name="HTTPS_PROXY" class="span6" style="height:30px;" type="text" value="$HTTPS_PROXY">
                <p class="help-block">(Optional)Please set proxy address for your server. (e.g.) https://proxyuser:password@proxyhost.example.com:8080<br>
                WARNING: This option will override server&apos;s environment variable!</p>
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" class="btn btn-primary" value="OK &amp; Upload &amp; Please Wait">
        </div>
    </form>
EOT
}

# http header
echo -e "Content-Type: text/html; charset=UTF-8\n"

# decode QUERY_STRING
if [ $QUERY_STRING ]; then
    saveIFS=$IFS
    IFS='=&'
    parm=($QUERY_STRING)
    IFS=$saveIFS

    for ((i=0; i<${#parm[@]}; i+=2))
    do
        declare ${parm[i]}=${parm[i+1]} >/dev/null 2>&1
    done
    
    if [ ! $TRUST ]; then
        P=`cd $@;pwd`
    fi

    export HTTPS_PROXY=$(urldecode $HTTPS_PROXY)

fi

# output
echo "<html><head>"
echo "<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">"
echo "<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>"
echo "</head><body>"

if [ ! $TRUST ]; then
    if [ ! $P ]; then
        P="`dirname  \`pwd\``/xoops_trust_path"
    fi
    showForm $P
else
    
    TRUST=`echo $TRUST | sed 's/%2F/\//g'`
    
    MSG=`mkdir $TRUST 2>&1`
    
    if [ -d $TRUST ]; then
        rm ./install.cgi
        echo "<h1 class="page-header">Getting XOOPS X (ten) and extracting...</h1>"
        echo "<pre style=\"height:60%;overflow:auto;\">"
        curl xoopsx.github.io/installer/install.sh|sed "s#<T>#$TRUST#"|sh 2>&1|cat
        echo "</pre>"
        echo "<div class="form-actions"><a href=\"./install/index.php\" class=\"btn btn-success\">Goto your XOOPS installer</a></div>"
    else
        echo "<div><span class=\"label label-important\">$MSG</span></div>"
        declare P="`dirname  \`pwd\``/xoops_trust_path"
        showForm $P
    fi
    
fi

echo "</body></html>"
