%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name sensu-puppet
%global commit 6d10bae43dbb16ca58e3188cc293de01a622240a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-sensu
Version:        2.1.0
Release:        2%{?alphatag}%{?dist}
Summary:        A module to install the Sensu monitoring framework
License:        MIT

URL:            https://github.com/sensu/sensu-puppet

Source0:        https://github.com/sensu/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

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
* Tue Nov 15 2016 Alfredo Moralejo <amoralej@redhat.com> 2.1.0-2.6d10bae.git
- Newton update 2.1.0 (6d10bae43dbb16ca58e3188cc293de01a622240a)

* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 2.1.0-1.7f60b2c.git
- Newton update 2.1.0 (7f60b2c5f708ed03b7769b69a1e86018db598aa9)


