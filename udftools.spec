#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Linux tools for UDF filesystems and DVD/CD-R(W) drives
Summary(pl.UTF-8):	Linuksowe narzędzia do systemów plików UDF oraz nagrywarek DVD/CD-R(W)
Name:		udftools
Version:	2.3
Release:	1
License:	GPL v2+
Group:		Applications/System
#Source0Download: https://github.com/pali/udftools/releases
Source0:	https://github.com/pali/udftools/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	eada8dd40a675763ec71c35655cfd85e
Patch0:		%{name}-shared.patch
URL:		http://linux-udf.sourceforge.net/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		specflags	-Wall -fno-strict-aliasing

%description
This package allows to use DVD/CDRW disks like a normal floppy disks.
The data can modified and deleted. Disks can be read in any UDF
compatibile system.

%description -l pl.UTF-8
Ten pakiet umożliwia nagrywanie na płytach DVD/CDRW jak na normalnych
dyskietkach. Dane można usuwać i modyfikować. Odczyt jest możliwy na
systemach obsługujących system plików UDF.

%package devel
Summary:	Header files for libudffs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libudffs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libudffs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libudffs.

%package static
Summary:	Static libudffs library
Summary(pl.UTF-8):	Statyczna biblioteka libudffs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libudffs library.

%description static -l pl.UTF-8
Statyczna biblioteka libudffs.

%prep
%setup -q
%patch0 -p1

%{__sed} -i -e 's,/usr/sbin/pkt,%{_sbindir}/pkt,g' pktsetup/pktsetup.rules

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--enable-static%{!?with_static_libs:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libudffs.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/udftools

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/{HOWTO.udf,UDF-Specifications}
%attr(755,root,root) %{_bindir}/cdrwtool
%attr(755,root,root) %{_bindir}/udfinfo
%attr(755,root,root) %{_bindir}/wrudf
%attr(755,root,root) %{_sbindir}/mkfs.udf
%attr(755,root,root) %{_sbindir}/mkudffs
%attr(755,root,root) %{_sbindir}/pktcdvd-check
%attr(755,root,root) %{_sbindir}/pktsetup
%attr(755,root,root) %{_sbindir}/udflabel
%attr(755,root,root) %{_libdir}/libudffs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libudffs.so.2
/lib/udev/rules.d/80-pktsetup.rules
%{_mandir}/man1/cdrwtool.1*
%{_mandir}/man1/udfinfo.1*
%{_mandir}/man1/wrudf.1*
%{_mandir}/man8/mkudffs.8*
%{_mandir}/man8/pktsetup.8*
%{_mandir}/man8/mkfs.udf.8*
%{_mandir}/man8/udflabel.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libudffs.so
%{_includedir}/udffs

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libudffs.a
%endif
