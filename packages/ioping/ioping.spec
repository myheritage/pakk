#-----------------------------------------------------------------------------
# ioping.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           ioping
Version:        0.5
Release:        1%{?dist}
Summary:        Simple disk I/0 latency measuring tool

Group:          Applications/System
License:        GPLv3+
URL:            http://code.google.com/p/ioping/
Source0:        http://ioping.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Lets you monitor I/O latency in real time, in a way similar to how ping(1)
does for network latency.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build
%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

strip %{buildroot}%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


#-----------------------------------------------------------------------------
%changelog
* Sat Jun 25 2011 Eric-Olivier Lamey <pakk@96b.it> - 0.5-1%{?dist}
- Initial package creation heavily inspired by the spec file provided
