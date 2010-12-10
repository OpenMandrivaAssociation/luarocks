%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           luarocks
Version:        1.0
Release:        %mkrel 3
Summary:        Deployment and management system for Lua modules

Group:          Development/Other
License:        MIT
URL:            http://www.luarocks.org/
Source0:        http://luaforge.net/frs/download.php/3727/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
Requires:       lua >= %{luaver}
Requires:       wget

BuildArch:      noarch

%description
LuaRocks allows you to install Lua modules as self-contained packages called "rocks",
which also contain version dependency information. This information is used both at
install time, so that when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module is required, the correct version is loaded.

LuaRocks supports both local and remote repositories, and multiple local rocks trees.


%prep
%setup -q -n %{name}-%{version}


%build
./configure --prefix=/usr --sysconfdir=%{_sysconfdir}/%{name} --rocks-tree=%{lualibdir} --scripts-dir=%{luapkgdir} --lua-suffix=%{luaver}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_sysconfdir}/luarocks/config.lua
%{_bindir}/*
%{luapkgdir}/%{name}/*
