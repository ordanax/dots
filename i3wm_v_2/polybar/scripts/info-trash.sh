#!/bin/sh

case "$1" in
    --clean)
        rm -rf ~/.local/share/Trash/files
        rm -rf ~/.local/share/Trash/info
        mkdir ~/.local/share/Trash/files
        mkdir ~/.local/share/Trash/info
        ;;
    *)
        num1=`find ~/.local/share/Trash/files/ -maxdepth 1 | wc -l`
        num2=1
        res=`expr $num1 - $num2`
        echo $res
        ;;
esac