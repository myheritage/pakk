#-------------------------------------------------------------------------------
# rubygem1.9-em-http-request.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname em-http-request


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-em-http-request
Version:        1.1.2
Release:        1%{?dist}
Summary:        EventMachine based, async HTTP Request client

Group:          Development/Languages
License:        MIT
URL:            http://github.com/igrigorik/em-http-request
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  ruby1.9-devel

Requires:       ruby1.9
Requires:       rubygem1.9-addressable >= 2.3.4
Requires:       rubygem1.9-cookiejar
Requires:       rubygem1.9-em-socksify >= 0.3
Requires:       rubygem1.9-eventmachine >= 1.0.3
Requires:       rubygem1.9-http_parser >= 0.6.0

%description
Async (EventMachine) HTTP client, with support for:
- Asynchronous HTTP API for single & parallel request execution
- Keep-Alive and HTTP pipelining support
- Auto-follow 3xx redirects with max depth
- Automatic gzip & deflate decoding
- Streaming response processing
- Streaming file uploads
- HTTP proxy and SOCKS5 support
- Basic Auth & OAuth
- Connection-level & Global middleware support
- Ryan Dahl's HTTP parser via http_parser.rb
- Works wherever EventMachine runs


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
  rm -rf .??* Gemfile Rakefile *.gemspec spec
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Changelog.md
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README.md
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/benchmarks
%{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Sun Dec 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.1.2-1%{?dist}
- New upstream version

* Tue Jun 25 2013 Eric-Olivier Lamey <pakk@96b.it> - 1.1.0-1%{?dist}
- New upstream version

* Tue Nov 13 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.0.3-1%{?dist}
- New upstream version

* Mon Apr 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.3.0-1%{?dist}
- Initial package creation
