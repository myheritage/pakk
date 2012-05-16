#-------------------------------------------------------------------------------
# rubygem1.9-chef-server-api.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname chef-server-api


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef-server-api
Version:        0.10.10
Release:        1%{?dist}
Summary:        Merb slice providing REST API for Chef client access (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-server.rb
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
Source5:        %{name}.man
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       couchdb >= 0.9.1
Requires:       rabbitmq-server
Requires:       ruby1.9
Requires:       rubygem1.9-dep_selector >= 0.0.3
Requires:       rubygem1.9-merb-core >= 1.1.0
Requires:       rubygem1.9-merb-assets >= 1.1.0
Requires:       rubygem1.9-merb-helpers >= 1.1.0
Requires:       rubygem1.9-merb-param-protection >= 1.1.0
Requires:       rubygem1.9-mixlib-authentication >= 1.1.3
Requires:       rubygem1.9-thin
Requires:       rubygem1.9-uuidtools >= 2.1.1

%description
The Chef Server API provides the API for the Chef Server so
clients can connect and is started with the chef-server program.

This package contains the rubygem code. If you need to run chef-server
as a daemon, please install the "chef-server-api" package.


#-----------------------------------------------------------------------------
# chef-server-api package
#-----------------------------------------------------------------------------
%package -n chef-server-api
Summary:        Merb slice providing REST API for Chef client access
Group:          System Environment/Daemons

Requires:       %{name} = %{version}

%description -n chef-server-api
The Chef Server API provides the API for the Chef Server so
clients can connect and is started with the chef-server program.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

Requires:       %{name} = %{version}

%description doc
Documentation for %{name} in rdoc and ri format.


#-------------------------------------------------------------------------------
%install
rm -rf %{buildroot}
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf Rakefile spec
  echo 'File.umask Chef::Config[:umask]' >> config/init.rb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/chef-server \
   %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/chef
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/chef/server.rb

install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/chef-server

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/chef-server
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/chef-server

install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man8/chef-server.8 \
  && gzip %{buildroot}%{_mandir}/man8/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -n chef-server-api
if [ $1 == 1 ]; then
  /sbin/chkconfig --add chef-server
fi

%preun -n chef-server-api
if [ $1 = 0 ]; then
  /sbin/service chef-server stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del chef-server
fi

%postun -n chef-server-api
if [ $1 == 2 ]; then
  /sbin/service chef-server try-restart || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%{_bindir}/*
%{_mandir}/man8/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/app
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/config
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/public
%{ruby_sitelib}/gems/%{gemname}-%{version}/*.ru
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-server-api
%config(noreplace) %{_sysconfdir}/chef/server.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/chef-server
%config(noreplace) %{_sysconfdir}/sysconfig/chef-server
%{_initrddir}/chef-server

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.16-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.14-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Feb 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-1%{?dist}
- Initial package creation
