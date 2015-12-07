#!/bin/sh

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cp -rf .rpmmacros ~/.rpmmacros

cp -rf app-1.0.0.spec ~/rpmbuild/SPECS

# To build
#rpmbuild -ba app-1.0.0.spec