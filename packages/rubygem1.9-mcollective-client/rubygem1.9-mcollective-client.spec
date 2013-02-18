#-------------------------------------------------------------------------------
# rubygem1.9-mcollective-client.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global upstream_name mcollective
%global gemname mcollective-client


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-mcollective-client
Version:        2.2.3
Release:        1%{?dist}
Summary:        Client libraries for The Marionette Collective

Group:          Development/Languages
License:        ASL 2.0
URL:            https://docs.puppetlabs.com/mcollective/
Source0:        http://downloads.puppetlabs.com/%{upstream_name}/%{upstream_name}-%{version}.tgz
Source1:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source2:        opscodeohai_facts.rb
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-json
Requires:       rubygem1.9-stomp
Requires:       rubygem1.9-systemu

%description
Client libraries for The Marionette Collective.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

Requires:       %{name} = %{version}

%description doc
Documentation for %{name} in rdoc and ri format.


#-----------------------------------------------------------------------------
# mcollective-client package
#-----------------------------------------------------------------------------
%package -n mcollective-client
Summary:        Client tools for the mcollective Application Server
Group:          Applications/System

Requires:       %{name} = %{version}

%description -n mcollective-client
Client tools for the mcollective Application Server.


#-----------------------------------------------------------------------------
# mcollective-server package
#-----------------------------------------------------------------------------
%package -n mcollective-server
Summary:        Application Server for hosting Ruby code
Group:          System Environment/Daemons

Requires:       %{name} = %{version}

%description -n mcollective-server
Application Server for hosting Ruby code.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{upstream_name}-%{version}


#-------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE1}
rm -rf %{buildroot}%{ruby_sitelib}/cache

cp lib/%{upstream_name}/runner.rb \
  %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/lib/%{upstream_name}/
pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  sed -i -e 's|@DEVELOPMENT_VERSION@|%{version}|g' lib/mcollective.rb
  rm -rf spec
popd

mkdir -p %{buildroot}%{_sysconfdir}/%{upstream_name}/{plugin.d,ssl,ssl/clients}
for file in client.cfg facts.yaml server.cfg; do
  install -p -D -m 0640 etc/${file}.dist %{buildroot}%{_sysconfdir}/%{upstream_name}/${file}
done
for file in rpc-help.erb; do
  install -p -m 0644 etc/${file} %{buildroot}%{_sysconfdir}/%{upstream_name}/${file}
done
install -p -D -m 0755 ext/redhat/%{upstream_name}.init \
  %{buildroot}%{_sysconfdir}/init.d/%{upstream_name}

install -p -D -m 0755 bin/mco %{buildroot}%{_bindir}/mco
install -p -D -m 0755 bin/mc-call-agent %{buildroot}%{_sbindir}/mc-call-agent
install -p -D -m 0755 bin/mcollectived %{buildroot}%{_sbindir}/mcollectived
sed -i -e 's|^#!/usr/bin/env ruby|#!/usr/bin/env ruby1.9|g' \
  %{buildroot}%{_bindir}/* %{buildroot}%{_sbindir}/*

mkdir -p  %{buildroot}%{_libexecdir}/%{upstream_name}/
cp -R plugins/* %{buildroot}%{_libexecdir}/%{upstream_name}/
install -p -D -m 0644 %{SOURCE2} \
  %{buildroot}%{_libexecdir}/%{upstream_name}/%{upstream_name}/facts/opscodeohai_facts.rb


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -n mcollective-server
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{upstream_name}
fi

%preun -n mcollective-server
if [ $1 = 0 ]; then
  /sbin/service %{upstream_name} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{upstream_name}
fi

%postun -n mcollective-server
if [ $1 == 2 ]; then
  /sbin/service %{upstream_name} upgrade || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc COPYING
%dir %{_sysconfdir}/%{upstream_name}
%dir %{_sysconfdir}/%{upstream_name}/ssl
%config(noreplace) %{_sysconfdir}/%{upstream_name}/*.erb
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec
%{_libexecdir}/%{upstream_name}
%exclude %{_libexecdir}/%{upstream_name}/%{upstream_name}/application
%exclude %{_libexecdir}/%{upstream_name}/%{upstream_name}/pluginpackager

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}

%files -n mcollective-client
%doc COPYING
%config(noreplace) %{_sysconfdir}/%{upstream_name}/client.cfg
%{_sbindir}/mc-call-agent
%{_bindir}/*
%{_libexecdir}/%{upstream_name}/%{upstream_name}/application
%{_libexecdir}/%{upstream_name}/%{upstream_name}/pluginpackager

%files -n mcollective-server
%doc COPYING
%config(noreplace) %{_sysconfdir}/%{upstream_name}/facts.yaml
%config(noreplace) %{_sysconfdir}/%{upstream_name}/server.cfg
%dir %{_sysconfdir}/%{upstream_name}/plugin.d
%dir %{_sysconfdir}/%{upstream_name}/ssl/clients
%{_sysconfdir}/init.d/%{upstream_name}
%{_sbindir}/%{upstream_name}d


#-------------------------------------------------------------------------------
%changelog
* Mon Feb 18 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.2.3-1%{?dist}
- New upstream version

* Sat Jan 19 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.2.2-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.1-1%{?dist}
- New upstream version

* Sun Sep 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Fri Jun 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0-1%{?dist}
- Initial package creation
