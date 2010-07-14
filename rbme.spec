Summary: RSYNC BACKUP MADE EASY
Name: rbme
Version: 1.6
Release: 1
Source: rbme-%{version}.tar.gz
License: GPL
BuildArchitectures: noarch
Group: System/Archiving
Packager: Schlomo Schapiro <rbme@schlomo.schapiro.org>
Requires: rsync
%if 0%{?suse_version} != 0
Requires: ssh
BuildRequires: ssh
%else
Requires: openssh-clients procmail
BuildRequires: openssh-clients
%endif

URL: http://schapiro.org/schlomo/projects/rbme.php

BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
RSYNC BACKUP MADE EASY is a rsync-based backup solution with integrated backup
disk space management to remove old backups when the disk gets full.

Creates nice reports to serve as daily backup overview.

See the project homepage at http://schapiro.org/schlomo/projects/rbme.php for
more details and examples.

%changelog
* Tue Aug 31 2009 Schlomo Schapiro
- Updated to rbme 1.6
- Fixed RPM dependancy for lockfile (provided by procmail)

* Thu Jun 04 2009 Schlomo Schapiro
- Updated to rbme 1.5
- Fixed RPM dependancies for ssh to work also for non-SUSE distros

* Tue Apr 07 2009 Schlomo Schapiro
- Removed Provides: rbme to build on suse 11.0++
* Tue May 20 2008 Schlomo Schapiro
- Version 1.4
* Thu Jan 03 2008 Schlomo Schapiro
- Version 1.3
* Thu Dec 27 2007 Schlomo Schapiro
- Version 1.2
* Sat Nov 10 2007 Schlomo Schapiro
- Version 1.1
* Tue Sep 12 2007 Schlomo Schapiro
- Initial Release

%prep
test "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / && rm -Rf "$RPM_BUILD_ROOT"
%setup
 
%install
export NO_BRP_STALE_LINK_ERROR=yes # don't fail on missing symlinks on newer SuSE systems
mkdir -p $RPM_BUILD_ROOT/{usr/bin,etc}
cp -a rbme $RPM_BUILD_ROOT/usr/bin
cp -a rbme.conf $RPM_BUILD_ROOT/etc


%files
%defattr(-,root,root)
%doc NEWS README LICENSE
/usr/bin/rbme
%config(noreplace) /etc/rbme.conf
