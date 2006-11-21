Summary:	A console-based tool for handling MTA queues
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
requeued

Just for example, it may be useful to inspect a traffic jam at a given
time, to see what is falling into and unexpectedly crowding your
deferred queue.

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
