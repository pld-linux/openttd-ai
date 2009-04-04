#
Summary:	Artificial Intelligence engines for OpenTTD
Name:		openttd-ai
Version:	20090404
Release:	1
License:	Mixed
Group:		X11/Applications/Games
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	98432a3aa955bac7163d648207f42148
URL:		http://www.openttd.com/
Requires:	openttd-data >= 0.7.0-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Artificial Intelligence engines for OpenTTD.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/openttd

cp -r ai $RPM_BUILD_ROOT%{_datadir}/openttd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/openttd/ai/*.tar
%{_datadir}/openttd/ai/library/*.tar
