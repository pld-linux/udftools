Summary:	UDF writing tools for CDRW recorders
Summary(pl.UTF-8):	Narzędzia umożliwiające zapisywanie na płytach CDRW w formacie UDF
Name:		udftools
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	https://github.com/pali/udftools/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	f5cbb7dffbb33778a90c08e76693651e
URL:		http://linux-udf.sourceforge.net/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	readline-devel
Obsoletes:	udftools-devel
Obsoletes:	udftools-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin
%define		specflags	-Wall

%description
This package allows to use CDRW disks like a normal floppy disks. The
data can modified and deleted. Disks can be read in any UDF
compatibile system.

%description -l pl.UTF-8
Ten pakiet umożliwia nagrywanie na dyskach CDRW jak na normalnych
dyskietkach. Dane można usuwać i modyfikować. Odczyt jest możliwy na
systemach obsługujących system plików UDF.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-shared \
	--enable-static=%{?with_static_libs:yes}%{!?with_static_libs:no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/cdrwtool
%attr(755,root,root) %{_sbindir}/mkudffs
%attr(755,root,root) %{_sbindir}/pktsetup
%attr(755,root,root) %{_sbindir}/wrudf
%attr(755,root,root) %{_sbindir}/mkfs.udf
%{_mandir}/man1/cdrwtool.1*
%{_mandir}/man1/wrudf.1*
%{_mandir}/man8/mkudffs.8*
%{_mandir}/man8/pktsetup.8*
%{_mandir}/man8/mkfs.udf.8*
