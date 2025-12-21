%define luaver 5.4
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           luarocks
Version:        3.12.2
Release:        1
Summary:        Deployment and management system for Lua modules

Group:          Development/Other
License:        MIT
URL:            https://luarocks.org
Source0:        https://luarocks.org/releases/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:   lua >= %{luaver}
BuildRequires:   lua-devel >= %{luaver}

Requires:       lua >= %{luaver}
Requires:       wget

BuildArch:      noarch

%description
LuaRocks allows you to install Lua modules
as self-contained packages called "rocks",
which also contain version dependency information.
This information is used both at install time, so that
when one rock is requested all rocks it depends on are installed
as well, and at run time, so that when a module
is required, the correct version is loaded.

LuaRocks supports both local and remote repositories,
and multiple local rocks trees.

%prep
%autosetup

%build
./configure --prefix=%{_prefix} --lua-version=%{luaver}
make

%install
%makeinstall_std

%files
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/luarocks/config-%{luaver}.lua
%{_bindir}/*
%{luapkgdir}/%{name}/*
