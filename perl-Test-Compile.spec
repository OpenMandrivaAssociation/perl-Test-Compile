%define upstream_name    Test-Compile

Name:		perl-%{upstream_name}
Version:	3.1.0
Release:	1

Summary:	Check whether Perl module files compile correctly

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-v%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(UNIVERSAL::require)
BuildArch:	noarch

%description
Check Perl module files for errors or warnings in a test file.

%prep
%autosetup -p1 -n %{upstream_name}-v%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
