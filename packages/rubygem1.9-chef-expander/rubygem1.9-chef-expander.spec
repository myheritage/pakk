#-------------------------------------------------------------------------------
# rubygem1.9-chef-expander.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname chef-expander


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef-expander
Version:        10.16.2
Release:        1%{?dist}
Summary:        Replaces the former chef-solr-indexer daemon (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-expander.rb
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
Source5:        %{name}-chef-expander.8
Source6:        %{name}-chef-expanderctl.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       ruby1.9
Requires:       rubygem1.9-amqp <= 0.6.7
Requires:       rubygem1.9-bunny <= 0.6.0
Requires:       rubygem1.9-chef = %{version}
Requires:       rubygem1.9-em-http-request <= 0.2.15
Requires:       rubygem1.9-eventmachine <= 0.12.10
Requires:       rubygem1.9-highline <= 1.6.9
Requires:       rubygem1.9-fast_xs <= 0.7.3
Requires:       rubygem1.9-mixlib-log >= 1.2.0
Requires:       rubygem1.9-uuidtools >= 2.1.1
Requires:       rubygem1.9-yajl >= 1.0.0

%description
Chef Expander replaces the chef-solr-indexer daemon that was included with
Chef 0.8 and 0.9.

This package contains the rubygem code. If you need to run chef-server
as a daemon, please install the "chef-server-api" package.


#-----------------------------------------------------------------------------
# chef-expander package
#-----------------------------------------------------------------------------
%package -n chef-expander
Summary:        Manages search indexes of Chef node attributes using expander
Group:          System Environment/Daemons

Requires:       %{name} = %{version}

%description -n chef-expander
Chef Expander replaces the chef-solr-indexer daemon that was included with
Chef 0.8 and 0.9.


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
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} \
  %{ruby_sitelib}/bin/%{gemname}ctl \
  %{ruby_sitelib}/bin/%{gemname}-vnode \
   %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/chef
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/chef/expander.rb

install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{gemname}

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gemname}
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{gemname}

install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man8/%{gemname}.8
install -D -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man8/%{gemname}ctl.8
gzip %{buildroot}%{_mandir}/man8/*


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -n chef-expander
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{gemname}
fi

%preun -n chef-expander
if [ $1 = 0 ]; then
  /sbin/service %{gemname} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{gemname}
fi

%postun -n chef-expander
if [ $1 == 2 ]; then
  /sbin/service %{gemname} try-restart || :
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
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/conf
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/scripts
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-expander
%config(noreplace) %{_sysconfdir}/chef/expander.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/%{gemname}
%config(noreplace) %{_sysconfdir}/sysconfig/%{gemname}
%{_initrddir}/%{gemname}

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Oct 30 2012 Eric-Olivier Lamey <pakk@96b.it> - 10.16.2-1%{?dist}
- New upstream version

* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Tue Jan 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- Initial package creation
