#-----------------------------------------------------------------------------
# ps_mem.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           ps_mem
Version:        2.7
Release:        1%{?dist}
Summary:        List processes by memory usage

Group:          Applications/System
License:        GPL
URL:            http://www.pixelbeat.org/scripts/
Source0:        http://www.pixelbeat.org/scripts/ps_mem.py
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python

%description
Try to determine how much RAM is currently being used per program.
Note per _program_, not per process. So for example this script
will report RAM used by all httpd process together. In detail it reports:
sum(private RAM for program processes) + sum(Shared RAM for program processes)
The shared RAM is problematic to calculate, and this script automatically
selects the most accurate method available for your kernel.


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}

install -p -D -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%changelog
* Sun Jul 1 2012 Eric-Olivier Lamey <pakk@96b.it> - 2.7-1%{?dist}
- Initial package creation
