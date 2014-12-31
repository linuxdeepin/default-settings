#!/bin/sh

XFT_SETTINGS="
Xft.autohint: 0
Xft.lcdfilter:  lcddefault
Xft.hintstyle:  hintfull
Xft.hinting: 1
Xft.antialias: 1
Xft.rgba: rgb
"

if [ -n "$DISPLAY" ]; then
    echo "$XFT_SETTINGS" | xrdb -merge -
fi
