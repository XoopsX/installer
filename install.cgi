#!/bin/sh

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
