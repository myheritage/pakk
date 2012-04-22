#-------------------------------------------------------------------------------
# rubygem1.9-nokogiri.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname nokogiri


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-nokogiri
Version:        1.5.1
Release:        1%{?dist}
Summary:        Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser

Group:          Development/Languages
License:        MIT
URL:            http://nokogiri.org
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  ruby1.9-devel
BuildRequires:  zlib-devel

Requires:       ruby1.9

%description
Nokogiri (鋸) is an HTML, XML, SAX, and Reader parser.  Among Nokogiri's
many features is the ability to search documents via XPath or CSS3 selectors.
XML is like violence - if it doesn’t solve your problems, you are not using
enough of it.


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
  rm -rf .autotest .gemtest Rakefile deps.rip ext tasks test
  strip lib/nokogiri/*.so
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/C_CODING_STYLE.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.ja.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.ja.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.rdoc
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Manifest.txt
%{_bindir}/%{gemname}
%{ruby_sitelib}/bin/%{gemname}
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/*.md


#-------------------------------------------------------------------------------
%changelog
* Fri Mar 9 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.5.1-1%{?dist}
- New upstream version

* Fri Jul 1 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.5.0-1%{?dist}
- New upstream version

* Wed Jun 22 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.6-1%{?dist}
- New upstream version

* Sat Jun 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.5-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.4.4-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Tue Nov 16 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.4.4-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.4.3.1-1%{?dist}
- Initial package creation
