%include /usr/lib/rpm/macros.perl
%define _name Trashcan
Summary:	Trashcan application for ROX-Filer
Summary(pl):	Kosz na ¶mieci dla ROX-Filera
Name:		rox-%{_name}
Version:	20020408
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.cerias.purdue.edu/homes/zamboni/files/rox/%{_name}.tar.gz
Patch0:		%{name}-use-tmpdir.patch
URL:		http://www.cerias.purdue.edu/homes/zamboni/rox/
BuildRequires:	rpm-perlprov
Requires:	perl-modules
%requires_eq	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%define   _appsdir  %{_libdir}/ROX-apps

%description
A trashcan application for ROX-Filer, originally inspired by
dfm-trashcan.tcl, but rewritten in Perl and now with very different
functionality, and specifically tailored for ROX-Filer.

%description -l pl
Kosz na ¶mieci dla ROX-Filera, zainspirowany przez dfm-trashcan.tcl,
ale przepisany w Perlu. Teraz posiada on ca³kiem inn± funkcjonalno¶æ i
jest dopasowany do ROX-Filera.

%prep
%setup -q -n %{_name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

install App* EmptyTrashIcon.xpm $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_appsdir}/%{_name}/AppRun
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/EmptyTrashIcon.xpm
%{_appsdir}/%{_name}/Help
%attr(777,root,root) %dir %{_appsdir}/%{_name}
