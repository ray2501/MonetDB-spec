# SPDX-License-Identifier: MPL-2.0
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0.  If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright 2024, 2025 MonetDB Foundation;
# Copyright August 2008 - 2023 MonetDB B.V.;
# Copyright 1997 - July 2008 CWI.

%global name MonetDB
%global version 11.55.1


# This package contains monetdbd which is a (long running) daemon, so
# we need to harden:
%global _hardened_build 1

Name: %{name}
Version: %{version}
Release: 1
Summary: Monet Database Management System
Vendor: MonetDB Foundation <info@monetdb.org>

Group: Applications/Databases
License: MPL-2.0
URL: https://www.monetdb.org/
BugURL: https://github.com/MonetDB/MonetDB/issues
Source: https://www.monetdb.org/downloads/sources/Dec2025/MonetDB-%{version}.tar.xz


BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(systemd)
BuildRequires: cmake >= 3.12
BuildRequires: make
BuildRequires: gcc
BuildRequires: bison
BuildRequires: libbz2-devel
BuildRequires: unixODBC-devel
BuildRequires: readline-devel
BuildRequires: pkgconfig(bzip2)
BuildRequires: pkgconfig(odbc)
BuildRequires: pkgconfig(readline)
BuildRequires: geos-devel >= 3.10.0
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(openssl) >= 1.1.1
BuildRequires: pkgconfig(libpcre2-8)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(liblz4) >= 1.8
# optional packages:
# BuildRequires: pkgconfig(cmocka)      # -DWITH_CMOCKA=ON
# BuildRequires: pkgconfig(gdal)        # -DSHP=ON
# BuildRequires: pkgconfig(netcdf)      # -DNETCDF=ON
# BuildRequires: pkgconfig(proj)        # -DWITH_PROJ=ON
# BuildRequires: pkgconfig(valgrind)    # -DWITH_VALGRIND=ON
BuildRoot:     %{buildroot}

%description
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the core components of MonetDB in the form of a
single shared library.  If you want to use MonetDB, you will certainly
need this package, but you will also need at least the %{name}-server
package, and most likely also %{name}-SQL, as well as one or
more client packages.

%ldconfig_scriptlets

%files
%license COPYING
%defattr(-,root,root)
%{_libdir}/libbat*.so.*

%package devel
Summary: MonetDB development files
Group: Applications/Databases
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-stream-devel%{?_isa} = %{version}-%{release}

%description devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains files needed to develop extensions to the core
functionality of MonetDB.

%files devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_includedir}/monetdb/copybinary.h
%{_includedir}/monetdb/gdk*.h
%{_includedir}/monetdb/matomic.h
%{_includedir}/monetdb/mstring.h
%exclude %{_includedir}/monetdb/monetdbe.h
%{_includedir}/monetdb/monet*.h
%{_libdir}/libbat*.so
%{_libdir}/pkgconfig/monetdb-gdk.pc
%dir %{_datadir}/monetdb
%dir %{_datadir}/monetdb/cmake
%{_datadir}/monetdb/cmake/gdkTargets*.cmake
%{_datadir}/monetdb/cmake/matomicTargets.cmake
%{_datadir}/monetdb/cmake/mstringTargets.cmake
%{_datadir}/monetdb/cmake/monetdb_config_headerTargets.cmake

%package mutils
Summary: MonetDB mutils library
Group: Applications/Databases

%description mutils
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains a shared library (libmutils) which is needed by
various other components.

%ldconfig_scriptlets mutils

%files mutils
%license COPYING
%defattr(-,root,root)
%{_libdir}/libmutils*.so.*

%package mutils-devel
Summary: MonetDB mutils library
Group: Applications/Databases
Requires: %{name}-mutils%{?_isa} = %{version}-%{release}

%description mutils-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the files to develop with the %{name}-mutils
library.

%files mutils-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_libdir}/libmutils*.so
%{_libdir}/pkgconfig/monetdb-mutils.pc
%{_datadir}/monetdb/cmake/mutilsTargets*.cmake

%package stream
Summary: MonetDB stream library
Group: Applications/Databases

