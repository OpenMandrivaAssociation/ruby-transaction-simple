%define rname transaction-simple
%define name ruby-%{rname}
%define version 1.3.0
%define release 1mdk

Summary: Transaction::Simple object transactions
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://trans-simple.rubyforge.org/
Source0: %{rname}-%{version}.tar.bz2
License: BSD-like
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby 
BuildRequires: ruby-devel
BuildArch: noarch

%define ruby_libdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')
%define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

%description
Transaction::Simple provides a generic way to add active transaction support
to objects. The transaction methods added by this module will work with most
objects, excluding those that cannot be Marshal-ed (bindings, procedure
objects, IO instances, or singleton objects).

The transactions supported by Transaction::Simple are not backend transaction;
that is, they are not associated with any sort of data store. They are "live"
transactions occurring in memory and in the object itself. This is to allow
"test" changes to be made to an object before making the changes permanent.

%prep
%setup -q -n %{rname}-%{version}

%build

%install
rm -rf %buildroot
DESTDIR=%buildroot ruby install.rb --no-ri --tests --rdoc

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_libdir}/*
%doc Changelog Readme tests doc

