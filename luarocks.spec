%define luaver 5.1
%define lualibdir %{_libdir}/lua/%{luaver}
%define luapkgdir %{_datadir}/lua/%{luaver}

Name:           luarocks
Version:        2.0.12
Release:        %mkrel 1
Summary:        Deployment and management system for Lua modules

Group:          Development/Other
License:        MIT
URL:            http://www.luarocks.org/
Source0:        http://luaforge.net/frs/download.php/3727/%{name}-%{version}.tar.gz

BuildRequires:  lua >= %{luaver}, lua-devel >= %{luaver}
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
%setup -q -n %{name}-%{version}

for file in COPYING_7z; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done


%build
./configure --prefix=/usr --sysconfdir=%{_sysconfdir}/%{name} --rocks-tree=%{lualibdir} --lua-suffix=%{luaver}
make

%install
make DESTDIR=%{buildroot} install

%files
%{_sysconfdir}/luarocks/config.lua
%{_bindir}/*
%{luapkgdir}/%{name}/*
