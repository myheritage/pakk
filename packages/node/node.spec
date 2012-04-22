#-----------------------------------------------------------------------------
# node.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           node
Version:        0.6.15
Release:        1%{?dist}
Summary:        Evented I/O for V8 JavaScript

Group:          System Environment/Libraries
License:        Copyright Joyent, Inc. and other Node contributors
URL:            http://nodejs.org/
Source0:        http://nodejs.org/dist/%{name}-v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel
%if 0%{?rhel} <= 5
BuildRequires:  python26
%else
BuildRequires:  python
%endif
BuildRequires:  zlib-devel

%description
Node's goal is to provide an easy way to build scalable network programs.
Node tells the operating system (through epoll, kqueue, /dev/poll, or select)
that it should be notified when a new connection is made, and then it goes to
sleep. If someone new connects, then it executes the callback. Each connection
is only a small heap allocation.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        A node development environment
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Header files and libraries for building a node extension library.


#-----------------------------------------------------------------------------
%prep
%setup -q -n %{name}-v%{version}
sed -i -e '/^#!\/usr\/bin\/env python/d' tools/wafadmin/*.py tools/wafadmin/Tools/*.py


#-----------------------------------------------------------------------------
%build
# export JOBS=2
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  --shared-zlib

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

strip %{buildroot}%{_bindir}/%{name}
ln -sf %{_libdir}/%{name}_modules/npm/bin/npm-cli.js %{buildroot}%{_bindir}/npm

gzip %{buildroot}%{_mandir}/man1/*
pushd %{buildroot}%{_libdir}/%{name}_modules
  find . -name .gitmodules -exec rm -f {} \;
  sed -i -e'1i#!/usr/bin/env node\n' npm/bin/read-package-json.js
  chmod 755 npm/scripts/index-build.js npm/scripts/install.sh npm/scripts/clean-old.sh
  rm -rf npm/node_modules/node-uuid/benchmark npm/test
popd


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog LICENSE README.md
%{_bindir}/%{name}
%{_bindir}/npm
%{_libdir}/%{name}_modules
%{_mandir}/man1/%{name}.1.gz

%files devel
%doc LICENSE
%{_bindir}/%{name}-waf
%{_includedir}/%{name}
%{_libdir}/%{name}/wafadmin


#-----------------------------------------------------------------------------
%changelog
* Tue Apr 10 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.15-1%{?dist}
- New upstream version

* Sat Mar 24 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.14-1%{?dist}
- New upstream version

* Sun Mar 18 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.13-1%{?dist}
- New upstream version

* Tue Mar 6 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.12-1%{?dist}
- New upstream version

* Thu Feb 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.11-1%{?dist}
- New upstream version

* Fri Feb 3 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.10-1%{?dist}
- New upstream version

* Mon Jan 30 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.6.9-1%{?dist}
- New upstream version

* Sat Dec 17 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.6-1%{?dist}
- New upstream version

* Sun Dec 4 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.5-1%{?dist}
- New upstream version

* Fri Dec 2 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.4-1%{?dist}
- New upstream version

* Sat Nov 26 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.3-1%{?dist}
- New upstream version

* Sat Nov 12 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.1-1%{?dist}
- New upstream version

* Sun Nov 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.6.0-1%{?dist}
- New upstream version

* Sun Sep 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.4.12-1%{?dist}
- Initial package creation
