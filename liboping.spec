Summary:	Liboping library to generate ICMP echo requests
Summary(pl.UTF-8):	Biblioteka liboping do generowania żądań ICMP echo
Name:		liboping
Version:	1.10.0
Release:	9
License:	LGPL v2.1+ (library), GPL v2+ (tool, perl binding)
Group:		Libraries
Source0:	http://noping.cc/files/%{name}-%{version}.tar.bz2
# Source0-md5:	54e0f5a1aaf9eabf3f412d2fdc9c6831
Patch0:		gcc8.patch
Patch1:		format-security.patch
URL:		http://noping.cc/
BuildRequires:	autoconf >= 2.65
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	ncurses-devel
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.6
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
liboping is a C library to generate ICMP echo requests, better known
as "ping packets". It is intended for use in network monitoring
applications or applications that would otherwise need to fork ping(1)
frequently.

liboping was inspired by ping, libping (homepage vanished) and fping:
It differs from these existing solutions in that it can `ping'
multiple hosts in parallel using IPv4 or IPv6 transparently. Other
design principles were an object oriented interface, simplicity and
extensibility: Is simple because there are only a few interface
functions and no external dependencies. It's extensible since all
(internal) data is kept in "opaque data types", so the storage may
change or be extended without applications noticing it.

%description -l pl.UTF-8
liboping to biblioteka C służąca do generowania żądań ICMP echo,
lepiej znanych jako "pakiety ping". Jej celem jest wykorzystanie w
aplikacjach do monitorowania sieci lub programach wymagających
regularnego wywoływania programu ping(1).

liboping została zainspirowana pakietami ping, libping (strona
domowa zniknęła) oraz fping - różni się od istniejących rozwiązań tym,
że potrafi "pingować" wiele hostów równolegle przy użyciu IPv4 lub
IPv6 w sposób przezroczysty. Inne reguły zastosowane przy
projektowaniu to interfejs zorientowany obiektowo, prostota i
rozszerzalność: biblioteka jest prosta, bo interfejs składa się tylko
z kilku funkcji i nie ma zewnętrznych zależności; jest rozszerzalna,
ponieważ wszystkie (wewnętrzne) dane są trzymane w niejawnych typach
danych, więc sposób przechowywania może być zmieniony lub rozszerzony
bez potrzeby uwzględniania tego w aplikacjach.

%package devel
Summary:	Header files for liboping library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liboping
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for liboping library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liboping.

%package static
Summary:	Static liboping library
Summary(pl.UTF-8):	Statyczna biblioteka liboping
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liboping library.

%description static -l pl.UTF-8
Statyczna biblioteka liboping.

%package -n perl-Net-Oping
Summary:	Net::Oping - ICMP latency measurement module using the oping library
Summary(pl.UTF-8):	Net::Oping - moduł mierzący opóźnienia ICMP przy użyciu biblioteki oping
License:	GPL v2+
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-Net-Oping
This Perl module is a high-level interface to the oping library. Its
purpose it to send "ICMP ECHO_REQUEST" packets (also known as "ping")
to a host and measure the time that elapses until the reception of an
"ICMP ECHO_REPLY" packet (also known as "pong"). If no such packet is
received after a certain timeout the host is considered to be
unreachable.

%description -n perl-Net-Oping -l pl.UTF-8
Ten moduł Perla to wysokopoziomowy interfejs do biblioteki oping. Jego
celem jest wysyłanie pakietów ICMP ECHO_REQUEST (znanych także jako
"ping") do hosta i mierzenie czasu mijającego do odebrania pakietu
ICMP ECHO_REPLY (znanego także jako "pong"). Jeśli taki pakiet nie
zostanie odebrany przez pewien określony limit czasu, host uważa się
za niedostępny.

%package -n oping
Summary:	oping ICMP query tool
Summary(pl.UTF-8):	Narzędzie oping do zapytań ICMP
License:	GPL v2+
Group:		Applications/Networking
Requires:	%{name} = %{version}-%{release}

%description -n oping
Sample application, which demonstrates the liboping's abilities. It is
like ping, ping6, and fping rolled into one.

%description -n oping -l pl.UTF-8
Przykładowa aplikacja, demonstrująca możliwości biblioteki liboping.
Jest to coś w rodzaju programów ping, ping6 i fping połączonych w
jeden.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-perl-bindings="INSTALLDIRS=vendor"
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
%attr(755,root,root) %{_bindir}/noping
%attr(755,root,root) %{_libdir}/liboping.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboping.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboping.so
%{_libdir}/liboping.la
%{_includedir}/oping.h
%{_pkgconfigdir}/liboping.pc
%{_mandir}/man3/liboping.3*
%{_mandir}/man3/ping_*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/liboping.a

%files -n perl-Net-Oping
%defattr(644,root,root,755)
%doc bindings/perl/Changes
%{perl_vendorarch}/Net/Oping.pm
%dir %{perl_vendorarch}/auto/Net/Oping
%attr(755,root,root) %{perl_vendorarch}/auto/Net/Oping/Oping.so
%{_mandir}/man3/Net::Oping.3pm*

%files -n oping
%defattr(644,root,root,755)
%attr(4754,root,adm) %{_bindir}/oping
%{_mandir}/man8/oping.8*
