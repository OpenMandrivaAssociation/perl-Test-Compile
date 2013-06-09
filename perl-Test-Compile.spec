%define upstream_name    Test-Compile
%define upstream_version 0.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Check whether Perl module files compile correctly
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Devel::CheckOS)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Check Perl module files for errors or warnings in a test file.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2011.0
+ Revision: 655226
- rebuild for updated spec-helper

* Wed Mar 03 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2011.0
+ Revision: 513798
- update to 0.13

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 504492
- update to 0.12

* Wed Dec 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 475396
- update to 0.11

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.1
+ Revision: 460771
- update to 0.10

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 401604
- rebuild using %%perl_convert_version
- fixed license field

* Tue Jan 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.08-1mdv2009.1
+ Revision: 329067
- import perl-Test-Compile


* Tue Jan 13 2009 cpan2dist 0.08-1mdv
- initial mdv release, generated with cpan2dist

