#-------------------------------------------------------------------------------
# rubygem1.9-polyglot.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname polyglot


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-polyglot
Version:        0.3.3
Release:        1%{?dist}
Summary:        Custom language loaders for specified file extensions

Group:          Development/Languages
License:        MIT
URL:            http://polyglot.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Polyglot provides a registry of file types that can be loaded by calling its
improved version of ‘require’. Each file extension that can be handled by a
custom loader is registered by calling Polyglot.register(“ext”, <class>),
and then you can simply require “somefile”, which will find and load
“somefile.ext” using your custom loader.


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
  rm -rf Manifest.txt Rakefile script test website
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/History.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/License.txt
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.txt
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue Nov 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.3-1%{?dist}
- New upstream version

* Sat Aug 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.2-1%{?dist}
- New upstream version

* Sun Apr 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.1-1%{?dist}
- Initial package creation
