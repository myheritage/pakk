#-----------------------------------------------------------------------------
# gecode.spec
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           gecode
Version:        3.5.0
Release:        1%{?dist}
Summary:        Toolkit for developing constraint-based systems and applications

Group:          System Environment/Libraries
License:        MIT
URL:            http://www.gecode.org
Source0:        http://www.gecode.org/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%if 0%{?rhel} <= 5
BuildRequires:  gcc44
BuildRequires:  gcc44-c++
%endif

%description
Gecode is a toolkit for developing constraint-based systems and applications.
Gecode provides a constraint solver with state-of-the-art performance while
being modular and extensible.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        Development libraries and headers for developing gecode applications
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Development libraries and headers for developing gecode applications.


#-----------------------------------------------------------------------------
%prep
%setup -q
chmod 644 LICENSE


#-----------------------------------------------------------------------------
%build
%if 0%{?rhel} <= 5
export CC=gcc44
export CXX=g++44
%endif
%configure \
  --enable-float-vars \
  --disable-gist \
  --disable-qt \
  --disable-examples

%{__make} %{?_smp_mflags}
%{__make} ChangeLog
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.new && \
  mv ChangeLog.new ChangeLog


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

rm -rf %{buildroot}%{_includedir}/examples
find %{buildroot}%{_includedir} -type f -exec chmod 644 {} \;
strip %{buildroot}%{_bindir}/*
strip %{buildroot}%{_libdir}/*


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-------------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc ChangeLog LICENSE
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so


#-----------------------------------------------------------------------------
%changelog
* Sun Apr 3 2011 Eric-Olivier Lamey <pakk@96b.it> - 3.5.0-1%{?dist}
- Initial package creation
