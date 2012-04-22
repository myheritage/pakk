#-------------------------------------------------------------------------------
# rubygem1.9-hpricot.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname hpricot


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-hpricot
Version:        0.8.6
Release:        1%{?dist}
Summary:        Swift, liberal HTML parser with a fantastic library

Group:          Development/Languages
License:        MIT
URL:            http://wiki.github.com/hpricot/hpricot
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Hpricot is a fast, flexible HTML parser written in C. It's designed to be
very accommodating (like Tanaka Akira's HTree) and to have a very helpful
library (like some JavaScript libs -- JQuery, Prototype -- give you.) 
The XPath and CSS parser, in fact, is based on John Resig's JQuery.


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
  rm -rf Rakefile test ext
  strip lib/*.so

  # let's make rpmlint happy
  sed -i -e '1d' lib/hpricot/xchar.rb lib/hpricot/blankslate.rb
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
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/extras


#-------------------------------------------------------------------------------
%changelog
* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.8.6-1%{?dist}
- New upstream version

* Thu Nov 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.5-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Mar 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.4-1%{?dist}
- New upstream version

* Sat Feb 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.3-1%{?dist}
- Initial package creation
