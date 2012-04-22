#-------------------------------------------------------------------------------
# rubygem1.9-systemu.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname systemu


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-systemu
Version:        2.5.0
Release:        1%{?dist}
Summary:        Univeral capture of stdout and stderr and handling of child process pid

Group:          Development/Languages
License:        Ruby
URL:            http://rubyforge.org/projects/codeforpeople/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Univeral capture of stdout and stderr and handling of child process pid for
windows, *nix, etc.


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
  rm -rf README.erb Rakefile systemu.gemspec test
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/samples


#-------------------------------------------------------------------------------
%changelog
* Sun Mar 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.5.0-1%{?dist}
- New upstream version

* Mon Dec 12 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.2-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.1-1%{?dist}
- New upstream version

* Wed Sep 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.4.0-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.3.0-1%{?dist}
- New upstream version

* Sat Apr 16 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.2.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- Initial package creation
