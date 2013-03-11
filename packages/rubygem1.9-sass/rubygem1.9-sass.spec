#-------------------------------------------------------------------------------
# rubygem1.9-sass.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname sass


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-sass
Version:        3.2.7
Release:        1%{?dist}
Summary:        Extension of CSS3

Group:          Development/Languages
License:        MIT
URL:            http://sass-lang.com/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Sass makes CSS fun again. Sass is an extension of CSS3, adding nested rules,
variables, mixins, selector inheritance, and more. It's translated to
well-formatted, standard CSS using the command line tool or a web-framework
plugin.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Documentation for %{name}
Group:          Documentation

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

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
  rm -rf .yardopts Rakefile test vendor/fssm/spec
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} \
  %{ruby_sitelib}/bin/sass-convert \
  %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CONTRIBUTING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/REVISION
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION_DATE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION_NAME
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/gems/%{gemname}-%{version}/rails
%{ruby_sitelib}/gems/%{gemname}-%{version}/vendor
%{ruby_sitelib}/gems/%{gemname}-%{version}/init.rb
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/extra


#-------------------------------------------------------------------------------
%changelog
* Mon Mar 11 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.7-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.6-1%{?dist}
- New upstream version

* Sat Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.2.5-1%{?dist}
- New upstream version

* Tue Dec 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.2.4-1%{?dist}
- New upstream version

* Sun Nov 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.2.3-1%{?dist}
- New upstream version

* Sun Nov 4 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.2.2-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.2.1-1%{?dist}
- New upstream version

* Sun Jan 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 3.1.12-1%{?dist}
- Initial package creation
