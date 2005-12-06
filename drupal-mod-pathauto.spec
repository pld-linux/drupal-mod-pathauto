%define		modname pathauto
Summary:	Drupal Pathauto Module
Summary(pl):	Modu³ Pathauto dla Drupala
Name:		drupal-mod-%{modname}
Version:	4.6.0
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://drupal.org/files/projects/%{modname}-%{version}.tar.gz
# Source0-md5:	87d92073546ce9f0e95960a454d84914
URL:		http://drupal.org/node/17345
Requires:	drupal >= 4.6.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules

%description
The pathauto module automatically generates path aliases for various
kinds of content (nodes, categories, users) when no explicit alias is
provided by the user.

%description -l pl
Modu³ pathauto automatycznie generuje aliasy ¶cie¿ek dla ró¿nych
rodzajów tre¶ci (wêz³ów, kategorii, u¿ytkowników), kiedy u¿ytkownik
nie zapewni aliasu wprost.

%prep
%setup -q -n %{modname}
rm -f LICENSE.txt # GPL v2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}
install *.module *.inc $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt contrib/
%{_moddir}/*.module
%{_moddir}/*.inc
