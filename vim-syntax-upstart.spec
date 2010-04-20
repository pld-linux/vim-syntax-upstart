%define		syntax upstart
Summary:	Vim syntax: Varnish configuation Language
Name:		vim-syntax-%{syntax}
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/Editors/Vim
Source0:	http://upstart.ubuntu.com/download/0.6/upstart-0.6.5.tar.gz
# Source0-md5:	f9466bba72b655c2408353b64105853f
Requires:	vim-rt >= 4:7.2.411
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Vim syntax for Upstart job files.

%prep
%setup -q -n %(echo $(basename %{S:0} .tar.gz))

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a contrib/vim/* $RPM_BUILD_ROOT%{_vimdatadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*.vim
%{_vimdatadir}/ftdetect/*.vim
