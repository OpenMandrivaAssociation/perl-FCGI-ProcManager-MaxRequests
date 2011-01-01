%define upstream_name    FCGI-ProcManager-MaxRequests
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Restrict max number of requests by each child
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/FCGI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FCGI::ProcManager)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
FCGI-ProcManager-MaxRequests is a extension of FCGI-ProcManager that allow
restrict fastcgi processes to process only limiting number of requests.
This may help avoid growing memory usage and compensate memory leaks.

This module subclass the FCGI::ProcManager manpage. After server process
max_requests number of requests, it simple exit, and manager starts another
server process. Maximum number of requests can be set from PM_MAX_REQUESTS
environment variable, max_requests - constructor argument and max_requests
accessor.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


