%define name MonetDB
%define version 11.47.11

# groups of related archs
%define all_x86 i386 i586 i686

%ifarch %{all_x86}
%define bits 32
%else
%define bits 64
%define with_int128 1
%endif

%define release 0

%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name: %{name}
Version: %{version}
Release: %{release}
Summary: MonetDB - Monet Database Management System
Vendor: MonetDB BV <info@monetdb.org>

Group: Applications/Databases
License: MPLv2.0
URL: http://www.monetdb.org/
Source: http://dev.monetdb.org/downloads/sources/Oct2020-SP1/%{name}-%{version}.tar.xz

BuildRequires: systemd
BuildRequires: bison
BuildRequires: libbz2-devel
BuildRequires: cmake >= 3.12
BuildRequires: gcc
BuildRequires: geos-devel >= 3.4.0
# BuildRequires: gsl-devel
BuildRequires: libcurl-devel
BuildRequires: xz-devel
# BuildRequires: libmicrohttpd-devel
# BuildRequires: libsphinxclient-devel
BuildRequires: libuuid-devel
BuildRequires: libxml2-devel
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: unixODBC-devel
BuildRequires: readline-devel
# BuildRequires: uriparser-devel
BuildRequires: zlib-devel
BuildRequires: python3-devel >= 3.5
BuildRequires: python3-numpy-devel
BuildRequires: R-core-devel
BuildRequires: libicu-devel

%description
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the core components of MonetDB in the form of a
single shared library.  If you want to use MonetDB, you will certainly
need this package, but you will also need at least the MonetDB5-server
package, and most likely also %{name}-SQL-server5, as well as one or
more client packages.

%files
%license COPYING
%defattr(-,root,root)
%{_libdir}/libbat.so.*

%package devel
Summary: MonetDB development files
Group: Development/Libraries/Other
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-stream-devel%{?_isa} = %{version}-%{release}

%description devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

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
%{_libdir}/libbat.so
%{_libdir}/pkgconfig/monetdb-gdk.pc

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

%files stream
%license COPYING
%defattr(-,root,root)
%{_libdir}/libstream.so.*

%package stream-devel
Summary: MonetDB stream library
Group: Applications/Databases
Requires: %{name}-stream%{?_isa} = %{version}-%{release}
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
%{_libdir}/libstream.so
%{_includedir}/monetdb/stream.h
%{_includedir}/monetdb/stream_socket.h
%{_libdir}/pkgconfig/monetdb-stream.pc

%package client
Summary: MonetDB - Monet Database Management System Client Programs
Group: Applications/Databases

%description client
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains mclient, the main client program to communicate
with the MonetDB database server, and msqldump, a program to dump the
SQL database so that it can be loaded back later.  If you want to use
MonetDB, you will very likely need this package.

%files client
%license COPYING
%defattr(-,root,root)
%{_bindir}/mclient
%{_bindir}/msqldump
%{_libdir}/libmapi.so.*
%doc %{_mandir}/man1/mclient.1.gz
%doc %{_mandir}/man1/msqldump.1.gz

%package client-devel
Summary: MonetDB - Monet Database Management System Client Programs
Group: Development/Libraries/Other
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: %{name}-stream-devel%{?_isa} = %{version}-%{release}
Requires: openssl-devel

%description client-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the files needed to develop with the
%{name}-client package.

%files client-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_libdir}/libmapi.so
%{_includedir}/monetdb/mapi*.h
%{_libdir}/pkgconfig/monetdb-mapi.pc

%package client-odbc
Summary: MonetDB ODBC driver
Group: Applications/Databases
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires(post): unixODBC
Requires(postun): unixODBC

%description client-odbc
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

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
Requires: MonetDB5-server%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: %{name}-client-odbc%{?_isa} = %{version}-%{release}
%if (0%{?fedora} >= 22)
Recommends: perl-DBD-monetdb >= 1.0
Recommends: php-monetdb >= 1.0
%endif
Requires: MonetDB5-server%{?_isa} = %{version}-%{release}
Requires: python3-pymonetdb >= 1.0.6

%description client-tests
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the sample MAPI programs used for testing other
MonetDB packages.  You probably don't need this, unless you are a
developer.

%files client-tests
%defattr(-,root,root)
%{_bindir}/ODBCStmtAttr
%{_bindir}/ODBCgetInfo
%{_bindir}/ODBCmetadata
%{_bindir}/ODBCtester
%{_bindir}/arraytest
%{_bindir}/bincopydata
%{_bindir}/odbcsample1
%{_bindir}/sample0
%{_bindir}/sample1
%{_bindir}/sample4
%{_bindir}/shutdowntest
%{_bindir}/smack00
%{_bindir}/smack01
%{_bindir}/streamcat
%{_bindir}/testcondvar
%{_bindir}/malsample.pl
%{_bindir}/sqlsample.php
%{_bindir}/sqlsample.pl

