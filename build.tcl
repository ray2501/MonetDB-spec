#!/usr/bin/tclsh

set arch "x86_64"
set base "MonetDB-11.49.11"
set fileurl "https://www.monetdb.org/downloads/sources/Dec2023-SP4/MonetDB-11.49.11.tar.xz"

set var [list wget $fileurl -O $base.tar.xz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.xz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb MonetDB.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.xz
