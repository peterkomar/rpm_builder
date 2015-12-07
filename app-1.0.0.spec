Name:           <name>
Version:        <version>
Release:        1
License:        GPL
Summary:
Url:
Vendor:         Peter Komar
Group:
Source:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description

%prep
%setup -q

%build
make %{?_smp_mflags}

%install

%post

%postun

%files
%defattr(-,root,root)

%changelog
* Thu Dec 2 2015 Peter Komar <peter0komar@gmail.com>
- Built app