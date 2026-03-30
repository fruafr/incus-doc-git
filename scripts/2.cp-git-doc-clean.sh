#!/bin/bash

#Copy doc folder content to the git-doc folder and clean the output

mkdir -p ../doc/

rm -rf ../doc/*

cp -r incus/doc/* ../doc/

## Remove the images folder
rm -rf ../doc/images

## Remove irrelevant files
rm -rf ../doc/reference/manpages
rm -rf ../doc/conf.py
rm -rf ../doc/substitutions.yaml

