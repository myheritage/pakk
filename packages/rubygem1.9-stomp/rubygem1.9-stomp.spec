#-------------------------------------------------------------------------------
# rubygem1.9-stomp.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname stomp


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-stomp
Version:        1.2.7
Release:        1%{?dist}
Summary:        Ruby client for the Stomp messaging protocol

Group:          Development/Languages
License:        ASL 2.0
URL:            https://github.com/stompgem/stomp
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Ruby client for the Stomp messaging protocol.


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
gem1.9 install --local \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf Rakefile spec test *.gemspec
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/catstomp %{buildroot}%{_bindir}/
ln -s %{ruby_sitelib}/bin/stompcat %{buildroot}%{_bindir}/
chmod 755 %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/bin/* 


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Sun Nov 4 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.7-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.6-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.5-1%{?dist}
- New upstream version

* Fri Jun 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.4-1%{?dist}
- Initial package creation
