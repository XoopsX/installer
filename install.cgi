#!/bin/bash

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

function msg() {
    if [ ${HTTP_ACCEPT_LANGUAGE:0:2} = 'ja' ]; then
        L=2
    else
        L=1
    fi

    MSG[10]="XOOPS Cube Legacy (XOOPS X) Setup"
    MSG[20]="XOOPS Cube Legacy (XOOPS X) セットアップ"

    MSG[11]="&quot;xoops_trust_path&quot; Settting"
    MSG[21]="&quot;xoops_trust_path&quot; の設定"

    MSG[12]="Please set server path of your &quot;xoops_trust_path&quot;."
    MSG[22]="サーバー上に配置する &quot;xoops_trust_path&quot; のパスを指定してください。<br>できる限りドキュメントルート外に指定してください。ただし、PHP からアクセスできる場所に限ります。"

    MSG[13]="HTTPS Proxy Config : <br>(Optional)"
    MSG[23]="HTTPS プロキシ : <br>(任意設定)"

    MSG[14]="(Optional)Please set proxy address for your server.<br>(e.g.) https://proxyuser:password@proxyhost.example.com:8080<br><span class="text-warning">WARNING: This option will override server&apos;s environment variable!</span>"
    MSG[24]="必要であれば、あなたの環境で利用する HTTPS プロキシの指定をしてください。<br>(例) https://proxyuser:password@proxyhost.example.com:8080<br><span class="text-warning">注意事項: サーバーの環境変数「HTTPS_PROXY」を上書きします。</span>"

    MSG[15]="OK &amp; Upload &amp; Please Wait"
    MSG[25]="OK &amp; アップロード &amp; 少々お待ちください"

    MSG[16]="Getting XOOPS X (ten) and extracting..."
    MSG[26]="XOOPS X (ten) のパッケージを取得しサーバー上に配置しています..."

    MSG[17]="Goto your XOOPS Cube Legacy installer"
    MSG[27]="クリックして XOOPS Cube Legacy のインストーラーへ進む"

    echo ${MSG[$L$1]}
}

function showForm() {
    cat <<EOT
    <h1 class="page-header">$(msg 0)</h1>
    <h2>$(msg 1)</h2>
    <form method="get" class="form-horizontal">
        <div class="control-group">
            <label class="control-label" for="TRUST">xoops_trust_path : </label>
            <div class="controls">
                <input id="TRUST"  name="TRUST" class="span6" style="height:30px" type="text" value="$1">
                <p class="help-block">$(msg 2)</p>
            </div>
        </div>
        <hr>
        <div class="control-group">
            <label class="control-label" for="https_proxy">$(msg 3)</label>
            <div class="controls">
                <input id="HTTPS_PROXY" name="HTTPS_PROXY" class="span6" style="height:30px;" type="text" value="$HTTPS_PROXY">
                <p class="help-block">$(msg 4)</p>
            </div>
        </div>
        <div class="form-actions">
            <input type="submit" class="btn btn-primary" value="$(msg 5)">
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

# get document root
if [ $DOCUMENT_ROOT ]; then
    DR=$DOCUMENT_ROOT
else
    DR=`pwd`
fi

# output
echo "<html><head>"
echo "<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">"
echo "<script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>"
echo "</head><body>"

if [ ! $TRUST ]; then
    showForm "`dirname ${DR}`/xoops_trust_path"
else
    
    TRUST=`echo $TRUST | sed 's/%2F/\//g'`
    
    MSG=`mkdir $TRUST 2>&1`
    
    if [ -d ${TRUST} ]; then
        chmod 0600 ./${0##*/}
        rm ./${0##*/}
        echo "<h1 class="page-header">$(msg 0)</h1>"
        echo "<p class="lead">$(msg 6)</p>"
        echo "<pre style=\"height:55%;overflow:auto;\">"
        curl xoopsx.github.io/installer/install.sh|sed "s#<T>#$TRUST#"|sh 2>&1|cat
        echo "</pre>"
        echo "<div class="form-actions"><a href=\"./install/index.php\" class=\"btn btn-success\">$(msg 7)</a></div>"
    else
        echo "<div><span class=\"label label-important\">$MSG</span></div>"
        showForm $TRUST
    fi
    
fi

echo "</body></html>"
