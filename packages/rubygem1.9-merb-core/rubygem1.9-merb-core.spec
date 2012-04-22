#-------------------------------------------------------------------------------
# rubygem1.9-merb-core.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname merb-core


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-merb-core
Version:        1.1.3
Release:        3%{?dist}
Summary:        Merb core

Group:          Development/Languages
License:        MIT
URL:            http://merbivore.com/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-bundler
Requires:       rubygem1.9-erubis >= 2.6.2
Requires:       rubygem1.9-extlib >= 0.9.13
Requires:       rubygem1.9-mime-types >= 1.16
Requires:       rubygem1.9-rack

%description
A new branch of Merb (sometimes referred to as merb-next) which aims to
provide a stable, stripped down API for the Merb 1.0 release.


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
  rm -rf Rakefile TODO spec spec10

  # The default umask is a bit too wide. And chef doesn't set one by default
  sed -i -e 's|File.umask 0000|File.umask 0022|g' lib/merb-core/server.rb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/merb %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CONTRIBUTORS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/PUBLIC_CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.3-3%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Feb 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.3-2%{?dist}
- Changed the default umask set upon server start

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.1.3-1%{?dist}
- Initial package creation
