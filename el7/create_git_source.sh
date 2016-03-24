#!/bin/bash

VERSION=0.5.4
NAME=subuser
PREFIX=rh-python34
SOURCE=$PREFIX-$NAME-$VERSION
TARBALL=$SOURCE-git.tar.gz

wget https://github.com/subuser-security/subuser/archive/master.zip

unzip master.zip; rm master.zip

mv $NAME-master $SOURCE

tar cf $TARBALL $SOURCE

rm -rf $SOURCE
