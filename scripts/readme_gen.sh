#!/bin/bash

files=`echo "$1" | tr "," "\n"`

challenges=$(echo $files | cut -d '/' -f 1 | uniq | awk '/^[0-9]+\.\s/ {print}')

echo $challenges | while read challenge; do echo $challenge && ! [ -z "$challenge" ]  && python3 $GEN_MD "$challenge"; done

        