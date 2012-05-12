#-------------------------------------------------------------------------------
# rubygem1.9-raindrops.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname raindrops


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-raindrops
Version:        0.8.1
Release:        1%{?dist}
Summary:        Real-time stats toolkit for Rack HTTP servers

Group:          Development/Languages
License:        MIT
URL:            http://raindrops.bogomips.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       ruby1.9

%description
Raindrops is a real-time stats toolkit to show statistics for Rack HTTP
servers. It is designed for preforking servers such as Rainbows! and Unicorn,
but should support any Rack HTTP server under Ruby 1.9, 1.8 and Rubinius on
platforms supporting POSIX shared memory. It may also be used as a generic
scoreboard for sharing atomic counters across multiple processes.


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
  rm -rf .??* GIT* GNUmakefile Gemfile Rakefile ext pkg.mk setup.rb test *.gemspec
  strip lib/*.so
  chmod 644 NEWS ChangeLog
popd


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LATEST
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/NEWS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/TODO
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/examples


#-------------------------------------------------------------------------------
%changelog
* Sat May 12 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.8.1-1%{?dist}
- New upstream version

* Sat Jul 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.7.0-1%{?dist}
- Initial package creation
