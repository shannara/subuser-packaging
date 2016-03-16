%{?scl:%scl_package subuser}
%{!?scl:%global pkg_name %{name}}

Name:       %{?scl_prefix}subuser           
Version:    0.5.3
Release:    1%{?dist}
Summary:    Securing the Linux desktop with Docker.

Group:      Applications/System
BuildRoot:  %{_tmppath}/%{pkg_name}-%{version}-%{release}-root-%(%{__id_u} -n)

License:    LGPLv3
URL:        http://subuser.org
#Source0:    https://github.com/%{name}-security/%{name}/archive/%{version}.tar.gz
Source0:    %{name}-%{version}.tar
Source1:    enablepython34.sh
Source2:    enablesubuser.sh

BuildRequires:  %{?scl_prefix}python-devel
BuildRequires:  %{?scl_prefix}python-sphinx
%{?scl:BuildRequires: %{scl}-build %{scl}-runtime}
%{?scl:Requires: %{scl}-runtime}
Requires: docker >= 1.3
Requires: xorg-x11-xauth

%define _unpackaged_files_terminate_build       0
%define _missing_doc_files_terminate_build      0        
#%define rootdir $RPM_BUILD_ROOT/%{_datarootdir}/%{name}
#%define licensedir $RPM_BUILD_ROOT/%{_datarootdir}/licenses/%{name}
#%define docdir $RPM_BUILD_ROOT/%{_datarootdir}/doc/%{name}

%description
As free software developers we like to share. We surf the web and discover new code.
 We are eager to try it out. We live out an orgy of love and trust, 
 unafraid that some code we cloned from git might be faulty or malicious. 
 We live in the 60s, carefree hippies.

 This is utopia.

 But sharing code isn't safe. Every time we try out some stranger's script we put ourselves at risk.
 Despite the occasional claim that linux is a secure operating system, haphazardly sharing programs is NOT secure.

 Furthermore, the fragmentation of the linux desktop means that packaging work is needlessly repeated.
 Programs that build and run on Fedora must be repackaged for Ubuntu. 
 This takes time away from creating great free open source software.

 Subuser with Docker attacks both problems simultaneously. Docker provides an isolated and consistent 
 environment for your programs to run in. Subuser gives your desktop programs access to the resources 
 they need in order to function normally.


%prep
%setup -q

%build
%{?scl:scl enable %{scl} "}
#cd docs/commands ; %{__python3} ./generate-command-docs.py
#cd ../../logic ; pylint --disable=C0111,C0301,C0103,C0322,C0323,C0324,R0913,R0903,R0904,superfluous-parens,bad-continuation,unused-variable,too-many-branches,too-many-locals,bad-builtin,deprecated-lambda,locally-disabled --indent-string='  ' subuserlib/ > ../docs/developers/pylint.rst
#cd ../docs ; ./developers/restructure-pylint-output
#cd ../docs ; sphinx-build -b html . _build/html
#cd .. ; %{__python3} setup.py build
%{__python3} setup.py build

%{?scl:"}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} "}
%{__python3} setup.py install --skip-build --root %{buildroot}
mkdir -p %{buildroot}/etc/profile.d
cp %{SOURCE1} %{buildroot}/etc/profile.d
cp %{SOURCE2} %{buildroot}/etc/profile.d
%{?scl:"}

pushd %{buildroot}%{python3_sitelib}
popd

#%pre
#/usr/bin/getent group docker || /usr/sbin/groupadd -r docker

#%postun
#/usr/sbin/userdel docker

%clean
rm -rf %{buildroot}


%files 
#%{_datarootdir}/%{name}
#%{_datarootdir}/licenses/%{name}
#%{_datarootdir}/doc/%{name}
%defattr(-,root,root,-)
%{_bindir}/subuser*
%{python3_sitelib}/*
/etc/profile.d/*
%doc

%changelog
* Wed Mar 09 2016 Stanislas LEDUC <stanislas.leduc@mailoo.org> 0.5.3-1
- Packaging 0.5.3
* Sun Feb 28 2016 Stanislas LEDUC <stanislas.leduc@mailoo.org> 0.5.2-1
- Initial package

