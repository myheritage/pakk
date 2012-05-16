#-------------------------------------------------------------------------------
# rubygem1.9-chef-server.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname chef-server


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-chef-server
Version:        0.10.10
Release:        1%{?dist}
Summary:        Meta package to install all server components for Chef (rubygem)

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.opscode.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}-chef-create-amqp_passwd
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       chef-common = %{version}
Requires:       ruby1.9
Requires:       rubygem1.9-chef-expander = %{version}
Requires:       rubygem1.9-chef-server-api = %{version}
Requires:       rubygem1.9-chef-server-webui = %{version}
Requires:       rubygem1.9-chef-solr = %{version}

%description
A meta-gem to install all server components of the Chef configuration
management system.


#-----------------------------------------------------------------------------
# chef-server package
#-----------------------------------------------------------------------------
%package -n chef-server
Summary:        Meta package to install all server components for Chef
Group:          System Environment/Daemons

Requires:       %{name} = %{version}
Requires:       chef-server-api = %{version}
Requires:       chef-server-webui = %{version}
Requires:       chef-solr = %{version}

%description -n chef-server
A meta-gem to install all server components of the Chef configuration
management system.


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
  rm -rf Rakefile
popd

install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/chef-create-amqp_passwd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n chef-server
%{_sbindir}/*

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
