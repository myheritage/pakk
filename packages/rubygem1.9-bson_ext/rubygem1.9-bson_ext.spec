#-------------------------------------------------------------------------------
# rubygem1.9-bson_ext.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname bson_ext


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-bson_ext
Version:        1.6.2
Release:        1%{?dist}
Summary:        C extensions for Ruby BSON

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.mongodb.org
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-bson = %{version}

%description
C extensions to accelerate the Ruby BSON serialization. For more information
about BSON, see http://bsonspec.org.  For information about MongoDB,
see http://www.mongodb.org.


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
gem1.9 install --local --force \
  --install-dir %{buildroot}%{ruby_sitelib} \
  %{SOURCE0}
rm -rf %{buildroot}%{ruby_sitelib}/cache

pushd %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}
  rm -rf .require_paths Rakefile ext/cbson ext/cmongo bson_ext.gemspec
  strip ext/bson_ext/*.so
popd

pushd %{buildroot}%{ruby_sitelib}
  sed -i -e 's|%{buildroot}||g' \
    doc/%{gemname}-%{version}/rdoc/ext/cbson/Makefile.html
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/ext
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Fri Apr 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.6.2-1%{?dist}
- New upstream version

* Thu Mar 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.6.1-1%{?dist}
- New upstream version

* Thu Feb 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.6.0-1%{?dist}
- New upstream version

* Sat Dec 17 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.2-1%{?dist}
- New upstream version

* Thu Nov 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.1-1%{?dist}
- New upstream version

* Thu Oct 20 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.1-1%{?dist}
- New upstream version

* Wed Sep 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.0-1%{?dist}
- New upstream version

* Wed May 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.1-1%{?dist}
- New upstream version

* Thu Apr 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.3.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Thu Feb 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.4-1%{?dist}
- New upstream version

* Wed Feb 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.3-1%{?dist}
- New upstream version

* Wed Feb 16 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.2-1%{?dist}
- New upstream version

* Fri Feb 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.1-1%{?dist}
- New upstream version

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.0-1%{?dist}
- New upstream version

* Thu Dec 16 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1.5-1%{?dist}
- New upstream version

* Wed Dec 1 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1.4-1%{?dist}
- New upstream version

* Fri Nov 5 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1.2-1%{?dist}
- New upstream version

* Fri Oct 15 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1.1-1%{?dist}
- New upstream version

* Sat Oct 9 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.1-1%{?dist}
- Initial package creation
