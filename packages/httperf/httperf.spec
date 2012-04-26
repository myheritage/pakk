#-----------------------------------------------------------------------------
# httperf.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           httperf
Version:        0.9.0
Release:        1%{?dist}
Summary:        The httperf HTTP load generator

Group:          Applications/System
License:        GPL
URL:            http://code.google.com/p/httperf/
Source0:        http://httperf.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  openssl-devel

%description
Httperf is a tool for measuring web server performance. It provides a
flexible facility for generating various HTTP workloads and for measuring
server performance.
The focus of httperf is not on implementing one particular benchmark but on
providing a robust, high-performance tool that facilitates the construction
of both micro- and macro-level benchmarks. The three distinguishing
characteristics of httperf are its robustness, which includes the ability
to generate and sustain server overload, support for the HTTP/1.1 and SSL
protocols, and its extensibility to new workload generators and performance
measurements.


#-----------------------------------------------------------------------------
%prep 
%setup -q


#-----------------------------------------------------------------------------
%build
%configure
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%{_bindir}/*
%{_mandir}/man1/*


#-----------------------------------------------------------------------------
%changelog
* Wed Apr 25 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.9.0-1%{?dist}
- Initial package creation
