Summary:	UDF writing tools for CDRW recorders
Summary(pl):	Narzêdzia umo¿liwaj±ce zapisywanie na p³ytach CDRW w formacie UDF
Name:		udftools
Version:	1.0.0b2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/linux-udf/%{name}-%{version}.tar.gz
# Source0-md5: e1fe1e18d31512f343f215ef2379ad0c
Patch0:		%{name}-acam.patch
URL:		http://linux-udf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to use CDRW disks like a normal floppy disks.
The data can modified and deleted. Disks can be read in any UDF
compatibile system.

%description -l pl
Ten pakiet umo¿liwia nagrywanie na dyskach CDRW jak na normalnych
dyskietkach. Dane mo¿na usuwaæ i modyfikowaæ. Odczyt jest mo¿liwy na
systemach obs³uguj±cych system plików UDF.

%package devel
Summary:	udftools - libudffs header files
Summary(pl):	udftools - pliki nag³ówkowe dla libudffs
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
udftools - libudffs header files.

%description devel -l pl
udftools - pliki nag³ówkowe dla libudffs.

%package static
Summary:	Static libudffs library
Summary(pl):	Statyczna biblioteka libudffs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libudffs library.

%description static -l pl
Statyczna biblioteka libudffs.

%prep
%setup -q
%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_includedir}/udffs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install include/{config,defaults,ecma_167r3,libudffs,osta_udf201,udf_endian}.h \
	$RPM_BUILD_ROOT%{_includedir}/udffs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/udffs

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
