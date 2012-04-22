#-----------------------------------------------------------------------------
# rubinius.spec
# - add %{_libdir}/%{name}/site/gems to gem's load path
#-----------------------------------------------------------------------------

%global release_date 20110705
%global llvm_version 2.8


#-----------------------------------------------------------------------------
# Main package
#-----------------------------------------------------------------------------
Name:           rubinius
Version:        1.2.4
Release:        1%{?dist}
Summary:        An implementation of the Ruby programming language

Group:          Development/Languages
License:        BSD
URL:            http://rubini.us/
Source0:        http://asset.rubini.us/%{name}-%{version}-%{release_date}.tar.gz
Source1:        http://asset.rubini.us/prebuilt/llvm-%{llvm_version}-i686-pc-linux-gnu-4.1.tar.bz2
Source2:        http://asset.rubini.us/prebuilt/llvm-%{llvm_version}-i686-pc-linux-gnu-4.1.tar.bz2.md5
Source3:        http://asset.rubini.us/prebuilt/llvm-%{llvm_version}-x86_64-unknown-linux-gnu-4.1.tar.bz2
Source4:        http://asset.rubini.us/prebuilt/llvm-%{llvm_version}-x86_64-unknown-linux-gnu-4.1.tar.bz2.md5
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  db4-devel
BuildRequires:  gdbm-devel
BuildRequires:  openssl-devel
BuildRequires:  readline-devel
BuildRequires:  ruby1.9-devel
BuildRequires:  zlib-devel

Requires:       db4
Requires:       gdbm
Requires:       openssl
Requires:       readline
Requires:       zlib

%description
Rubinius is an implementation of the Ruby programming language. Rubinius
includes a bytecode virtual machine, parser, bytecode compiler, garbage
collector, JIT native machine code compiler, and Ruby core and standard
libraries.

Rubinius currently is compatible with Ruby version 1.8.7. Support for Ruby
version 1.9.2 is coming soon.


#-----------------------------------------------------------------------------
# -devel package
#-----------------------------------------------------------------------------
%package devel
Summary:        A rubinius development environment
Group:          Development/Languages

Requires:       %{name} = %{version}

%description devel
Header files and libraries for building a extension library for
rubinius or an application embedded rubinius.


#-----------------------------------------------------------------------------
# -doc package
#-----------------------------------------------------------------------------
%package doc 
Summary:        Rubinius documentation
Group:          Documentation

%if 0%{?rhel} >= 6
BuildArch:      noarch
%endif

%description doc 
Documentation for Rubinius.


#-----------------------------------------------------------------------------
%prep
%setup -q


#-----------------------------------------------------------------------------
%build
mkdir vm/external_libs/prebuilt
%ifarch i386
cp %{SOURCE1} vm/external_libs/prebuilt/
cp %{SOURCE2} vm/external_libs/prebuilt/
%endif
%ifarch x86_64
cp %{SOURCE3} vm/external_libs/prebuilt/
cp %{SOURCE4} vm/external_libs/prebuilt/
%endif
export CFLAGS="%{optflags}"
ruby1.9 configure \
  --rake rake1.9 \
  --skip-system \
  --bindir=%{_bindir} \
  --includedir=%{_includedir}/%{name} \
  --libdir=%{_libdir}/ \
  --mandir=%{_mandir} \
  --gemsdir=%{_libdir}/%{name}/gems \
  --sitedir=%{_libdir}/%{name}/site \
  --vendordir=%{_libdir}/%{name}/vendor

sed -i -e '/sh "bin\/mspec ci --background --agent"/d' Rakefile
rake1.9


#-----------------------------------------------------------------------------
%install
rm -rf %{buildroot}
rake1.9 install FAKEROOT=%{buildroot}

mkdir -p %{buildroot}%{_libdir}/%{name}/{site,vendor}

pushd %{buildroot}%{_bindir}
  strip rbx
  rm ruby
  for binary in gem irb rake rdoc ri; do
    mv ${binary} ${binary}rbx
  done
popd

pushd %{buildroot}%{_libdir}/%{name}
  find . -name \*.so -exec strip {} \;
  pushd 1.2/lib/bin
    for file in *.rb; do
      mv ${file} $(basename ${file} .rb)rbx.rb
    done
    for file in *.rbc; do
      mv ${file} $(basename ${file} .rbc)rbx.rbc
    done
  popd
  pushd gems/bin
    for file in *; do
      mv ${file} ${binary}rbx
    done
  popd
popd

pushd %{buildroot}
  find . -exec grep -q \
    -e '#!/usr/bin/env ruby' \
    -e '#!/usr/local/bin/ruby' \
    -e '#!/usr/bin/env rubinius' \
    -e '#!/Users/evan/git/rbx/bin/rbx' \
    -e '#!/System/Library/Frameworks/Ruby.framework/Versions/1.8/usr/bin/ruby' {} \; -print | \
    xargs sed -i -e '1c#!/usr/bin/env rbx'
popd


#-----------------------------------------------------------------------------
%clean
rm -rf %{buildroot}


#-----------------------------------------------------------------------------
%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, -)
%doc AUTHORS LICENSE README THANKS
%{_bindir}/*
%{_libdir}/%{name}
%exclude %{_libdir}/%{name}/1.2/lib/rubinius/documentation

%files devel
%doc LICENSE
%{_includedir}/%{name}

%files doc
%doc LICENSE
%{_libdir}/%{name}/1.2/lib/rubinius/documentation


#-----------------------------------------------------------------------------
%changelog
* Sat Jul 30 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.4-1%{?dist}
- New upstream version

* Fri Mar 11 2011 Eric-Olivier Lamey <pakk@96b.it> - 1.2.3-1%{?dist}
- Initial package creation
