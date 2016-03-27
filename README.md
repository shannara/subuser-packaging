# subuser-packaging
Stuff for packaging subuser to CentOS/RHEL, and Debian

For CentOS/RHEL package, Shann Signing Key
```
pub  2048R/12EC4983 2016-03-24 Stanislas Leduc (shann) <stanislas.leduc@mailoo.org>
 Key fingerprint = 9ACA E5D6 AC5F 390F 4EB1  3955 6217 44A2 12EC 4983
```

System Requirements
--------------------

 * CentOS or RHEL 7 or Debian 8 x64 (not support Fedora for moment)
 * Softwares Collections enable
 * SELINUX Disable or Permissive mode (investigate to use with Enforcing) 

Installation
------------
* CentOS/RHEL
0. Install Software Collection
```
 On CentOS
 # yum install centos-release-scl
 On RHEL
 # subscription-manager repos --enable rhel-7-server-optional-rpms
 # yum-config-manager --enable rhel-server-rhscl-7-rpms
```

1. Install subuser

Download version you should from el7/rpms folder (for now only git version 0.5.4-20160324git in available).

```
 # yum localinstall path/to/rh-python34-subuser-xxx.el7.centos.x86_64.rpm
```


* Debian
1. Install subuser

Download version you should from jessie/deb folder (0.5.5 is latest version).
For moment, i not create repository but this does not delay. 
````
 # dpkg -i path/to/subsuser_xxx-1_amd64.deb
 Dpkg can't resolv dependencies you need to run apt-get -f install for fetch them.
 # apt-get -f install
````

Post Installation
-----------------

1. Add your user to docker group
```
dockerroot for CentOS/RHEL
 # usermod -aG docker {user}
```

2. For CentOS/RHEL, run docker with dockerroot group (in future include in post installation)

Edit ``/etc/sysconfig/docker`` and add "-G dockerroot" to OPTIONS line.
```
before
OPTIONS='--selinux-enabled'
after
OPTIONS='--selinux-enabled -G dockerroot'
```
3. Start Docker daemon

Rerun command with replace 'start' with 'enable' to run docker at boot. 
```
 # systemctl start docker
```

4. Update path
```
 $ source /etc/profile
```

Now play with subuser, you invit to visit http://subuser.org/tutorial-use.html for quickstart guide.

