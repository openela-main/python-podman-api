%global modname podman
%global distname podman-api
%global eggname podman_api

# https://github.com/containers/python-podman
%global git0 https://github.com/containers/python-%{modname}
%global commit0 d0a45fea27f3c1b1c481b05e1531adc168f1881e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})


Name: python-%{distname}
Version: 1.2.0
Release: 0.2.git%{shortcommit0}%{?dist}
Summary: Podman API
License: LGPLv2
URL: %{git0}
Source0: %{git0}/archive/%{commit0}/python-%{modname}-%{shortcommit0}.tar.gz
BuildArch: noarch
BuildRequires: python-rpm-macros
BuildRequires: python3-dateutil
BuildRequires: python3-setuptools
Requires: python3-psutil
Provides: python3-%{distname} = %{version}-%{release}

%description 
%{summary}

%prep
%setup -q -n python-%{modname}-%{commit0}

%build
%py3_build

%install
%py3_install

%check

%files
%license LICENSE
%{python3_sitelib}/%{modname}/*
%{python3_sitelib}/%{modname}-*.egg-info/*

%changelog
* Thu Dec 12 2019 Jindrich Novy <jnovy@redhat.com> - 1.2.0-0.2.gitd0a45fe
- revert update to 1.6.0 due to new python3-pbr dependency which
  is not in RHEL
- Related: RHELPLAN-25139

* Wed May 15 2019 Lokesh Mandvekar <lsm5@@redhat.com> - 1.2.0-0.1.gitd0a45fe
- Initial package

