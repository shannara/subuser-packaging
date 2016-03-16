#!/bin/bash

VERSION=0.5.4
NAME=subuser
PREFIX=rh-python34
SOURCE=$PREFIX-$NAME-$VERSION
TARBALL=$SOURCE.tar.gz

wget https://github.com/subuser-security/subuser/archive/$VERSION.tar.gz

tar xf $VERSION.tar.gz; rm $VERSION.tar.gz

mv $NAME-$VERSION $SOURCE

tar cf $TARBALL $SOURCE

rm -rf $SOURCE
