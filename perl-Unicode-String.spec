%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	String
Summary:	Unicode::String perl module
Summary(pl):	Modu³ perla Unicode::String
Name:		perl-Unicode-String
Version:	2.06
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-MIME-Base64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::String perl module.

%description -l pl
Modu³ perla Unicode::String.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Unicode/CharName.pm
%{perl_sitearch}/Unicode/String.pm
%dir %{perl_sitearch}/auto/Unicode/String
%{perl_sitearch}/auto/Unicode/String/String.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/String/String.so
%{_mandir}/man3/*
