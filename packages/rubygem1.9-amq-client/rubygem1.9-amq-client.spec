#-------------------------------------------------------------------------------
# rubygem1.9-amq-client.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname amq-client


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-amq-client
Version:        0.9.12
Release:        1%{?dist}
Summary:        Fully-featured, low-level AMQP 0.9.1 client

Group:          Development/Languages
License:        Ruby
URL:            https://github.com/ruby-amqp/amq-client
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-amq-protocol >= 1.2.0
Requires:       rubygem1.9-eventmachine

%description
amq-client is a fully-featured, low-level AMQP 0.9.1 client with pluggable
networking I/O adapters (EventMachine, cool.io, Eventpanda and so on) and
supposed to back more opinionated AMQP clients (such as amqp gem) or be used
directly in cases when access to more advanced AMQP 0.9.1 features is more
important that convenient APIs.


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
  rm -rf .??* Gemfile Rakefile *.gemspec *.rb bin spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.textile
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.9.12-1%{?dist}
- New upstream version

* Sun Jan 27 2013 Eric-Olivier Lamey <pakk@96b.it> - 0.9.11-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.10-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.5-1%{?dist}
- New upstream version

* Sun Jul 8 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.4-1%{?dist}
- New upstream version

* Wed Jun 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.3-1%{?dist}
- New upstream version

* Sun Feb 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.2-1%{?dist}
- New upstream version

* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.1-1%{?dist}
- New upstream version

* Wed Jan 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.0-1%{?dist}
- New upstream version

* Wed Dec 7 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.7-1%{?dist}
- New upstream version

* Fri Nov 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.6-1%{?dist}
- New upstream version

* Sun Oct 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.5-1%{?dist}
- New upstream version

* Sun Sep 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.8.3-1%{?dist}
- Initial package creation
