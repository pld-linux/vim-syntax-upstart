%define		syntax upstart
Summary:	Vim syntax: Varnish configuation Language
Name:		vim-syntax-%{syntax}
Version:	1.3
Release:	1
License:	GPL v2
Group:		Applications/Editors/Vim
Source0:	http://launchpad.net/upstart/1.x/1.3/+download/upstart-%{version}.tar.gz
# Source0-md5:	7820797b64878c27115fff6a7398a6a9
Patch0:		%{name}-keywords_and_pld.patch
Requires:	vim-rt >= 4:7.2.411
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Vim syntax for Upstart job files.

%prep
%setup -qc
mv upstart-*/contrib/vim/* .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a syntax ftdetect $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*.vim
%{_vimdatadir}/ftdetect/*.vim
