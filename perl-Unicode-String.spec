#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	String
Summary:	Unicode::String perl module
Summary(pl):	Modu³ perla Unicode::String
Name:		perl-Unicode-String
Version:	2.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d3658d0d1adbf69361771244ac88b237
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-MIME-Base64 >= 2.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::String Perl module - String of Unicode characters
(UCS2/UTF16).

%description -l pl
Modu³ Perla Unicode::String - klasa ci±gu unikodowych znaków
(UCS2/UTF16).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Unicode/CharName.pm
%{perl_vendorarch}/Unicode/String.pm
%dir %{perl_vendorarch}/auto/Unicode/String
%{perl_vendorarch}/auto/Unicode/String/String.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/String/String.so
%{_mandir}/man3/*
