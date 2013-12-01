#-------------------------------------------------------------------------------
# rubygem1.9-unicorn.spec
#-------------------------------------------------------------------------------

%global ruby_sitelib  %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitelibdir']")
%global ruby_sitearch %(ruby1.9 -rrbconfig -e "puts RbConfig::CONFIG['sitearchdir']")

%global gemname unicorn


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubygem1.9-unicorn
Version:        4.7.0
Release:        1%{?dist}
Summary:        Rack HTTP server for fast clients and Unix (rubygem)

Group:          Development/Languages
License:        Ruby and GPLv2 and GPLv3
URL:            http://unicorn.bogomips.org/
Source0:        http://rubygems.org/downloads/%{gemname}-%{version}.gem
Source1:        %{name}.config.rb
Source2:        %{name}.init
Source3:        %{name}.sysconfig
Source4:        %{name}.logrotate
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ruby1.9-devel

Requires:       initscripts
Requires:       ruby1.9
Requires:       rubygem1.9-kgio >= 2.6
Requires:       rubygem1.9-rack
Requires:       rubygem1.9-raindrops >= 0.7
Requires:       shadow-utils

%description
Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between Unicorn and slow clients.

This package contains the rubygem code. If you need to run this service
as a daemon, please install the "unicorn" package.


#-----------------------------------------------------------------------------
# unicorn package
#-----------------------------------------------------------------------------
%package -n unicorn
Summary:        Rack HTTP server for fast clients and Unix
Group:          System Environment/Daemons

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

Requires:       %{name} = %{version}

