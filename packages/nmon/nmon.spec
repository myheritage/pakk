#-----------------------------------------------------------------------------
# nmon.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           nmon
Version:        14g
Release:        1%{?dist}
Summary:        Nigel's performance Monitor for Linux

Group:          Applications/System
License:        GPL
URL:            http://nmon.sourceforge.net/
Source0:        http://sourceforge.net/projects/nmon/files/lmon%{version}.c
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  ncurses-devel

%description
Nigel's performance Monitor for Linux.


#-----------------------------------------------------------------------------
%prep


#-----------------------------------------------------------------------------
%build
gcc -o %{name} %{SOURCE0} \
  %{optflags} -D JFS -D GETUSER -Wall -D LARGEMEM -lncurses -g


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
* Mon Apr 23 2012 Eric-Olivier Lamey <pakk@96b.it> - 14g-1%{?dist}
- Initial package creation