%description stream
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains a shared library (libstream) which is needed by
various other components.

%ldconfig_scriptlets stream

%files stream
%license COPYING
%defattr(-,root,root)
%{_libdir}/libstream*.so.*

%package stream-devel
Summary: MonetDB stream library
Group: Applications/Databases
Requires: %{name}-stream%{?_isa} = %{version}-%{release}
Requires: %{name}-mutils-devel%{?_isa} = %{version}-%{release}
Requires: libbz2-devel
Requires: libcurl-devel
Requires: zlib-devel

%description stream-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the files to develop with the %{name}-stream
library.

%files stream-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_libdir}/libstream*.so
%{_includedir}/monetdb/stream.h
%{_includedir}/monetdb/stream_socket.h
%{_libdir}/pkgconfig/monetdb-stream.pc
%{_datadir}/monetdb/cmake/streamTargets*.cmake

%package client-lib
Summary: MonetDB - Monet Database Management System Client Programs
Group: Applications/Databases

%description client-lib
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains libmapi.so, the main client library used by both
mclient, msqldump and by the ODBC driver.  If you want to use MonetDB,
you will very likely need this package.

%ldconfig_scriptlets client-lib

%files client-lib
%license COPYING
%defattr(-,root,root)
%{_libdir}/libmapi*.so.*

%package client
Summary: MonetDB - Monet Database Management System Client Programs
Group: Applications/Databases
Requires: %{name}-client-lib%{?_isa} = %{version}-%{release}

%description client
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains mclient, the main client program to communicate
with the MonetDB database server, and msqldump, a program to dump the
SQL database so that it can be loaded back later.  If you want to use
MonetDB, you will very likely need this package.

%files client
%license COPYING
%defattr(-,root,root)
%{_bindir}/mclient*
%{_bindir}/msqldump*
%{_mandir}/man1/mclient.1*
%{_mandir}/man1/msqldump.1*

%package client-devel
Summary: MonetDB - Monet Database Management System Client Programs
Group: Applications/Databases
Requires: %{name}-client-lib%{?_isa} = %{version}-%{release}
Requires: %{name}-stream-devel%{?_isa} = %{version}-%{release}

%description client-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the files needed to develop with the
%{name}-client package.

%files client-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_libdir}/libmapi*.so
%{_includedir}/monetdb/mapi*.h
%{_includedir}/monetdb/msettings.h
%{_libdir}/pkgconfig/monetdb-mapi.pc
%{_datadir}/monetdb/cmake/mapiTargets*.cmake

%package client-odbc
Summary: MonetDB ODBC driver
Group: Applications/Databases
Requires: %{name}-client-lib%{?_isa} = %{version}-%{release}
Requires(post): %{_bindir}/odbcinst
Requires(postun): %{_bindir}/odbcinst

%description client-odbc
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the MonetDB ODBC driver.

%post client-odbc
# install driver if first install of package or if driver not installed yet
if [ "$1" -eq 1 ] || ! odbcinst -d -q -n MonetDB >& /dev/null; then
odbcinst -i -d -r <<EOF
[MonetDB]
Description = ODBC for MonetDB
Driver = %{_exec_prefix}/lib/libMonetODBC.so
Setup = %{_exec_prefix}/lib/libMonetODBCs.so
Driver64 = %{_exec_prefix}/lib64/libMonetODBC.so
Setup64 = %{_exec_prefix}/lib64/libMonetODBCs.so
EOF
fi

%postun client-odbc
if [ "$1" -eq 0 ]; then
odbcinst -u -d -n MonetDB
fi

%files client-odbc
%license COPYING
%defattr(-,root,root)
%{_libdir}/libMonetODBC.so
%{_libdir}/libMonetODBCs.so

%package client-tests
Summary: MonetDB Client tests package
Group: Applications/Databases
Requires: %{name}-server%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: %{name}-client-odbc%{?_isa} = %{version}-%{release}

%description client-tests
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the sample MAPI programs used for testing other
MonetDB packages.  You probably don't need this, unless you are a
developer.

