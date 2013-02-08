#-------------------------------------------------------------------------------
# rubygem1.9-net-ssh-multi.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname net-ssh-multi


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-net-ssh-multi
Version:        1.2.0
Release:        1%{?dist}
Summary:        Control multiple Net::SSH connections via a single interface

Group:          Development/Languages
License:        MIT
URL:            http://net-ssh.rubyforge.org/multi
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-net-ssh >= 2.6.5
Requires:       rubygem1.9-net-ssh-gateway >= 1.2.0

%description
Net::SSH::Multi is a library for controlling multiple Net::SSH connections
via a single interface. It exposes an API similar to that of
Net::SSH::Connection::Session and Net::SSH::Connection::Channel, making
it simpler to adapt programs designed for single connections to be used with
multiple connections.


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
  rm -rf *.gemspec *.pem Manifest Rakefile setup.rb test
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGES.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri Feb 8 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Thu Apr 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.0.1-1%{?dist}
- Initial package creation
