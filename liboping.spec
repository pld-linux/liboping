# TODO:
# - package perl modules
Summary:	Liboping library
Name:		liboping
Version:	1.1.2
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://verplant.org/liboping/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a120dcd0d808e9a59e2729e7cffcb067
URL:		http://verplant.org/liboping/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboping is a C library to generate ICMP echo requests, better known as
"ping packets". It is intended for use in network monitoring applications
or applications that would otherwise need to fork ping(1) frequently.

liboping was inspired by ping, libping (homepage vanished) and fping:
It differs from these existing solutions in that it can `ping' multiple
hosts in parallel using IPv4 or IPv6 transparently. Other design principles
were an object oriented interface, simplicity and extensibility: Is simple
because there are only a few interface functions and no external
dependencies. It's extensible since all (internal) data is kept in "opaque
data types", so the storage may change or be extended without applications
noticing it.

%package -n oping
Summary:	oping ICMP query tool
Group:		Applications/Networking

%description -n oping
Sample application, which demonstrates the liboping's abilities. It is like
ping, ping6, and fping rolled into one.

%package devel
Summary:	Header files for liboping library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboping
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for liboping library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboping.

%package static
Summary:	Static liboping library
Summary(pl.UTF-8):	Statyczna biblioteka liboping
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboping library.

%description static -l pl.UTF-8
Statyczna biblioteka liboping.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files -n oping
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_bindir}/*
%{_mandir}/man8/*.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/oping.h
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
