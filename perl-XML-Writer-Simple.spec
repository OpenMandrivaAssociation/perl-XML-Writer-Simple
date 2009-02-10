%define module 	XML-Writer-Simple
%define version 0.03
%define release %mkrel 1

Summary:	Module for writing XML documents
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License:	GPL or Artistic
URL:		http://search.cpan.org/dist/%{module}
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.gz
BuildRequires:	perl
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-DTDParser
BuildRequires:	perl-XML-DT
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

%description
XML-Writer-Simple is a simple Perl module to write XML. It takes some
ideas from CGI and applies them for the XML World.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/XML/Writer*
%{_mandir}/*/*
