#-----------------------------------------------------------------------------
# apache24.spec
# dists: el6
#-----------------------------------------------------------------------------

%global upstream_name httpd


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           apache24
Version:        2.4.1
Release:        1%{?dist}
Summary:        Apache web server

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            http://httpd.apache.org
Source0:        http://apache.multidist.com/httpd/httpd-%{version}.tar.bz2
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
Source5:        %{name}cacheclean.init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 

BuildRequires:  apr-devel >= 1.4.0
BuildRequires:  apr-util-devel >= 1.4.0
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel

Requires:       initscripts
Requires:       shadow-utils

%description
The Apache HTTP Server Project is a collaborative software development effort
aimed at creating a robust, commercial-grade, featureful, and
freely-available source code implementation of an HTTP (Web) server.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Apache development files
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Header files and libraries for building an extension library for the
Apache web server.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc 
Summary:        Apache documentation
Group:          Documentation

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

%description doc 
Documentation for the Apache web server.


#-----------------------------------------------------------------------------
# -mod_lua package
#-----------------------------------------------------------------------------
%package mod_lua
Summary:        Lua module for the Apache HTTP Server
Group:          System Environment/Daemons

BuildRequires:  lua-devel

Requires:       %{name} = %{version}

%description mod_lua
Lua module for the Apache HTTP Server.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{upstream_name}-%{version}


#-----------------------------------------------------------------------------
%build
cat << EOF >> config.layout
<Layout pakk>
  prefix:          %{_prefix}
  exec_prefix:     %{_prefix}
  bindir:          %{_bindir}
  sbindir:         %{_sbindir}
  libdir:          %{_libdir}
  libexecdir:      %{_libdir}/%{name}/modules
  mandir:          %{_mandir}
  sysconfdir:      %{_sysconfdir}/%{name}
  installbuilddir: %{_libdir}/%{name}/build
  includedir:      %{_includedir}/%{name}
  localstatedir:   %{_localstatedir}
  datadir:         %{_localstatedir}/lib/%{name}
  errordir:        %{_localstatedir}/lib/%{name}/error
  iconsdir:        %{_localstatedir}/lib/%{name}/icons
  htdocsdir:       %{_localstatedir}/lib/%{name}/default
  manualdir:       %{_localstatedir}/lib/%{name}/manual
  cgidir:          %{_localstatedir}/lib/%{name}/cgi-bin
  runtimedir:      %{_localstatedir}/run
  logfiledir:      %{_localstatedir}/log/%{name}
  proxycachedir:   %{_localstatedir}/cache/%{name}/cache-root
</Layout>
EOF
export CFLAGS="%{optflags}"
./configure \
  --enable-layout=pakk \
  --enable-pie \
  --enable-ssl \
  --enable-unixd \
  --enable-mods-shared=reallyall \
  --enable-mpms-shared=all

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

pushd %{buildroot}%{_sysconfdir}/%{name}
  rm -rf original
  mv extra modules
  sed -i -e 's|/extra/|/modules/|g' httpd.conf
popd

install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{name}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

install -p -D -m 0755 %{SOURCE5} %{buildroot}%{_initrddir}/%{name}cacheclean

rm -f %{buildroot}%{_sbindir}/envvars*

rmdir %{buildroot}%{_localstatedir}/run
gzip %{buildroot}%{_mandir}/man{1,8}/*

pushd %{buildroot}%{_localstatedir}/lib/%{name}/manual
  find . \( -name \*.xml -o -name \*.xml.* -o -name \*.ent \
         -o -name \*.xsl -o -name \*.dtd \) -print0 | xargs -0 rm -f
  for f in $(find . -name \*.html -type f); do
    if [ -f ${f}.en ]; then
      cp ${f}.en ${f}
      rm ${f}.*
    fi
  done
  rm -f rewrite/rewrite_guide.html.fr rewrite/rewrite_guide_advanced.html.fr
popd


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre
getent group %{name} > /dev/null || \
  /usr/sbin/groupadd -r %{name} 2> /dev/null || :
getent passwd %{name} > /dev/null || \
  /usr/sbin/useradd -c "%{name}" -s /bin/false -r -M -g %{name} \
    -d %{_localstatedir}/lib/%{name} %{name} 2> /dev/null || :

%post
/sbin/chkconfig --add %{name}

%preun
if [ $1 = 0 ]; then
  /sbin/service %{name} stop >/dev/null 2>&1
  /sbin/chkconfig --del %{name}
fi

%postun
if [ $1 -ge 1 ]; then
  /sbin/service %{name} condrestart > /dev/null 2>&1 || :
fi


%files
%defattr(-, root, root, -)
%doc CHANGES INSTALL LICENSE README
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_initrddir}/*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/httpd.conf
%config(noreplace) %{_sysconfdir}/%{name}/magic
%config(noreplace) %{_sysconfdir}/%{name}/mime.types
%dir %{_sysconfdir}/%{name}/modules
%config(noreplace) %{_sysconfdir}/%{name}/modules/*
%{_bindir}/*
%{_sbindir}/*
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/modules/mod_lua.so
%{_localstatedir}/lib/%{name}
%exclude %{_localstatedir}/lib/%{name}/manual
%dir %{_localstatedir}/log/%{name}
%{_mandir}/man1/*.gz
%{_mandir}/man8/*.gz

%files devel
%{_libdir}/%{name}/build
%{_includedir}/%{name}

%files doc
%{_localstatedir}/lib/%{name}/manual

%files mod_lua
%{_libdir}/%{name}/modules/mod_lua.so


#-----------------------------------------------------------------------------
%changelog
* Wed Apr 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.4.1-1%{?dist}
- Initial package creation
