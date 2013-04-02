#-------------------------------------------------------------------------------
# rubygem1.9-mime-types.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname mime-types


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-mime-types
Version:        1.22
Release:        1%{?dist}
Summary:        Ruby implementation of a MIME Types information library

Group:          Development/Languages
License:        Ruby or Perl or GPL
URL:            http://rubyforge.org/projects/mime-types/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Manages a MIME Content-Type database that will return the Content-Type for a
given filename.


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
  rm -rf .??* Install.txt Gemfile Manifest.txt Rakefile mime-types.gemspec setup.rb test
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/History.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Licence.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/Contributing.rdoc
%{ruby_sitelib}/gems/%{gemname}-%{version}/docs


#-------------------------------------------------------------------------------
%changelog
* Tue Apr 2 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.22-1%{?dist}
- New upstream version

* Tue Feb 12 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.21-1%{?dist}
- New upstream version

* Tue Feb 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.20.1-1%{?dist}
- New upstream version

* Sat Jun 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.19-1%{?dist}
- New upstream version

* Wed Mar 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.18-1%{?dist}
- New upstream version

* Sun Oct 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.17.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.16-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Mon Jan 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.16-1%{?dist}
- Initial package creation
