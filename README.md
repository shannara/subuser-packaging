# subuser-packaging
Stuff for packaging subuser to CentOS/RHEL, and Debian

For CentOS/RHEL package, Shann Signing Key
```
pub  2048R/12EC4983 2016-03-24 Stanislas Leduc (shann) <stanislas.leduc@mailoo.org>
 Key fingerprint = 9ACA E5D6 AC5F 390F 4EB1  3955 6217 44A2 12EC 4983
```

System Requirements
--------------------

 * CentOS 7 x64
 
 * SCL enable

 * SELINUX Disable or Permissive mode (investigate to use with Enforcing) 

Installation
------------

1. Install Software Collection
```
 # yum install centos-release-scl
```

2. Install subuser

Download version you should from el7/rpms folder (for now only git version 0.5.4-20160324git in available).

```
 # yum localinstall path/to/rh-python34-subuser-xxx.el7.centos.x86_64.rpm
```

3. Add your user to dockerroot group
```
 # usermod -aG dockerroot {user}
```

4. Run docker with dockerroot group (in future package include in post installation)

Edit ``/etc/sysconfig/docker`` and add "-G dockerroot" to OPTIONS line.
```
before
OPTIONS='--selinux-enabled'
after
OPTIONS='--selinux-enabled -G dockerroot'
```

5. Start Docker daemon

Rerun command with replace 'start' with 'enable' to run docker at boot. 
```
 # systemctl start docker
```

6. Update path
```
 $ source /etc/profile
```

Now play with subuser, you invit to visit http://subuser.org/tutorial-use.html for quickstart guide.
