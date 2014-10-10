%define upstream_name 	 XML-Writer-Simple%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Module for writing XML documents
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/%{upstream_name}
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::DTDParser)
BuildRequires:	perl(XML::DT)
BuildArch:	noarch

%description
XML-Writer-Simple is a simple Perl module to write XML. It takes some
ideas from CGI and applies them for the XML World.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML/Writer*
%{_mandir}/*/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 654384
- update to new version 0.07

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 401814
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 370251
- update to new version 0.05

* Tue Feb 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 341227
- update to new version 0.04

* Tue Feb 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 339102
- update to new version 0.03

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
+ Revision: 338671
- update to new version 0.02

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.01-3mdv2009.0
+ Revision: 242292
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jun 14 2007 Funda Wang <fwang@mandriva.org> 0.01-1mdv2008.0
+ Revision: 39226
- Add more buildrequires
- First package for Mandriva
- Create perl-XML-Writer-Simple



