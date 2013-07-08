#-------------------------------------------------------------------------------
# rubygem1.9-bcrypt.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname bcrypt-ruby


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-bcrypt
Version:        3.1.1
Release:        1%{?dist}
Summary:        Provides a simple, humane wrapper for safely handling passwords

Group:          Development/Languages
License:        MIT
URL:            http://bcrypt-ruby.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
An easy way to keep your users' passwords secure.


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
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem1.9 install --local \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .??* Gemfile* Rakefile ext bcrypt-ruby.gemspec spec
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri Jul 12 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.1.1-1%{?dist}
- New upstream version

* Mon Jul 8 2013 Eric-Olivier Lamey <pakk@96b.it> - 3.1.0-1%{?dist}
- New upstream version

* Wed Sep 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.0.1-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.0.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 2.1.4-1%{?dist}
- New upstream version

* Tue Dec 21 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.1.3-1%{?dist}
- New upstream version

* Tue Nov 2 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.1.2-1%{?dist}
- Initial package creation
