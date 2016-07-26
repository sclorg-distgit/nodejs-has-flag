%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global npm_name has-flag

Summary:       Check if argv has a specific flag
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.0.0
Release:       3%{?dist}
License:       MIT
URL:           https://github.com/sindresorhus/has-flag
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Check if argv has a specific flag

Correctly stops looking after an -- argument terminator.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%files
%{!?_licensedir:%global license %doc}
%doc license readme.md
%{nodejs_sitelib}/%{npm_name}

%changelog
* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Enable find provides and requires macro

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 1.0.0-1
- Initial package