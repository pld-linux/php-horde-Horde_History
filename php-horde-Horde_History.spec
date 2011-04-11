%define		status		stable
%define		pearname	Horde_History
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - API for tracking the history of an object
Name:		php-horde-Horde_History
Version:	1.0.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	b7cf809e88f969f5d0099ca45e7fa7b3
URL:		http://pear.horde.org/package/Horde_History/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Db < 2.0.0
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Horde_History API provides a way to track changes on arbitrary
pieces of data in Horde applications.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/History.php
%{php_pear_dir}/Horde/History
%{php_pear_dir}/data/Horde_History
