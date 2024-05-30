%define luaver 5.4
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           luarocks
Version:        2.2.2
Release:        1
Summary:        Deployment and management system for Lua modules

Group:          Development/Other
License:        MIT
URL:            http://www.luarocks.org/
Source0:        http://luaforge.net/frs/download.php/3727/%{name}-%{version}.tar.gz

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
%setup -q

for file in COPYING_7z; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build
./configure --prefix=%{_prefix}
make

%install
%makeinstall_std

%files
%doc COPYING README.md 
%config(noreplace) %{_sysconfdir}/luarocks/config-%{luaver}.lua
%{_bindir}/*
%{luapkgdir}/%{name}/*
