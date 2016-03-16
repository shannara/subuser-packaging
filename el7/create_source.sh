#!/bin/bash

VERSION=0.5.3
NAME=subuser
PREFIX=rh-python34
SOURCE=$PREFIX-$NAME-$VERSION
TARBALL=$PREFIX-$NAME-$VERSION.tar.gz

wget https://github.com/subuser-security/subuser/archive/$VERSION.tar.gz

tar xf $VERSION.tar.gz; rm $VERSION.tar.gz

mv $NAME-$VERSION $SOURCE

tar cf $TARBALL $SOURCE

rm -rf $SOURCE
