opt="-Dawt.useSystemAAFontSettings=gasp"
if ! echo ${_JAVA_OPTIONS} |grep -q -- ${opt}  ;then 
    export _JAVA_OPTIONS="${_JAVA_OPTIONS}  ${opt}"
fi
