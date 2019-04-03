#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-contextlib2
Version  : 0.5.5
Release  : 47
URL      : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Source0  : http://pypi.debian.net/contextlib2/contextlib2-0.5.5.tar.gz
Summary  : Backports and enhancements for the contextlib module
Group    : Development/Tools
License  : Python-2.0
Requires: deprecated-contextlib2-license = %{version}-%{release}
Requires: deprecated-contextlib2-python = %{version}-%{release}
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : linecache2-legacypython
BuildRequires : six
BuildRequires : six-legacypython
BuildRequires : traceback2-legacypython
BuildRequires : unittest2-legacypython

%description
.. image:: https://jazzband.co/static/img/badge.svg
:target: https://jazzband.co/
:alt: Jazzband

%package legacypython
Summary: legacypython components for the deprecated-contextlib2 package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-contextlib2 package.


%package license
Summary: license components for the deprecated-contextlib2 package.
Group: Default

%description license
license components for the deprecated-contextlib2 package.


%package python
Summary: python components for the deprecated-contextlib2 package.
Group: Default

%description python
python components for the deprecated-contextlib2 package.


%prep
%setup -q -n contextlib2-0.5.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554307117
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 test_contextlib2.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-contextlib2
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/deprecated-contextlib2/LICENSE.txt
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-contextlib2/LICENSE.txt

%files python
%defattr(-,root,root,-)
