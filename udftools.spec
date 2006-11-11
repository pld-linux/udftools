Summary:	UDF writing tools for CDRW recorders
Summary(pl):	Narzêdzia umo¿liwiaj±ce zapisywanie na p³ytach CDRW w formacie UDF
Name:		udftools
Version:	1.0.0b3
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-udf/%{name}-%{version}.tar.gz
# Source0-md5:	2f491ddd63f31040797236fe18db9e60
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-pktcdvd.patch
Patch2:		%{name}-gcc4.patch
Patch3:		%{name}-warnings.patch
URL:		http://linux-udf.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		specflags	-Wall

%description
This package allows to use CDRW disks like a normal floppy disks. The
data can modified and deleted. Disks can be read in any UDF
compatibile system.

%description -l pl
Ten pakiet umo¿liwia nagrywanie na dyskach CDRW jak na normalnych
dyskietkach. Dane mo¿na usuwaæ i modyfikowaæ. Odczyt jest mo¿liwy na
systemach obs³uguj±cych system plików UDF.

%package devel
Summary:	udftools - libudffs header files
Summary(pl):	udftools - pliki nag³ówkowe dla libudffs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
udftools - libudffs header files.

%description devel -l pl
udftools - pliki nag³ówkowe dla libudffs.

%package static
Summary:	Static libudffs library
Summary(pl):	Statyczna biblioteka libudffs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libudffs library.

%description static -l pl
Statyczna biblioteka libudffs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir}/udffs,%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install include/{bswap,config,defaults,ecma_167,libudffs,osta_udf,udf_endian,udf_lib}.h \
	$RPM_BUILD_ROOT%{_includedir}/udffs

ln -s %{_bindir}/mkudffs $RPM_BUILD_ROOT%{_sbindir}/mkfs.udf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/cdrwtool
%attr(755,root,root) %{_bindir}/mkudffs
%attr(755,root,root) %{_bindir}/pktsetup
%attr(755,root,root) %{_bindir}/udffsck
%attr(755,root,root) %{_bindir}/wrudf
%attr(755,root,root) %{_sbindir}/mkfs.udf
%attr(755,root,root) %{_libdir}/libudffs.so.*.*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudffs.so
%{_libdir}/libudffs.la
%{_includedir}/udffs

%files static
%defattr(644,root,root,755)
%{_libdir}/libudffs.a
