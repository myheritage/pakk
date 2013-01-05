#-------------------------------------------------------------------------------
# rubygem1.9-json.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname json


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-json
Version:        1.7.6
Release:        1%{?dist}
Summary:        This is a JSON implementation as a Ruby extension in C

Group:          Development/Languages
License:        GPL
URL:            http://json-jruby.rubyforge.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
This is a implementation of the JSON specification according to RFC 4627
http://www.ietf.org/rfc/rfc4627.txt.


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
  rm -rf ext lib/json/ext/.keep
  strip lib/json/ext/*.so
  rm -rf .??* COPYING-json-jruby README-json-jruby.markdown Gemfile Rakefile \
    benchmarks data diagrams install.rb java *.gemspec tests tools
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/GPL
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/TODO
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/VERSION
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}


#-------------------------------------------------------------------------------
%changelog
* Sat Jan 5 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.7.6-1%{?dist}
- New upstream version

* Sat Aug 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.7.5-1%{?dist}
- New upstream version

* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.7.3-1%{?dist}
- New upstream version

* Mon May 7 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.7.1-1%{?dist}
- New upstream version

* Sat Apr 28 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.7.0-1%{?dist}
- New upstream version

* Tue Mar 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.6.6-1%{?dist}
- New upstream version

* Sun Dec 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.4-1%{?dist}
- New upstream version

* Thu Dec 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.3-1%{?dist}
- New upstream version

* Wed Sep 21 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.1-1%{?dist}
- New upstream version

* Wed Sep 14 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.6.0-1%{?dist}
- New upstream version

* Wed Aug 31 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.4-1%{?dist}
- New upstream version

* Wed Jun 22 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.3-1%{?dist}
- New upstream version

* Sat Jun 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.2-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.1-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Mar 5 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.1-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.4.6-1%{?dist}
- Initial package creation