%files client-tests
%defattr(-,root,root)
%{_bindir}/arraytest
%{_bindir}/backrefencode
%{_bindir}/bincopydata
%{_bindir}/malsample.pl
%{_bindir}/murltest
%{_bindir}/odbcconnect
%{_bindir}/ODBCgetInfo
%{_bindir}/ODBCmetadata
%{_bindir}/odbcsample1
%{_bindir}/ODBCStmtAttr
%{_bindir}/ODBCtester
%{_bindir}/sample0
%{_bindir}/sample1
%{_bindir}/sample4
%{_bindir}/shutdowntest
%{_bindir}/smack00
%{_bindir}/smack01
%{_bindir}/sqlsample.php
%{_bindir}/sqlsample.pl
%{_bindir}/streamcat
%{_bindir}/testcondvar


%package geom
Summary: SQL GIS support module for MonetDB
Group: Applications/Databases
Requires: %{name}-server%{?_isa} = %{version}-%{release}
Obsoletes: MonetDB-geom-MonetDB5 < 11.50.0
Provides: %{name}-geom-MonetDB5 = %{version}-%{release}
Provides: %{name}-geom-MonetDB5%{?_isa} = %{version}-%{release}

%description geom
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the GIS (Geographic Information System)
extensions for %{name}-server.

%files geom
%defattr(-,root,root)
%{_libdir}/monetdb5*/lib_geom.so


%package libs
Summary: MonetDB - Monet Database Main Libraries
Group: Applications/Databases
Obsoletes: MonetDB5-libs < 11.50.0
Provides: MonetDB5-libs = %{version}-%{release}
Provides: MonetDB5-libs%{?_isa} = %{version}-%{release}

%description libs
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the MonetDB server component in the form of a set
of libraries.  You need this package if you want to use the MonetDB
database system, either as independent program (%{name}-server) or as
embedded library (%{name}-embedded).

%ldconfig_scriptlets libs

%files libs
%defattr(-,root,root)
%{_libdir}/libmonetdb5*.so.*
%{_libdir}/libmonetdbsql*.so*
%dir %{_libdir}/monetdb5-%{version}
%{_libdir}/monetdb5*/lib_capi.so
%{_libdir}/monetdb5*/lib_csv.so
%{_libdir}/monetdb5*/lib_generator.so
%{_libdir}/monetdb5*/lib_monetdb_loader.so

%package odbc-loader
Summary: MonetDB ODBC loader module
Group: Applications/Databases
Requires: %{name}-server%{?_isa} = %{version}-%{release}

%description odbc-loader
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package provides an interface to the MonetDB server through which
data from remote databases can be loaded through an ODBC interface.  In
order to use this module, mserver5 needs to be run with the option
--loadmodule odbc_loader.

%files odbc-loader
%defattr(-,root,root)
%{_libdir}/monetdb5*/lib_odbc_loader.so

%package server
Summary: MonetDB - Monet Database Management System
Group: Applications/Databases
Requires(pre): shadow
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: MonetDB5-server < 11.50.0
Provides: MonetDB5-server = %{version}-%{release}
Provides: MonetDB5-server%{?_isa} = %{version}-%{release}
Requires(pre): systemd
Provides:       group(monetdb)
Provides:       user(monetdb)

%description server
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the MonetDB server component.  You need this
package if you want to use the MonetDB database system.  If you want to
use the monetdb and monetdbd programs to manage your databases
(recommended), you also need %{name}-SQL.

%pre server

getent group monetdb >/dev/null || groupadd --system monetdb
if getent passwd monetdb >/dev/null; then
    case $(getent passwd monetdb | cut -d: -f6) in
    %{_localstatedir}/MonetDB) # old value
        # change home directory, but not using usermod
        # usermod requires there to not be any running processes owned by the user
        EDITOR='sed -i "/^monetdb:/s|:%{_localstatedir}/MonetDB:|:%{_localstatedir}/lib/monetdb:|"'
        unset VISUAL
        export EDITOR
        /sbin/vipw > /dev/null
        ;;
    esac