%package geom-MonetDB5
Summary: MonetDB5 SQL GIS support module
Group: Applications/Databases
Requires: MonetDB5-server%{?_isa} = %{version}-%{release}

%description geom-MonetDB5
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the GIS (Geographic Information System)
extensions for %{name}-SQL-server5.

%files geom-MonetDB5
%defattr(-,root,root)
%{_libdir}/monetdb5/lib_geom.so

%package R
Summary: Integration of MonetDB and R, allowing use of R from within SQL
Group: Applications/Databases
Requires: MonetDB-SQL-server5%{?_isa} = %{version}-%{release}

%description R
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the interface to use the R language from within
SQL queries.

NOTE: INSTALLING THIS PACKAGE OPENS UP SECURITY ISSUES.  If you don't
know how this package affects the security of your system, do not
install it.

%files R
%defattr(-,root,root)
%{_libdir}/monetdb5/rapi.R
%{_libdir}/monetdb5/lib_rapi.so

%package python3
Summary: Integration of MonetDB and Python, allowing use of Python from within SQL
Group: Applications/Databases
Requires: MonetDB-SQL-server5%{?_isa} = %{version}-%{release}

%description python3
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the interface to use the Python language from
within SQL queries.  This package is for Python 3.

NOTE: INSTALLING THIS PACKAGE OPENS UP SECURITY ISSUES.  If you don't
know how this package affects the security of your system, do not
install it.

%files python3
%defattr(-,root,root)
%{_libdir}/monetdb5/lib_pyapi3.so

%package -n MonetDB5-server
Summary: MonetDB - Monet Database Management System
Group: Applications/Databases
Requires(pre): pwdutils
Requires: %{name}-client%{?_isa} = %{version}-%{release}

%description -n MonetDB5-server
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the MonetDB server component.  You need this
package if you want to use the MonetDB database system.  If you want
to use the SQL frontend, you also need %{name}-SQL-server5.

%pre -n MonetDB5-server
%{?sysusers_create_package:echo 'u monetdb - "MonetDB Server" /var/lib/monetdb' | systemd-sysusers --replace=%_sysusersdir/monetdb.conf -}


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

