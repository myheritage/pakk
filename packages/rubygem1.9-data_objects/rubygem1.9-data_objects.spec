#-------------------------------------------------------------------------------
# rubygem1.9-data_objects.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname data_objects


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-data_objects
Version:        0.10.13
Release:        1%{?dist}
Summary:        DataObjects basic API and shared driver specifications

Group:          Development/Languages
License:        MIT
URL:            http://dataobjects.info
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-addressable >= 2.1

%description
Provide a standard and simplified API for communicating with RDBMS from Ruby


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
  rm -rf Rakefile spec tasks
  chmod 644 lib/data_objects/quoting.rb
  rm -f lib/data_objects/spec/quoting_spec.rb lib/data_objects/spec/typecast/ipaddr_spec.rb
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog.markdown
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.markdown
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Tue May 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.10.13-1%{?dist}
- New upstream version

* Mon Jan 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.10.12-1%{?dist}
- New upstream version

* Sat Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.10.11-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.10-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.10.8-1%{?dist}
- New upstream version

* Sun Oct 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.7-1%{?dist}
- New upstream version

* Wed May 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.6-1%{?dist}
- New upstream version

* Wed May 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.5-1%{?dist}
- New upstream version

* Sat Apr 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.4-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.3-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.10.3-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.10.2-1%{?dist}
- Initial package creation
