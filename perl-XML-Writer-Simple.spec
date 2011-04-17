%define upstream_name 	 XML-Writer-Simple
%define upstream_version 0.07

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary:	module for writing XML documents
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/%{upstream_name}
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-DTDParser
BuildRequires:	perl-XML-DT
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
XML-Writer-Simple is a simple Perl module to write XML. It takes some
ideas from CGI and applies them for the XML World.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
