#-------------------------------------------------------------------------------
# rubygem1.9-escape_utils.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname escape_utils


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-escape_utils
Version:        0.3.2
Release:        1%{?dist}
Summary:        Faster string escaping routines for your web apps

Group:          Development/Languages
License:        MIT
URL:            http://github.com/brianmario/escape_utils
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Being as though we're all html escaping everything these days, why not make
it faster? At the moment escape_utils supports escaping and unescaping of HTML,
and Javascript but I wanna add URL encoding soon.
For character encoding in 1.9, we'll return strings in whatever
Encoding.default_internal is set to or utf-8 otherwise.
It has monkey-patches for Rack::Utils, CGI, ERB::Util and Haml and ActionView
so you can drop this in and have your app start escaping fast as balls in
no time


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
  rm -rf .??* Rakefile Gemfile escape_utils.gemspec ext spec test
  strip lib/%{gemname}/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/MIT-LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/benchmark


#-------------------------------------------------------------------------------
%changelog
* Mon Mar 4 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.3.2-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.3.0-1%{?dist}
- New upstream version

* Fri Sep 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.4-1%{?dist}
- New upstream version

* Wed Mar 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.3-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.2-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Fri Feb 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.2-1%{?dist}
- New upstream version

* Wed Feb 23 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.1-1%{?dist}
- New upstream version

* Wed Feb 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.2.0-1%{?dist}
- New upstream version

* Tue Nov 2 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.1.9-1%{?dist}
- Initial package creation
