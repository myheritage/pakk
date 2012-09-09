#-------------------------------------------------------------------------------
# rubygem1.9-eventmachine.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname eventmachine


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-eventmachine
Version:        1.0.0
Release:        1%{?dist}
Summary:        Ruby/EventMachine library

Group:          Development/Languages
License:        Ruby
URL:            http://rubyeventmachine.com
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
EventMachine implements a fast, single-threaded engine for arbitrary network
communications. It's extremely easy to use in Ruby. EventMachine wraps all
interactions with IP sockets, allowing programs to concentrate on the
implementation of network protocols. It can be used to create both network
servers and clients. To create a server or client, a Ruby program only needs
to specify the IP address and port, and provide a Module that implements the
communications protocol. Implementations of several standard network protocols
are provided with the package, primarily to serve as examples. The real goal
of EventMachine is to enable programs to easily interface with other programs
using TCP/IP, especially if custom protocols are required.


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
  rm -rf .??* Gemfile Rakefile *.gemspec ext java rakelib tests
  strip lib/*.so
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/GNU
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/docs
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Sun Sep 9 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.12.10-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 0.12.10-1%{?dist}
- Initial package creation
