Summary:	UDF writing tools for CDRW recorders
Summary(pl):	Narzêdzia umo¿liwaj±ce zapisywanie na nagrywarkach w formacie UDF
Name:		udftools
Version:	1.0.0b2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://belnet.dl.sourceforge.net/sourceforge/linux-udf/%{name}-%{version}.tar.gz
Patch0:		%{name}-acam.patch
URL:		http://linux-udf.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package allows to use CDRW disks like a normal floppy disks.
The data can modified and deleted. Disks can be read in any UDF
compatibile system.

%description -l pl
Ten pakiet umo¿liwia nagrywanie na dyskach CDRW jak na normalnych
dyskietkach. Dane mo¿na usuwaæ i modyfikowaæ. Odczyt jest mo¿liwy na
systemach obs³uguj±cych system UDF.

%package devel
Summary:	udftools - library files
Summary(pl):	udftools - pliki biblioteki
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
udftools - library files.

%description devel -l pl
udftools - pliki biblioteki.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*