else
    useradd --system --gid monetdb --home-dir %{_localstatedir}/lib/monetdb \
        --shell /sbin/nologin --comment "MonetDB Server" monetdb
fi
exit 0

%files server
%defattr(-,root,root)
%attr(2750,monetdb,monetdb) %dir %{_localstatedir}/lib/monetdb
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5/dbfarm
%{_bindir}/mserver5*
%{_mandir}/man1/mserver5.1*
%dir %{_datadir}/doc/MonetDB
%docdir %{_datadir}/doc/MonetDB
%{_datadir}/doc/MonetDB/*

%package server-devel
Summary: MonetDB development files
Group: Applications/Databases
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes: MonetDB5-server-devel < 11.50.0
Provides: MonetDB5-server-devel = %{version}-%{release}
Provides: MonetDB5-server-devel%{?_isa} = %{version}-%{release}

%description server-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains files needed to develop extensions that can be
used from the MAL level.

%files server-devel
%defattr(-,root,root)
%{_includedir}/monetdb/mal*.h
%{_includedir}/monetdb/mel.h
%{_libdir}/libmonetdb5*.so
%{_libdir}/pkgconfig/monetdb5.pc
%{_datadir}/monetdb/cmake/monetdb5Targets*.cmake

%package SQL
Summary: MonetDB SQL server modules
Group: Applications/Databases
Requires(pre): %{name}-server%{?_isa} = %{version}-%{release}
Obsoletes: MonetDB-SQL-server5 < 11.50.0
Provides: %{name}-SQL-server5 = %{version}-%{release}
Provides: %{name}-SQL-server5%{?_isa} = %{version}-%{release}
%{?systemd_requires}

%description SQL
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the monetdb and monetdbd programs and the systemd
configuration.

%post SQL
%systemd_post monetdbd.service

%preun SQL
%systemd_preun monetdbd.service

%postun SQL
%systemd_postun_with_restart monetdbd.service

%files SQL
%defattr(-,root,root)
%{_bindir}/monetdb*
%{_bindir}/monetdbd*
%dir %attr(775,monetdb,monetdb) %{_localstatedir}/log/monetdb
%dir %attr(775,monetdb,monetdb) %{_rundir}/monetdb
# RHEL >= 7, and all current Fedora
%{_tmpfilesdir}/monetdbd.conf
%{_unitdir}/monetdbd.service
%config(noreplace) %attr(664,monetdb,monetdb) %{_localstatedir}/monetdb5/dbfarm/.merovingian_properties
%verify(not mtime) %attr(664,monetdb,monetdb) %{_localstatedir}/monetdb5/dbfarm/.merovingian_lock
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/monetdbd
%{_mandir}/man1/monetdb.1*
%{_mandir}/man1/monetdbd.1*
%dir %{_datadir}/doc/MonetDB-SQL
%docdir %{_datadir}/doc/MonetDB-SQL
%{_datadir}/doc/MonetDB-SQL/*

%package SQL-devel
Summary: MonetDB SQL server modules development files
Group: Applications/Databases
Requires: %{name}-SQL%{?_isa} = %{version}-%{release}
Requires: %{name}-server-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-embedded-devel%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-SQL-server5-devel < 11.50.0
Provides: %{name}-SQL-server5-devel = %{version}-%{release}
Provides: %{name}-SQL-server5-devel%{?_isa} = %{version}-%{release}

%description SQL-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains files needed to develop SQL extensions.

%files SQL-devel
%defattr(-,root,root)
%{_includedir}/monetdb/opt_backend.h
%{_includedir}/monetdb/rel_*.h
%{_includedir}/monetdb/sql*.h
%{_includedir}/monetdb/store_*.h
%{_datadir}/monetdb/cmake/MonetDBConfig*.cmake
%{_datadir}/monetdb/cmake/sqlTargets*.cmake

%package embedded
Summary: MonetDB as an embedded library
Group: Applications/Databases
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description embedded
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the library to turn MonetDB into an embeddable
library, also known as MonetDBe.  Also see %{name}-embedded-devel to
use this in a program.

%ldconfig_scriptlets embedded

%files embedded
%{_libdir}/libmonetdbe.so.*

%package embedded-devel
Summary: MonetDB as an embedded library development files
Group: Applications/Databases
Requires: %{name}-embedded%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description embedded-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the library and include files to create a
program that uses MonetDB as an embeddable library.

%files embedded-devel
%defattr(-,root,root)
%{_libdir}/libmonetdbe.so
%{_includedir}/monetdb/monetdbe.h
%{_libdir}/pkgconfig/monetdbe.pc
%{_datadir}/monetdb/cmake/monetdbeTargets*.cmake

%package embedded-tests
Summary: MonetDBe tests package
Group: Applications/Databases
Requires: %{name}-embedded%{?_isa} = %{version}-%{release}

%description embedded-tests
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains some test programs using the %{name}-embedded
package.  You probably don't need this, unless you are a developer.

%files embedded-tests
%defattr(-,root,root)
%{_bindir}/example_proxy

%prep
%setup -q

%build
mkdir build
cd build
cmake .. \
	-DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DDESTDIR=%{buildroot} \
        -DCMAKE_INSTALL_RUNSTATEDIR=/run \
        -DRELEASE_VERSION=ON \
        -DASSERT=OFF \
        -DCINTEGRATION=ON \
        -DFITS=OFF \
        -DGEOM=ON \
        -DINT128=ON \
        -DNETCDF=OFF \
        -DODBC=ON \
        -DPY3INTEGRATION=OFF \
        -DRINTEGRATION=OFF \
        -DSANITIZER=OFF \
        -DSHP=OFF \
        -DSTRICT=OFF \
        -DTESTING=ON \
        -DWITH_BZ2=ON \
        -DWITH_CMOCKA=OFF \
        -DWITH_CURL=ON \
        -DWITH_LZ4=ON \
        -DWITH_LZMA=ON \
        -DWITH_OPENSSL=ON \
        -DWITH_PCRE=ON \
        -DWITH_PROJ=OFF \
        -DWITH_READLINE=ON \
        -DWITH_RTREE=OFF \
        -DWITH_SQLPARSE=OFF \
        -DWITH_VALGRIND=OFF \
        -DWITH_XML2=ON \
        -DWITH_ZLIB=ON

cmake --build .

%install
mkdir -p %{buildroot}/usr
for d in etc var; do mkdir %{buildroot}/$d; ln -s ../$d %{buildroot}/usr/$d; done

cd build
make DESTDIR=%{buildroot} install

cd ..
rm %{buildroot}/usr/var %{buildroot}/usr/etc

# move file to correct location
mkdir -p %{buildroot}%{_tmpfilesdir}
mv %{buildroot}%{_sysconfdir}/tmpfiles.d/monetdbd.conf %{buildroot}%{_tmpfilesdir}
rmdir %{buildroot}%{_sysconfdir}/tmpfiles.d

install -d -m 0750 %{buildroot}%{_localstatedir}/lib/monetdb
install -d -m 0770 %{buildroot}%{_localstatedir}/monetdb5/dbfarm
install -d -m 0775 %{buildroot}%{_localstatedir}/log/monetdb
install -d -m 0775 %{buildroot}%{_rundir}/monetdb

# remove unwanted stuff
rm -f %{buildroot}%{_libdir}/monetdb5*/lib_opt_sql_append.so
rm -f %{buildroot}%{_libdir}/monetdb5*/lib_microbenchmark*.so
rm -f %{buildroot}%{_libdir}/monetdb5*/lib_udf*.so
rm -f %{buildroot}%{_bindir}/monetdb_mtest.sh
rm -f %{buildroot}%{_bindir}/Mconvert.py
rm -f %{buildroot}%{_bindir}/Mtest.py
rm -f %{buildroot}%{_bindir}/Mz.py
rm -f %{buildroot}%{_bindir}/mktest.py
rm -f %{buildroot}%{_bindir}/sqllogictest.py
rm -rf %{buildroot}%{python3_sitelib}/MonetDBtesting

%changelog

