%{!?upstream_version: %global upstream_version %version}
%define upstream_name sensu-puppet


Name:           puppet-sensu
Version:        2.30.1
Release:        2%{?dist}
Summary:        A module to install the Sensu monitoring framework
License:        MIT

URL:            https://github.com/sensu/sensu-puppet

Source0:        https://github.com/sensu/%{upstream_name}/archive/v%{version}.tar.gz

# patches_base=v2.30.1

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
A module to install the Sensu monitoring framework

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/sensu/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/sensu/



%files
%{_datadir}/openstack-puppet/modules/sensu/


%changelog
* Wed Nov 01 2017 Jon Schlueter <jschluet@redhat.com> 2.30.1-2
- convert to real release tarball instead of git-tarball

* Fri Aug 25 2017 Alfredo Moralejo <amoralej@redhat.com> 2.30.1-1.c99f0d2git
- Pike update 2.30.1 (c99f0d261fcf68edbd27706cc391f06a3006c4f5)

