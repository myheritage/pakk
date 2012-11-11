#-----------------------------------------------------------------------------
# ruby1.9.spec
#-----------------------------------------------------------------------------

%global ruby_major          1.9
%global ruby_version        1.9.3
%global ruby_patchlevel     p327
%global ruby_compatibility  1.9.1
%global program_suffix      %{ruby_major}


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           ruby1.9
Version:        %{ruby_version}.%{ruby_patchlevel}
Release:        1%{?dist}
Summary:        An interpreter of object-oriented scripting language

Group:          Development/Languages
License:        Ruby or GPLv2
URL:            http://www.ruby-lang.org/
Source0:        ftp://ftp.ruby-lang.org/pub/ruby/%{ruby_major}/ruby-%{ruby_version}-%{ruby_patchlevel}.tar.bz2
Source1:        %{name}-gemrc
Patch0:         %{name}-gempath.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel
BuildRequires:  gdbm-devel
BuildRequires:  libffi-devel
BuildRequires:  libyaml-devel
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
%prep
%setup -q -n ruby-%{ruby_version}-%{ruby_patchlevel}
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

pushd %{buildroot}%{_libdir}/ruby/%{ruby_compatibility}
  chmod 755 abbrev.rb set.rb tkextlib/pkg_checker.rb
popd

install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/gemrc
mkdir -p %{buildroot}%{_libdir}/ruby/gems/%{ruby_compatibility}


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc ChangeLog COPYING* GPL LEGAL NEWS README*
%config(noreplace) %{_sysconfdir}/gemrc
%{_bindir}/*
%{_libdir}/ruby/%{ruby_compatibility}
%exclude %{_libdir}/ruby/%{ruby_compatibility}/*tk*
%exclude %{_libdir}/ruby/%{ruby_compatibility}/*tcl*
%exclude %{_libdir}/ruby/%{ruby_compatibility}/%{_arch}-linux/*tk*
%exclude %{_libdir}/ruby/%{ruby_compatibility}/%{_arch}-linux/*tcl*
%{_libdir}/ruby/gems/%{ruby_compatibility}
%{_libdir}/ruby/site/%{ruby_compatibility}
%{_libdir}/ruby/vendor/%{ruby_compatibility}
%{_libdir}/*.so.*
%{_mandir}/man1/*.1.gz

%files tcltk
%doc COPYING* GPL LEGAL
%{_libdir}/ruby/%{ruby_compatibility}/*tk*
%{_libdir}/ruby/%{ruby_compatibility}/*tcl*
%{_libdir}/ruby/%{ruby_compatibility}/%{_arch}-linux/*tk*
%{_libdir}/ruby/%{ruby_compatibility}/%{_arch}-linux/*tcl*

%files devel
%doc COPYING* GPL LEGAL
%{_includedir}/ruby-%{ruby_compatibility}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libruby.so
%{_libdir}/*.a

%files doc
%doc COPYING* GPL LEGAL
%{_datadir}/ri


#-----------------------------------------------------------------------------
%changelog
* Sun Nov 11 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p327-1%{?dist}
- New upstream version

* Sun Oct 21 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p286-1%{?dist}
- New upstream version

* Fri Apr 20 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p194-1%{?dist}
- New upstream version

* Thu Feb 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p125-1%{?dist}
- New upstream version

* Thu Feb 16 2012 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p125-1%{?dist}
- New upstream version

* Sun Oct 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.3.p0-1%{?dist}
- New upstream version

* Sat Aug 6 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p290-3%{?dist}
- Applied GC patch again

* Sat Jul 16 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p290-1%{?dist}
- New upstream version
- Removed previously applied GC patch

* Fri Feb 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p180-2%{?dist}
- Better dependencies for the -tcltk package
- Applied GC patch from http://redmine.ruby-lang.org/issues/1047

* Fri Feb 18 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p180-1%{?dist}
- New upstream version

* Tue Feb 15 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p136-2%{?dist}
- Separate tcltk package

* Mon Dec 27 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p136-1%{?dist}
- New upstream version
- ruby1.9-etc-sysconfdir.patch was integrated upstream

* Tue Sep 21 2010 Eric-Olivier Lamey <pakk@96b.it> - 1.9.2.p0-2%{?dist}
- Initial package creation
- ruby1.9-etc-sysconfdir.patch (ruby-core:32394)