%files -n MonetDB5-server
%defattr(-,root,root)
%attr(2750,monetdb,monetdb) %dir %{_localstatedir}/lib/monetdb
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5/dbfarm
%{_bindir}/mserver5
%{_libdir}/libmonetdb5.so.*
%{_libdir}/libmonetdbsql.so*
%dir %{_libdir}/monetdb5
%{_libdir}/monetdb5/lib_capi.so
%{_libdir}/monetdb5/lib_generator.so
%{_libdir}/monetdb5/lib_udf.so
%doc %{_mandir}/man1/mserver5.1.gz
%dir %{_datadir}/doc/MonetDB
%docdir %{_datadir}/doc/MonetDB
%{_datadir}/doc/MonetDB/*

%package -n MonetDB5-server-devel
Summary: MonetDB development files
Group: Development/Libraries/Other
Requires: MonetDB5-server%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description -n MonetDB5-server-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains files needed to develop extensions that can be
used from the MAL level.

%files -n MonetDB5-server-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_includedir}/monetdb/mal*.h
%{_includedir}/monetdb/mel.h
%{_libdir}/libmonetdb5.so
%{_libdir}/pkgconfig/monetdb5.pc

%package SQL-server5
Summary: MonetDB5 SQL server modules
Group: Applications/Databases
Requires(pre): MonetDB5-server%{?_isa} = %{version}-%{release}
Obsoletes: %{name}-SQL-server5-hugeint < 11.38.0
%if %{with hugeint}
Provides: %{name}-SQL-server5-hugeint%{?_isa} = %{version}-%{release}
%endif
%if (0%{?fedora} >= 22)
Suggests: %{name}-client%{?_isa} = %{version}-%{release}
%endif
%if %{?rhel:0}%{!?rhel:1} || 0%{?rhel} >= 7
%{?systemd_requires}
%endif

%description SQL-server5
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the monetdb and monetdbd programs and the systemd
configuration.

%files SQL-server5
%defattr(-,root,root)
%{_bindir}/monetdb
%{_bindir}/monetdbd
%dir %attr(775,monetdb,monetdb) %{_localstatedir}/log/monetdb
%dir %attr(775,monetdb,monetdb) %{_localstatedir}/run/monetdb
%{_sysconfdir}/tmpfiles.d/monetdbd.conf
%{_unitdir}/monetdbd.service
%config(noreplace) %attr(664,monetdb,monetdb) %{_localstatedir}/monetdb5/dbfarm/.merovingian_properties
%verify(not mtime) %attr(664,monetdb,monetdb) %{_localstatedir}/monetdb5/dbfarm/.merovingian_lock
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/monetdbd
%doc %{_mandir}/man1/monetdb.1.gz
%doc %{_mandir}/man1/monetdbd.1.gz
%dir %{_datadir}/doc/MonetDB-SQL
%docdir %{_datadir}/doc/MonetDB-SQL
%{_datadir}/doc/MonetDB-SQL/*

%package SQL-server5-devel
Summary: MonetDB5 SQL server modules
Group: Applications/Databases
Requires: %{name}-SQL-server5%{?_isa} = %{version}-%{release}
Requires: MonetDB5-server-devel%{?_isa} = %{version}-%{release}

%description SQL-server5-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains files needed to develop SQL extensions.

%files SQL-server5-devel
%defattr(-,root,root)
%{_includedir}/monetdb/exception_buffer.h
%{_includedir}/monetdb/opt_backend.h
%{_includedir}/monetdb/rel_*.h
%{_includedir}/monetdb/sql*.h
%{_includedir}/monetdb/store_*.h

%package embedded
Summary: MonetDB as an embedded library
Group: Applications/Databases

%description embedded
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL front end.

This package contains the library to turn MonetDB into an embeddable
library.  Also see %{name}-embedded-devel to use this in a program.

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

%package testing-python
Summary: MonetDB - Monet Database Management System
Group: Applications/Databases
Requires: %{name}-testing = %{version}-%{release}
Requires: %{name}-client-tests = %{version}-%{release}
Requires: python
BuildArch: noarch

%description testing-python
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the Python programs and files needed for testing
the MonetDB packages.  You probably don't need this, unless you are a
developer, but if you do want to test, this is the package you need.

%files testing-python
%defattr(-,root,root)
%{_bindir}/Mconvert.py
%{_bindir}/Mtest.py
%{_bindir}/Mz.py
%{_bindir}/mktest.py
%{_bindir}/sqllogictest.py
%dir %{python3_sitelib}/MonetDBtesting
%{python3_sitelib}/MonetDBtesting/*

%prep
%setup -q

#sed -i 's/WIN32?//g' clients/mapilib/Makefile.ag
#sed -i 's/@WIN32_TRUE@//g' clients/mapilib/Makefile.in
#sed -i 's/WIN32?//g' common/stream/Makefile.ag
#sed -i 's/@WIN32_TRUE@//g' common/stream/Makefile.in

%build
cmake \
	-DRELEASE_VERSION=ON \
    -DRUNDIR=/var/run/monetdb \
    -DLOGDIR=/var/log/monetdb \
	-DASSERT=OFF \
	-DCINTEGRATION=ON \
	-DFITS=NO \
	-DGEOM=YES \
	-DINT128=ON \
	-DNETCDF=OFF \
	-DODBC=ON \
	-DPY3INTEGRATION=ON \
	-DRINTEGRATION=ON \
	-DSANITIZER=OFF \
	-DSHP=OFF \
	-DSTRICT=OFF \
	-DTESTING=ON \
	-DWITH_BZ2=ON \
	-DWITH_CMOCKA=OFF \
	-DWITH_CRYPTO=ON \
	-DWITH_CURL=ON \
	-DWITH_LZ4=OFF \
	-DWITH_LZMA=ON \
	-DWITH_PCRE=ON \
	-DWITH_PROJ=OFF \
	-DWITH_READLINE=ON \
	-DWITH_SNAPPY=OFF \
	-DWITH_UUID=ON \
	-DWITH_VALGRIND=OFF \
	-DWITH_XML2=ON \
	-DWITH_ZLIB=ON

cmake -DCMAKE_INSTALL_PREFIX=/usr .
cmake --build .

%install
mkdir -p "%{buildroot}/usr"
for d in etc var; do mkdir "%{buildroot}/$d"; ln -s ../$d "%{buildroot}/usr/$d"; done
%make_install
rm "%{buildroot}/usr/var" "%{buildroot}/usr/etc"

install -d -m 0750 %{buildroot}%{_localstatedir}/lib/monetdb
install -d -m 0770 %{buildroot}%{_localstatedir}/monetdb5/dbfarm
install -d -m 0775 %{buildroot}%{_localstatedir}/log/monetdb
install -d -m 0775 %{buildroot}%{_localstatedir}/run/monetdb

# remove unwanted stuff
# .la files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/monetdb5/*.la
rm -f %{buildroot}%{_libdir}/monetdb5/lib_opt_sql_append.so
rm -f %{buildroot}%{_libdir}/monetdb5/run_*.mal
rm -f %{buildroot}%{_libdir}/monetdb5/lib_run_*.so
rm -f %{buildroot}%{_libdir}/monetdb5/microbenchmark.mal
rm -f %{buildroot}%{_libdir}/monetdb5/lib_microbenchmark*.so
rm -f %{buildroot}%{_bindir}/monetdb_mtest.sh
rm -rf %{buildroot}%{_datadir}/monetdb # /cmake

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
