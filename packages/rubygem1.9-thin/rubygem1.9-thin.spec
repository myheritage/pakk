#-------------------------------------------------------------------------------
# rubygem1.9-thin.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname thin


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-thin
Version:        1.2.7
Release:        3%{?dist}
Summary:        A thin and fast web server (rubygem)

Group:          Development/Languages
License:        Ruby
URL:            http://code.macournoyer.com/thin/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}.config.yml
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       initscripts
Requires:       ruby1.9
Requires:       rubygem1.9-daemons
Requires:       rubygem1.9-eventmachine
Requires:       rubygem1.9-rack
Requires:       shadow-utils

%description
Thin is a Ruby web server that glues together 3 of the best Ruby
libraries in web history:
* the Mongrel parser: the root of Mongrel speed and security
* Event Machine: a network I/O library with extremely high scalability,
  performance and stability
* Rack: a minimal interface between webservers and Ruby frameworks
Which makes it, with all humility, the most secure, stable, fast and
extensible Ruby web server bundled in an easy to use gem for your own
pleasure.

This package contains the rubygem code. If you need to run this service
as a daemon, please install the "thin" package.

#-----------------------------------------------------------------------------
# thin package
#-----------------------------------------------------------------------------
%package -n thin
Summary:        A thin and fast web server
Group:          System Environment/Daemons

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       %{name} = %{version}

%description -n thin
Thin is a Ruby web server that glues together 3 of the best Ruby
libraries in web history:
* the Mongrel parser: the root of Mongrel speed and security
* Event Machine: a network I/O library with extremely high scalability,
  performance and stability
* Rack: a minimal interface between webservers and Ruby frameworks
Which makes it, with all humility, the most secure, stable, fast and 
extensible Ruby web server bundled in an easy to use gem for your own 
pleasure.


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
  rm -rf Rakefile benchmark spec tasks

  # let's make rpmlint happy
  rm -rf ext
  strip lib/*.so
  chmod 755 lib/thin/controllers/service.sh.erb
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_sysconfdir}/%{gemname}
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{gemname}/config.yml

install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{gemname}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gemname}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{gemname}

mkdir -p %{buildroot}%{_localstatedir}/log/%{gemname}
mkdir -p %{buildroot}%{_localstatedir}/run/%{gemname}


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre -n thin
if [ $1 == 1 ]; then
  /usr/bin/getent group %{gemname} > /dev/null || \
    /usr/sbin/groupadd -r %{gemname}
  /usr/sbin/useradd -g "%{gemname}" -c "%{gemname} user" -s /sbin/nologin -r -M \
    -d %{_sysconfdir}/%{gemname} %{gemname} 2> /dev/null || :
fi

%post -n thin
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{gemname}
fi

%preun -n thin
if [ $1 = 0 ]; then
  /sbin/service %{gemname} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{gemname}
fi

%postun -n thin
if [ $1 == 2 ]; then
  /sbin/service %{gemname} reload || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CHANGELOG
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%{_bindir}/*
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n thin
%dir %{_sysconfdir}/%{gemname}
%config(noreplace) %{_sysconfdir}/%{gemname}/*.yml
%config(noreplace) %{_sysconfdir}/logrotate.d/%{gemname}
%config(noreplace) %{_sysconfdir}/sysconfig/%{gemname}
%{_initrddir}/%{gemname}
%dir %{_localstatedir}/log/%{gemname}
%attr(-, thin, root) %dir %{_localstatedir}/run/%{gemname}

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/example


#-------------------------------------------------------------------------------
%changelog
* Sun Jan 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.2.7-3%{?dist}
- Better dependencies

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.7-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.2.7-1%{?dist}
- Initial package creation
