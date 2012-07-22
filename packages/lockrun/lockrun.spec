#-----------------------------------------------------------------------------
# lockrun.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           lockrun
Version:        0.20090625
Release:        1%{?dist}
Summary:        Run cron job with overrun protection

Group:          Applications/System
License:        GPL
URL:            http://www.unixwiz.net/tools/lockrun.html
Source0:        http://www.unixwiz.net/tools/%{name}.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Run cron job with overrun protection.


#-----------------------------------------------------------------------------
%prep


#-----------------------------------------------------------------------------
%build
gcc -o %{name} %{SOURCE0} %{optflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
strip %{buildroot}%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%files
%defattr(-, root, root, -)
%{_bindir}/%{name}


#-----------------------------------------------------------------------------
%changelog
* Sun Jul 22 2012 Eric-Olivier Lamey <pakk@96b.it> - 0.20090625-1%{?dist}
- Initial package creation
