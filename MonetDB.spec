%define name MonetDB
%define version 11.33.11

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
Source: http://dev.monetdb.org/downloads/sources/Aug2018/%{name}-%{version}.tar.xz

BuildRequires: sed
BuildRequires: systemd
BuildRequires: bison
BuildRequires: libbz2-devel
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
BuildRequires: pcre-devel >= 4.5
BuildRequires: readline-devel
BuildRequires: unixODBC-devel
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

%package stream
Summary: MonetDB stream library
Group: Applications/Databases

%description stream
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains a shared library (libstream) which is needed by
various other components.

%files stream
%license COPYING
%defattr(-,root,root)
%{_libdir}/libstream.so.*

%package stream-devel
Summary: MonetDB stream library
Group: Development/Libraries/Other
Requires: %{name}-stream%{?_isa} = %{version}-%{release}
Requires: libbz2-devel
Requires: libcurl-devel
Requires: zlib-devel

%description stream-devel
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the files to develop with the %{name}-stream
library.

%files stream-devel
%defattr(-,root,root)
%dir %{_includedir}/monetdb
%{_libdir}/libstream.so
%{_includedir}/monetdb/stream.h
%{_includedir}/monetdb/stream_socket.h
%{_libdir}/pkgconfig/monetdb-stream.pc

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
%{_includedir}/monetdb/gdk*.h
%{_includedir}/monetdb/monet*.h
%{_libdir}/libbat.so
%{_libdir}/pkgconfig/monetdb-gdk.pc

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

%package client-tools
Summary: MonetDB - Monet Database Management System Client Programs
Group: Applications/Databases
Requires: %{name}-client%{?_isa} = %{version}-%{release}

%description client-tools
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains stethoscope, tomograph, and tachograph.  These
tools can be used to monitor the MonetDB database server.

