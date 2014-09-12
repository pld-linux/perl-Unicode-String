#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	String
Summary:	Unicode::String perl module
Summary(pl.UTF-8):	Moduł perla Unicode::String
Name:		perl-Unicode-String
Version:	2.09
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Unicode/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	553e68e603723bf7c631f8701ab0d678
URL:		http://search.cpan.org/dist/Unicode-String/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-MIME-Base64 >= 2.00
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::String Perl module - String of Unicode characters
(UCS2/UTF16).

%description -l pl.UTF-8
Moduł Perla Unicode::String - klasa ciągu unikodowych znaków
(UCS2/UTF16).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/String/String.so
%{_mandir}/man3/Unicode::CharName.3pm*
%{_mandir}/man3/Unicode::String.3pm*
