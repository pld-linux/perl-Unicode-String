%include	/usr/lib/rpm/macros.perl
Summary:	Unicode-String perl module
Summary(pl):	Modu³ perla Unicode-String
Name:		perl-Unicode-String
Version:	2.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/Unicode-String-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-MIME-Base64
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Unicode-String perl module.

%description -l pl
Modu³ perla Unicode-String.

%prep
%setup -q -n Unicode-String-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Unicode/String/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Unicode/String
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitearch}/Unicode/CharName.pm
%{perl_sitearch}/Unicode/String.pm

%dir %{perl_sitearch}/auto/Unicode/String
%{perl_sitearch}/auto/Unicode/String/.packlist
%{perl_sitearch}/auto/Unicode/String/String.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/String/String.so

%{_mandir}/man3/*