%files client-tools
%defattr(-,root,root)
%{_bindir}/stethoscope
%{_bindir}/tachograph
%{_bindir}/tomograph
%dir %{_datadir}/doc/MonetDB-client-tools
%docdir %{_datadir}/doc/MonetDB-client-tools
%{_datadir}/doc/MonetDB-client-tools/*

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
%{_includedir}/monetdb/mapi.h
%{_libdir}/pkgconfig/monetdb-mapi.pc

%package client-odbc
Summary: MonetDB ODBC driver
Group: Applications/Databases
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires(pre): unixODBC

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
Requires: %{name}-SQL-server5%{?_isa} = %{version}-%{release}
Requires: python-pymonetdb >= 1.0

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
%{_bindir}/arraytest
%{_bindir}/odbcsample1
%{_bindir}/sample0
%{_bindir}/sample1
%{_bindir}/sample4
%{_bindir}/smack00
%{_bindir}/smack01
%{_bindir}/shutdowntest
%{_bindir}/testgetinfo
%{_bindir}/testStmtAttr
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
%{_libdir}/monetdb5/autoload/*_geom.mal
%{_libdir}/monetdb5/createdb/*_geom.sql
%{_libdir}/monetdb5/geom.mal
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
%{_libdir}/monetdb5/rapi.*
%{_libdir}/monetdb5/autoload/*_rapi.mal
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
%{_libdir}/monetdb5/pyapi3.*
%{_libdir}/monetdb5/autoload/*_pyapi3.mal
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
getent group monetdb >/dev/null || groupadd -r monetdb
getent passwd monetdb >/dev/null || \
useradd -r -g monetdb -d %{_localstatedir}/MonetDB -s /sbin/nologin \
    -c "MonetDB Server" monetdb
exit 0

%post -n MonetDB5-server
# move database from old location to new location
if [ -d %{_localstatedir}/MonetDB5/dbfarm -a ! %{_localstatedir}/MonetDB5/dbfarm -ef %{_localstatedir}/monetdb5/dbfarm ]; then
	# old database exists and is different from new
	if [ $(find %{_localstatedir}/monetdb5 -print | wc -l) -le 2 ]; then
		# new database is still empty
		rmdir %{_localstatedir}/monetdb5/dbfarm
		rmdir %{_localstatedir}/monetdb5
		mv %{_localstatedir}/MonetDB5 %{_localstatedir}/monetdb5
	fi
fi

%files -n MonetDB5-server
%defattr(-,root,root)
%attr(750,monetdb,monetdb) %dir %{_localstatedir}/MonetDB
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5
%attr(2770,monetdb,monetdb) %dir %{_localstatedir}/monetdb5/dbfarm
%{_bindir}/mserver5
%{_libdir}/libmonetdb5.so.*
%dir %{_libdir}/monetdb5
%dir %{_libdir}/monetdb5/autoload
%exclude %{_libdir}/monetdb5/geom.mal
%exclude %{_libdir}/monetdb5/pyapi3.mal
%exclude %{_libdir}/monetdb5/rapi.mal
%exclude %{_libdir}/monetdb5/sql*.mal
%if %{bits} == 64
%exclude %{_libdir}/monetdb5/*_hge.mal
%exclude %{_libdir}/monetdb5/autoload/*_hge.mal
%endif
%exclude %{_libdir}/monetdb5/autoload/*_geom.mal
%exclude %{_libdir}/monetdb5/autoload/*_pyapi3.mal
%exclude %{_libdir}/monetdb5/autoload/*_rapi.mal
%{_libdir}/monetdb5/*.mal
%exclude %{_libdir}/monetdb5/autoload/??_sql*.mal
%{_libdir}/monetdb5/autoload/*.mal
%exclude %{_libdir}/monetdb5/lib_geom.so
%exclude %{_libdir}/monetdb5/lib_pyapi3.so
%exclude %{_libdir}/monetdb5/lib_rapi.so
%exclude %{_libdir}/monetdb5/lib_sql.so
%{_libdir}/monetdb5/*.so
%doc %{_mandir}/man1/mserver5.1.gz
%dir %{_datadir}/doc/MonetDB
%docdir %{_datadir}/doc/MonetDB
%{_datadir}/doc/MonetDB/*

%if %{bits} == 64
%package -n MonetDB5-server-hugeint
Summary: MonetDB - 128-bit integer support for MonetDB5-server
Group: Applications/Databases
Requires: MonetDB5-server%{?_isa}

%description -n MonetDB5-server-hugeint
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package provides HUGEINT (128-bit integer) support for the
MonetDB5-server component.

%files -n MonetDB5-server-hugeint
%exclude %{_libdir}/monetdb5/sql*_hge.mal
%{_libdir}/monetdb5/*_hge.mal
%exclude %{_libdir}/monetdb5/autoload/??_sql_hge.mal
%{_libdir}/monetdb5/autoload/*_hge.mal
%endif

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
%{_libdir}/libmonetdb5.so
%{_libdir}/pkgconfig/monetdb5.pc

%package SQL-server5
Summary: MonetDB5 SQL server modules
Group: Applications/Databases
Requires: MonetDB5-server%{?_isa} = %{version}-%{release}
%if %{?rhel:0}%{!?rhel:1} || 0%{?rhel} >= 7
# RHEL >= 7, and all current Fedora
Requires: %{_bindir}/systemd-tmpfiles
%endif
%if (0%{?fedora} >= 22)
%if %{bits} == 64
Recommends: %{name}-SQL-server5-hugeint%{?_isa} = %{version}-%{release}
%endif
Suggests: %{name}-client%{?_isa} = %{version}-%{release}
%endif

%description SQL-server5
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the SQL frontend for MonetDB.  If you want to
use SQL with MonetDB, you will need to install this package.

%if %{?rhel:0}%{!?rhel:1} || 0%{?rhel} >= 7
%post SQL-server5
systemd-tmpfiles --create %{_sysconfdir}/tmpfiles.d/monetdbd.conf
%endif

%files SQL-server5
%defattr(-,root,root)
%{_bindir}/monetdb
%{_bindir}/monetdbd
%dir %attr(775,monetdb,monetdb) %{_localstatedir}/log/monetdb
%{_sysconfdir}/tmpfiles.d/monetdbd.conf
%{_unitdir}/monetdbd.service
%config(noreplace) %{_localstatedir}/monetdb5/dbfarm/.merovingian_properties
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/logrotate.d/monetdbd
%{_libdir}/monetdb5/autoload/??_sql.mal
%{_libdir}/monetdb5/lib_sql.so
%dir %{_libdir}/monetdb5/createdb
%exclude %{_libdir}/monetdb5/createdb/*_geom.sql
%{_libdir}/monetdb5/createdb/*.sql
%{_libdir}/monetdb5/sql*.mal
%if %{bits} == 64
%exclude %{_libdir}/monetdb5/createdb/*_hge.sql
%exclude %{_libdir}/monetdb5/sql*_hge.mal
%endif
%doc %{_mandir}/man1/monetdb.1.gz
%doc %{_mandir}/man1/monetdbd.1.gz
%dir %{_datadir}/doc/MonetDB-SQL
%docdir %{_datadir}/doc/MonetDB-SQL
%{_datadir}/doc/MonetDB-SQL/*

%if %{bits} == 64
%package SQL-server5-hugeint
Summary: MonetDB5 128 bit integer (hugeint) support for SQL
Group: Applications/Databases
Requires: MonetDB5-server-hugeint%{?_isa} = %{version}-%{release}
Requires: MonetDB-SQL-server5%{?_isa} = %{version}-%{release}

%description SQL-server5-hugeint
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package provides HUGEINT (128-bit integer) support for the SQL
frontend of MonetDB.

%files SQL-server5-hugeint
%defattr(-,root,root)
%{_libdir}/monetdb5/autoload/??_sql_hge.mal
%{_libdir}/monetdb5/createdb/*_hge.sql
%{_libdir}/monetdb5/sql*_hge.mal
%endif

%package testing
Summary: MonetDB - Monet Database Management System
Group: Applications/Databases

%description testing
MonetDB is a database management system that is developed from a
main-memory perspective with use of a fully decomposed storage model,
automatic index management, extensibility of data types and search
accelerators.  It also has an SQL frontend.

This package contains the programs and files needed for testing the
MonetDB packages.  You probably don't need this, unless you are a
developer.  If you do want to test, install %{name}-testing-python.

%files testing
%license COPYING
%defattr(-,root,root)
%{_bindir}/Mdiff
%{_bindir}/Mlog

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
%{_bindir}/Mapprove.py
%{_bindir}/Mtest.py
%dir %{python2_sitelib}/MonetDBtesting
%{python2_sitelib}/MonetDBtesting/*

%prep
%setup -q

sed -i 's/WIN32?//g' clients/mapilib/Makefile.ag
sed -i 's/@WIN32_TRUE@//g' clients/mapilib/Makefile.in
sed -i 's/WIN32?//g' common/stream/Makefile.ag
sed -i 's/@WIN32_TRUE@//g' common/stream/Makefile.in

%build

# There is a bug in GCC version 4.8 on AArch64 architectures
# that causes it to report an internal error when compiling
# testing/difflib.c.  The work around is to not use -fstack-protector-strong.
# The bug exhibits itself on CentOS 7 on AArch64.
if [ `gcc -v 2>&1 | grep -c 'Target: aarch64\|gcc version 4\.'` -eq 2 ]; then
	# set CFLAGS before configure, so that this value gets used
	CFLAGS='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches  '
	export CFLAGS
fi
%{configure} \
	--enable-assert=no \
	--enable-console=yes \
	--enable-debug=no \
	--enable-developer=no \
	--enable-embedded=no \
	--enable-embedded-r=no \
	--enable-fits=no \
	--enable-gdk=yes \
	--enable-geom=yes \
	--enable-int128=%{?with_int128:yes}%{!?with_int128:no} \
	--enable-lidar=no \
	--enable-mapi=yes \
	--enable-monetdb5=yes \
	--enable-netcdf=no \
	--enable-odbc=yes \
	--enable-optimize=yes \
	--enable-py2integration=no \
	--enable-py3integration=yes \
	--enable-rintegration=yes \
	--enable-shp=no \
	--enable-sql=yes \
	--enable-strict=no \
	--enable-testing=yes \
	--with-bz2=yes \
	--with-curl=yes \
	--with-gdal=no \
	--with-geos=yes \
	--with-liblas=no \
	--with-libxml2=yes \
	--with-lz4=no \
	--with-lzma=yes \
	--with-openssl=yes \
	--with-regex=PCRE \
	--with-proj=no \
	--with-pthread=yes \
	--with-python2=yes \
	--with-python3=yes \
	--with-readline=yes \
	--with-samtools=no \
	--with-snappy=no \
	--with-unixodbc=yes \
	--with-uuid=yes \
	--with-valgrind=no \
	%{?comp_cc:CC="%{comp_cc}"}

make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}%{_localstatedir}/MonetDB
mkdir -p %{buildroot}%{_localstatedir}/monetdb5/dbfarm
mkdir -p %{buildroot}%{_localstatedir}/log/monetdb
mkdir -p %{buildroot}%{_localstatedir}/run/monetdb

# remove unwanted stuff
# .la files
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/monetdb5/*.la
# internal development stuff
rm -f %{buildroot}%{_bindir}/Maddlog

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
