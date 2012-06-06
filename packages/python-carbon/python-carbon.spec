#-----------------------------------------------------------------------------
# python-carbon.spec
# dists: el6
#-----------------------------------------------------------------------------

%global upstream_name carbon
%global datadir       %{_localstatedir}/lib/%{upstream_name}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           python-%{upstream_name}
Version:        0.9.10
Release:        1%{?dist}
Summary:        Backend data caching and persistence daemon for Graphite

Group:          System Environment/Daemons
License:        ASL 2.0
URL:            https://launchpad.net/graphite
Source0:        http://launchpad.net/graphite/0.9/%{version}/+download/%{upstream_name}-%{version}.tar.gz
Source1:        %{upstream_name}-cache.init
Source2:        %{upstream_name}-relay.init
Source3:        %{upstream_name}-aggregator.init
Source4:        %{upstream_name}-cache.sysconfig
Source5:        %{upstream_name}-relay.sysconfig
Source6:        %{upstream_name}-aggregator.sysconfig
Patch0:         %{upstream_name}-paths.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python

Requires:       initscripts
Requires:       python-twisted-core >= 8.0
Requires:       python-whisper
Requires:       shadow-utils

%description
Backend data caching and persistence daemon for Graphite.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{upstream_name}-%{version}
%patch0 -p1


#-----------------------------------------------------------------------------
%build
rm -f setup.cfg
%{__python} setup.py build


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

chmod 755 %{buildroot}%{python_sitelib}/%{upstream_name}/{amqp_listener,amqp_publisher,service}.py

mkdir -p %{buildroot}%{_sysconfdir}/%{upstream_name}
pushd %{buildroot}%{_prefix}/conf
  for file in *; do
    mv ${file} %{buildroot}%{_sysconfdir}/%{upstream_name}/${file/.example/}
  done
popd
rm -rf %{buildroot}%{_prefix}/conf 

install -p -D -m 0755 %{SOURCE1} %{buildroot}%{_initrddir}/%{upstream_name}-cache
install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{upstream_name}-relay
install -p -D -m 0755 %{SOURCE3} %{buildroot}%{_initrddir}/%{upstream_name}-aggregator
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/%{upstream_name}-cache
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/sysconfig/%{upstream_name}-relay
install -p -D -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/sysconfig/%{upstream_name}-aggregator

mkdir -p %{buildroot}%{datadir}
mkdir -p %{buildroot}%{_localstatedir}/log/%{upstream_name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%pre
if [ $1 == 1 ]; then
  /usr/sbin/useradd -c %{upstream_name} -s /bin/false -r -M -d %{datadir} \
    %{upstream_name} 2> /dev/null || :
fi

%post
if [ $1 == 1 ]; then
  for service in cache relay aggregator; do
    /sbin/chkconfig --add %{upstream_name}-${service}
  done
fi

%preun
if [ $1 = 0 ]; then
  for service in cache relay aggregator; do
    /sbin/service %{upstream_name}-${service} stop > /dev/null 2>&1
    /sbin/chkconfig --del %{upstream_name}-${service}
  done
fi

%postun
if [ $1 == 2 ]; then
  for service in cache relay aggregator; do
    /sbin/service %{upstream_name}-${service} condrestart || :
  done
fi


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc LICENSE
%dir %{_sysconfdir}/%{upstream_name}
%config(noreplace) %{_sysconfdir}/%{upstream_name}/*.conf
%config(noreplace) %{_sysconfdir}/sysconfig/%{upstream_name}*
%{_initrddir}/%{upstream_name}*
%{_bindir}/*
%{python_sitelib}/*
%dir %attr(-, %{upstream_name}, %{upstream_name}) %{datadir}
%dir %attr(-, %{upstream_name}, %{upstream_name}) %{_localstatedir}/log/%{upstream_name}


#-----------------------------------------------------------------------------
%changelog
* Sat Jun 2 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.10-1%{?dist}
- New upstream version

* Sun Apr 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.9-1%{?dist}
- Initial package creation