%description -n unicorn
Unicorn is an HTTP server for Rack applications designed to only serve
fast clients on low-latency, high-bandwidth connections and take
advantage of features in Unix/Unix-like kernels.  Slow clients should
only be served by placing a reverse proxy capable of fully buffering
both the the request and response in between \Unicorn and slow clients.


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
  rm -rf .??* GIT* GNUmakefile Rakefile ext local.mk.sample script setup.rb t test *.gemspec

  sed -i -e 's|/this/will/be/overwritten/or/wrapped/anyways/do/not/worry/ruby|/usr/bin/ruby1.9|g' bin/*
 
  chmod 644 NEWS ChangeLog
  find . \( -name .gitignore -o -name .gitkeep \) -exec rm -f {} \;

  strip lib/*.so
popd

mkdir -p %{buildroot}%{_bindir}
ln -s %{ruby_sitelib}/bin/%{gemname} %{ruby_sitelib}/bin/unicorn_rails \
  %{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_mandir}/man1
cp %{buildroot}%{ruby_sitelib}/gems/%{gemname}-%{version}/man/man1/* \
  %{buildroot}%{_mandir}/man1 && gzip %{buildroot}%{_mandir}/man1/*

install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/%{gemname}/config.rb

install -p -D -m 0755 %{SOURCE2} %{buildroot}%{_initrddir}/%{gemname}
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{gemname}
install -p -D -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/logrotate.d/%{gemname}

mkdir -p %{buildroot}%{_localstatedir}/log/%{gemname}
mkdir -p %{buildroot}%{_localstatedir}/run/%{gemname}


#-------------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%pre -n unicorn
if [ $1 == 1 ]; then
  /usr/bin/getent group %{gemname} > /dev/null || \
      /usr/sbin/groupadd -r %{gemname}
  /usr/sbin/useradd -g "%{gemname}" -c "%{gemname} user" -s /bin/false -r -M \
    -d %{_sysconfdir}/%{gemname} %{gemname} 2> /dev/null || :
fi

%post -n unicorn
if [ $1 == 1 ]; then
  /sbin/chkconfig --add %{gemname}
fi

%preun -n unicorn
if [ $1 = 0 ]; then
  /sbin/service %{gemname} stop > /dev/null 2>&1
  /sbin/chkconfig --del %{gemname}
fi

%postun -n unicorn
if [ $1 == 2 ]; then
  /sbin/service %{gemname} upgrade || :
fi


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/CONTRIBUTORS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/COPYING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ChangeLog
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/FAQ
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/ISSUES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/KNOWN_ISSUES
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LATEST
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/LICENSE
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Links
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/NEWS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/README
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/TODO
%{_bindir}/*
%{_mandir}/man1/*.gz
%{ruby_sitelib}/bin/*
%dir %{ruby_sitelib}/gems/%{gemname}-%{version}
%{ruby_sitelib}/gems/%{gemname}-%{version}/bin
%{ruby_sitelib}/gems/%{gemname}-%{version}/lib
%{ruby_sitelib}/specifications/%{gemname}-%{version}.gemspec

%files -n unicorn
%defattr(-, root, root, -)
%dir %{_sysconfdir}/%{gemname}
%config(noreplace) %{_sysconfdir}/%{gemname}/*.rb
%config(noreplace) %{_sysconfdir}/logrotate.d/%{gemname}
%config(noreplace) %{_sysconfdir}/sysconfig/%{gemname}
%{_initrddir}/%{gemname}
%dir %{_localstatedir}/log/%{gemname}
%dir %{_localstatedir}/run/%{gemname}

%files doc
%doc %{ruby_sitelib}/doc/%{gemname}-%{version}
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Application_Timeouts
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/DESIGN
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Documentation
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/HACKING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/PHILOSOPHY
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/SIGNALS
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/Sandbox
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/TUNING
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/examples
%doc %{ruby_sitelib}/gems/%{gemname}-%{version}/man


#-------------------------------------------------------------------------------
%changelog
* Tue Dec 3 2013 Eric-Olivier Lamey <pakk@96b.it> - 4.7.0-1%{?dist}
- New upstream version

* Sat Jun 22 2013 Eric-Olivier Lamey <pakk@96b.it> - 4.6.3-1%{?dist}
- New upstream version

* Tue Feb 26 2013 Eric-Olivier Lamey <pakk@96b.it> - 4.6.2-1%{?dist}
- New upstream version

* Wed Feb 6 2013 Eric-Olivier Lamey <pakk@96b.it> - 4.6.0-1%{?dist}
- New upstream version

* Mon Dec 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.5.0-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.4.0-1%{?dist}
- New upstream version

* Sun Apr 29 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.3.1-1%{?dist}
- New upstream version

* Thu Apr 19 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.3.0-1%{?dist}
- New upstream version

* Tue Mar 27 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.2.1-1%{?dist}
- New upstream version

* Tue Jan 31 2012 Eric-Olivier Lamey <pakk@96b.it> - 4.2.0-1%{?dist}
- New upstream version

* Sat Aug 27 2011 Eric-Olivier Lamey <pakk@96b.it> - 4.1.1-1%{?dist}
- New upstream version

* Sat Jul 9 2011 Eric-Olivier Lamey <pakk@96b.it> - 4.0.1-1%{?dist}
- New upstream version

* Sat Jun 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.7.0-1%{?dist}
- New upstream version

* Sat Apr 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.6.2-1%{?dist}
- New upstream version

* Sun Apr 24 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.6.0-1%{?dist}
- New upstream version

* Sat Mar 19 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.5.0-1%{?dist}
- New upstream version

* Sun Mar 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.4.0-2%{?dist}
- Massive rebuild to change pakk's packages requirements

* Fri Feb 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.4.0-1%{?dist}
- New upstream version

* Sun Jan 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.3.1-1%{?dist}
- New upstream version

* Thu Jan 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.3.0-1%{?dist}
- New upstream version

* Mon Dec 27 2010 Eric-Olivier Lamey <pakk@96b.it> - 3.2.1-1%{?dist}
- New upstream version

* Fri Dec 10 2010 Eric-Olivier Lamey <pakk@96b.it> - 3.1.0-1%{?dist}
- New upstream version

* Fri Dec 3 2010 Eric-Olivier Lamey <pakk@96b.it> - 3.0.1-1%{?dist}
- New upstream version

* Mon Nov 22 2010 Eric-Olivier Lamey <pakk@96b.it> - 3.0.0-1%{?dist}
- New upstream version

* Thu Oct 28 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0-1%{?dist}
- New upstream version

* Sat Oct 23 2010 Eric-Olivier Lamey <pakk@96b.it> - 2.0.0pre2-1%{?dist}
- Initial package creation
