#-----------------------------------------------------------------------------
# tsung.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           tsung
Version:        1.4.2
Release:        1%{?dist}
Summary:        Multi-protocol distributed load testing tool

Group:          Applications/System
License:        GPLv2
URL:            http://tsung.erlang-projects.org/
Source0:        http://%{name}.erlang-projects.org/dist/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  autoconf
BuildRequires:  erlang-kernel
BuildRequires:  erlang-sasl
BuildRequires:  erlang-snmp
BuildRequires:  erlang-ssl
BuildRequires:  erlang-xmerl

Requires:       erlang-kernel
Requires:       erlang-sasl
Requires:       erlang-snmp
Requires:       erlang-ssl
Requires:       erlang-xmerl

%description
It can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and
Jabber/XMPP servers. Tsung is a free software released under the GPLv2
license.
The purpose of Tsung is to simulate users in order to test the scalability
and performance of IP based client/server applications. You can use it to do
load and stress testing of your servers. Many protocols have been implemented
and tested, and it can be easily extended.
It can be distributed on several client machines and is able to simulate
hundreds of thousands of virtual users concurrently (or even millions if you
have enough hardware ...).


#-----------------------------------------------------------------------------
# -plotter package
#-----------------------------------------------------------------------------
%package plotter
Summary:        Plotter tool for tsung
Group:          Applications/System

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       python-matplotlib

%description plotter
Plotter tool for tsung.


#-----------------------------------------------------------------------------
# -stats package
#-----------------------------------------------------------------------------
%package stats
Summary:        Statistics tool for tsung
Group:          Applications/System

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       gnuplot
Requires:       perl(Template)

%description stats
Statistics tool for tsung.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build
%configure --docdir=%{_docdir}/%{name}-%{version}
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

mv %{buildroot}%{_libdir}/%{name}/bin/* %{buildroot}%{_bindir}
sed -i -e '1d' %{buildroot}%{_libdir}/%{name}/tsung_plotter/tsung.py

iconv -f ISO-8859-1 -t UTF-8 CONTRIBUTORS > CONTRIBUTORS.utf8 && \
  mv CONTRIBUTORS.utf8 CONTRIBUTORS


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc CHANGES CONTRIBUTORS COPYING README
%{_bindir}/%{name}
%{_bindir}/%{name}-recorder
%{_bindir}/log2tsung.pl
%dir %{_libdir}/%{name}
%{_libdir}/erlang/lib/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.dtd
%{_mandir}/man1/%{name}*

%files plotter
%defattr(-, root, root, -)
%{_bindir}/tsplot
%{_libdir}/%{name}/tsung_plotter
%{_datadir}/%{name}/tsung_plotter
%{_mandir}/man1/tsplot*

%files stats
%defattr(-, root, root, -)
%{_bindir}/tsung-rrd.pl
%{_bindir}/tsung_stats.pl
%{_datadir}/%{name}/templates


#-----------------------------------------------------------------------------
%changelog
* Mon Apr 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.2-1%{?dist}
- Initial package creation
