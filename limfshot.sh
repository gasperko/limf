#!/bin/bash
i=/tmp/.limfshot.png
scrot $i
limf -l $i | xclip -selection clipboard
rm $i
