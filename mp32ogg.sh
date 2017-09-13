#!/bin/bash
mkdir -p oggs
for file in words_pronounce/*.mp3 
    #do avconv -i "${file}" "`echo ${file%.mp3}.ogg`";
    do 
        fbname=$(basename "$file" .mp3)
        avconv -i "${file}" "oggs/${fbname}.ogg"
    done
done 
