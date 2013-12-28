#-----------------------------------------------------------------------------
# ruby2.0.spec
#-----------------------------------------------------------------------------

%global ruby_major     2.1
%global program_suffix %{ruby_major}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           ruby2.1
Version:        2.1.0
Release:        1%{?dist}
Summary:        An interpreter of object-oriented scripting language

Group:          Development/Languages
License:        Ruby or GPLv2
URL:            http://www.ruby-lang.org/
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/%{ruby_major}/ruby-%{version}.tar.bz2
Source1:        %{name}-gemrc
Patch0:         %{name}-gempath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  zlib-devel

Requires:       db4
Requires:       gdbm
Requires:       ncurses
Requires:       openssl
Requires:       readline
Requires:       zlib

Provides:       ruby(abi) = %{ruby_major}

%description
Ruby is the interpreted scripting language for quick and easy
object-oriented programming. It has many features to process text
files and to do system management tasks (as in Perl). It is simple,
straight-forward, and extensible.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        A Ruby development environment
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Header files and libraries for building Ruby extension libraries.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc
Summary:        Ruby documentation
Group:          Documentation

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

%description doc
Documentation for Ruby methods, classes and modules which can be
accessed with the ri tool.


#-----------------------------------------------------------------------------
# -tcltk package
#-----------------------------------------------------------------------------
%package tcltk
Summary:        Tcl/tk libraries for Ruby
Group:          Development/Languages

Requires:       %{name} = %{version}
Requires:       tcl
Requires:       tk

%description tcltk
Tcl and tk Ruby libraries.


#-----------------------------------------------------------------------------
%prep
%setup -q -n ruby-%{version}
%patch0 -p1


#-----------------------------------------------------------------------------
%build
%configure \
  --enable-shared \
  --disable-rpath \
  --program-suffix=%{program_suffix} \
  --with-sitedir=%{_libdir}/ruby/site \
  --with-vendordir=%{_libdir}/ruby/vendor

%{__make} %{?_smp_mflags}


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

pushd %{buildroot}%{_libdir}/ruby/%{version}
  chmod 755 abbrev.rb tkextlib/pkg_checker.rb
popd

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gemrc2.0


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc ChangeLog COPYING* GPL LEGAL NEWS README*
%config(noreplace) %{_sysconfdir}/gemrc2.0
%{_bindir}/*
%{_libdir}/ruby/%{version}
%exclude %{_libdir}/ruby/%{version}/*tk*
%exclude %{_libdir}/ruby/%{version}/*tcl*
%exclude %{_libdir}/ruby/%{version}/%{_arch}-*/*tk*
%exclude %{_libdir}/ruby/%{version}/%{_arch}-*/*tcl*
%{_libdir}/ruby/gems/%{version}
%{_libdir}/ruby/site/%{version}
%{_libdir}/ruby/vendor/%{version}
%{_libdir}/*.so.*
%{_mandir}/man1/*.1.gz

%files tcltk
%doc COPYING* GPL LEGAL
%{_libdir}/ruby/%{version}/*tk*
%{_libdir}/ruby/%{version}/*tcl*
%{_libdir}/ruby/%{version}/%{_arch}-*/*tk*
%{_libdir}/ruby/%{version}/%{_arch}-*/*tcl*

%files devel
%doc COPYING* GPL LEGAL
%{_includedir}/ruby-%{version}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libruby.so
%{_libdir}/*.a

%files doc
%doc COPYING* GPL LEGAL
%{_datadir}/ri


#-----------------------------------------------------------------------------
%changelog
* Sat Dec 28 2013 Eric-Olivier Lamey <pakk@96b.it> - 2.1.0-1%{?dist}
- Initial package creation
