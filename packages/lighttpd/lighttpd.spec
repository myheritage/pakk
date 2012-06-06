#-----------------------------------------------------------------------------
# lighttpd.spec
#-----------------------------------------------------------------------------

%global basedir  %{_localstatedir}/lib/%{name}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           lighttpd
Version:        1.4.31
Release:        1%{?dist}
Summary:        Secure, fast, compliant and flexible web server

Group:          System Environment/Daemons
License:        BSD
URL:            http://www.lighttpd.net/
Source0:        http://download.lighttpd.net/%{name}/releases-1.4.x/%{name}-%{version}.tar.bz2
Source1:        %{name}.conf
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  bzip2-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel

Requires:       initscripts
Requires:       shadow-utils

%description
Security, speed, compliance, and flexibility -- all of these describe lighttpd
(pron. lighty) which is rapidly redefining efficiency of a webserver; as it is
designed and optimized for high performance environments. With a small memory
footprint compared to other web-servers, effective management of the cpu-load,
and advanced feature set (FastCGI, SCGI, Auth, Output-Compression,
URL-Rewriting and many more) lighttpd is the perfect solution for every
server that is suffering load problems.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build
%configure \
  --libdir=%{_libdir}/%{name}

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/conf.d
cp doc/config/modules.conf %{buildroot}%{_sysconfdir}/%{name}/modules.conf
cp doc/config/conf.d/*.conf %{buildroot}%{_sysconfdir}/%{name}/conf.d

install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{basedir}/sites/default
mkdir -p %{buildroot}%{basedir}/sockets

mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre
if [ $1 == 1 ]; then
  /usr/sbin/useradd -c "%{name} user" -s /bin/false -r -M -d %{basedir} %{name} 2> /dev/null || :
fi

%post
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{name}
fi

%preun
if [ $1 = 0 ]; then
  /sbin/service %{name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 == 2 ]; then
  /sbin/service %{name} upgrade || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING NEWS README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_initrddir}/%{name}
%{_sbindir}/%{name}
%{_sbindir}/%{name}-angel
%{_libdir}/%{name}
%{_mandir}/man8/%{name}.8.gz
%dir %attr(0750, lighttpd, lighttpd) %{_localstatedir}/cache/%{name}
%dir %attr(0750, lighttpd, lighttpd) %{_localstatedir}/log/%{name}
%dir %{basedir}
%{basedir}/sites
%dir %attr(0750, lighttpd, lighttpd) %{basedir}/sockets


#-----------------------------------------------------------------------------
%changelog
* Fri Jun 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.31-1%{?dist}
- New upstream version

* Mon Mar 26 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.4.30-1%{?dist}
- New upstream version

* Sun Sep 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.29-1%{?dist}
- New upstream version

* Tue Oct 19 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.4.28-1%{?dist}
- Initial package creation
