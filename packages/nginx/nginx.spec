#-----------------------------------------------------------------------------
# nginx.spec
#-----------------------------------------------------------------------------

%global basedir %{_localstatedir}/lib/%{name}
%global tmpdir  %{_localstatedir}/cache/%{name}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           nginx
Version:        1.2.6
Release:        1%{?dist}
Summary:        A HTTP and reverse proxy server

Group:          System Environment/Daemons
License:        BSD
URL:            http://nginx.org/
Source0:        http://nginx.org/download/%{name}-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel

Requires:       initscripts
Requires:       shadow-utils

%description
Nginx [engine x] is an HTTP(S) server, HTTP(S) reverse proxy and IMAP/POP3
proxy server written by Igor Sysoev.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build
export CFLAGS="%{optflags}"
./configure \
  --prefix=%{_prefix} \
  --conf-path=%{_sysconfdir}/%{name}/%{name}.conf \
  --error-log-path=%{_localstatedir}/log/%{name}/error.log \
  --pid-path=%{_localstatedir}/run/%{name}.pid \
  --lock-path=%{_localstatedir}/run/%{name}.lock \
  --user=%{name} \
  --group=%{name} \
  --with-file-aio \
  --with-ipv6 \
  \
  --http-client-body-temp-path=%{tmpdir}/client_body \
  --http-proxy-temp-path=%{tmpdir}/proxy \
  --http-fastcgi-temp-path=%{tmpdir}/fastcgi \
  --http-uwsgi-temp-path=%{tmpdir}/uwsgi \
  --http-scgi-temp-path=%{tmpdir}/scgi \
  --http-log-path=%{_localstatedir}/log/%{name}/access.log \
  \
  --with-http_addition_module \
  --with-http_degradation_module \
  --with-http_flv_module \
  --with-http_gzip_static_module \
  --with-http_mp4_module \
  --with-http_realip_module \
  --with-http_secure_link_module \
  --with-http_ssl_module \
  --with-http_stub_status_module \
  --with-http_sub_module

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

pushd %{buildroot}%{_sysconfdir}/%{name}
  rm -f fastcgi.conf *.default

  mkdir conf.d
  mv fastcgi_params conf.d/fastcgi.conf
  mv scgi_params conf.d/scgi.conf
  mv uwsgi_params conf.d/uwsgi.conf
  mv mime.types conf.d/

  mkdir charsets
  mv koi-utf koi-win win-utf charsets

  cp %{SOURCE1} %{name}.conf
popd

install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{basedir}/sites/default
mv %{buildroot}/usr/html/* %{buildroot}%{basedir}/sites/default
mkdir -p %{buildroot}%{tmpdir}/{client_body,proxy,fastcgi,uwsgi,scgi}

rm -rf %{buildroot}{_localstatedir}/run


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%pre
if [ $1 == 1 ]; then
  /usr/sbin/useradd -c %{name} -s /sbin/nologin -r -M -d %{basedir} %{name} \
    2> /dev/null || :
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


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc CHANGES CHANGES.ru LICENSE README
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*.conf
%dir %{_sysconfdir}/%{name}/conf.d
%config(noreplace) %{_sysconfdir}/%{name}/conf.d/*
%dir %{_sysconfdir}/%{name}/charsets
%config(noreplace) %{_sysconfdir}/%{name}/charsets/*
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_initrddir}/%{name}
%{_sbindir}/%{name}
%{_localstatedir}/log/%{name}
%{basedir}


#-----------------------------------------------------------------------------
%changelog
* Wed Dec 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.6-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.5-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.4-1%{?dist}
- New upstream version

* Wed Jul 4 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.2-1%{?dist}
- New upstream version

* Tue Jun 5 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.1-1%{?dist}
- New upstream version

* Mon Apr 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Tue Apr 17 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.15-1%{?dist}
- New upstream version

* Wed Apr 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.14-1%{?dist}
- New upstream version
- Resumed packaging at pakk

* Sun Sep 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.6-1%{?dist}
- New upstream version

* Mon Jul 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.5-1%{?dist}
- New upstream version

* Tue Apr 12 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.54-1%{?dist}
- New upstream version

* Tue Oct 19 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.8.53-1%{?dist}
- Initial package creation
