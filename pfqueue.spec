Summary:	A console-based tool for handling MTA queues
Summary(pl):	Tekstowe narzêdzie do obs³ugi kolejek MTA
Name:		pfqueue
Version:	0.5.3
Release:	0.2
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/pfqueue/%{name}-%{version}.tar.gz
# Source0-md5:	7700198871f91cf28e0164f8e776dd55
URL:		http://pfqueue.sourceforge.net/
BuildRequires:	ncurses-devel
#Requires:	postfix or exim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pfqueue is an effort to give postqueue/mailq/postsuper/exim4 a console
(ncurses) interface: it won't add any particular functionality to
those provided with MTAs themselves, but will hopefully make them
easier to use.

It's a real-time queue scanner, that shows per-queue lists of existing
messages; the messages can be shown, deleted, put on hold, released or
requeued.

Just for example, it may be useful to inspect a traffic jam at a given
time, to see what is falling into and unexpectedly crowding your
deferred queue.

%description -l pl
pfqueue to próba dostarczenia tekstowego (opartego na ncurses)
interfejsu do poleceñ postqueue/mailq/postsuper/exim4; nie dodaje
¿adnych konkretnych funkcji do dostarczanych przez same MTA, jedynie
czyni je ³atwiejszymi w u¿yciu.

Jest to program przeszukuj±cy kolejki w czasie rzeczywistym,
pokazuj±cy listê istniej±cych wiadomo¶ci dla ka¿dej kolejki;
wiadomo¶ci mog± byæ wy¶wietlone, usuniête, wstrzymane, wypuszczone lub
ponownie skolejkowane.

Program mo¿e byæ przydatny na przyk³ad do ¶ledzenia zatkania ruchu o
danym czasie, aby zobaczyæ, co wpad³o i nieoczekiwanie zapcha³o
kolejkê.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
export CFLAGS
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libpfq*.so.*.*.*
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
