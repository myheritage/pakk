#-------------------------------------------------------------------------------
# rubygem1.9-bson.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname bson


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-bson
Version:        1.6.3
Release:        1%{?dist}
Summary:        Ruby implementation of BSON

Group:          Development/Languages
License:        ASL 2.0
URL:            http://www.mongodb.org
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
A Ruby BSON implementation for MongoDB. For more information about Mongo,
see http://www.mongodb.org. For more information on BSON,
see http://www.bsonspec.org.


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
  rm -rf Rakefile ext bson.gemspec test
  sed -i -e 's|/usr/bin/ruby|/usr/bin/ruby1.9|g' bin/*
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/b2json %{buildroot}%{_bindir}/
ln -s %{ruby_sitelib}/bin/j2bson %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE.txt
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
* Wed Jun 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.6.3-1%{?dist}
- New upstream version

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
