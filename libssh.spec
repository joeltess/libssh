%define lib_major       4
%define lib_name_orig   %mklibname ssh
%define lib_name        %mklibname ssh %{lib_major}
%define dev_name	%mklibname ssh -d

Summary:	C library to authenticate in a simple manner to one or more SSH servers
Name:		libssh
Version:	0.5.0
Release:	%mkrel 4
Epoch:		1
Group:		System/Libraries
License:	LGPLv2.1+
URL:		http://www.libssh.org
# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source0:	http://www.libssh.org/files/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	openssl-devel
BuildRequires:	cmake
BuildRequires:	zlib-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	libpcap-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The ssh library was designed to be used by programmers needing a working 
SSH implementation by the mean of a library. The complete control of the 
client is made by the programmer. With libssh, you can remotely execute 
programs, transfer files, use a secure and transparent tunnel for your 
remote programs. With its Secure FTP implementation, you can play with 
remote files easily, without third-party programs others than libcrypto 
(from openssl). libssh features :

    * Full C library functions for manipulating a client-side SSH
      connection
    * Lesser GPL licensing -SSH2 protocol compliant
    * Fully configurable sessions
    * Support for AES-128,AES-192,AES-256,blowfish, in cbc mode
    * Use multiple SSH connections in a same process, at same time
    * Use multiple channels in the same connection
    * Thread safety when using different sessions at same time
    * Basic but correct SFTP implementation (secure file transfer)
    * RSA and DSS server public key supported
    * Compression support (with zlib)
    * Public key (RSA and DSS), password and keyboard-interactive
      authentication
    * Complete documentation about its API
    * Runs and tested under amd64, x86, arm, sparc32, ppc under Linux,
      BSD, MacosX and Solaris
    * A developer listening to you
    * It's free (LGPL)!


%package -n %{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{lib_name}
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl).

%files -n %{lib_name}
%defattr(-,root,root,-)
%{_libdir}/*.so.%{lib_major}*

#-----------------------------------------------------------

%package -n %{dev_name}
Summary:	Development files for %{name}
Group:		System/Libraries
Requires:	%{lib_name} = %{epoch}:%{version}-%{release}
Provides:	ssh-devel = %{epoch}:%{version}-%{release}
Provides:	libssh-devel = %{epoch}:%{version}-%{release}

%description -n %{dev_name}
This package contains the development files for %{name}.

%files -n %{dev_name}
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DWITH_GCRYPT=ON -DWITH_PCAP=ON
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}


%changelog
* Wed Jun 01 2011 Funda Wang <fwang@mandriva.org> 1:0.5.0-1mdv2011.0
+ Revision: 682331
- new version 0.5.0

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.7-2
+ Revision: 661528
- mass rebuild

* Sun Jan 02 2011 Lev Givon <lev@mandriva.org> 1:0.4.7-1mdv2011.0
+ Revision: 627541
- Update to 0.4.7.

* Tue Sep 07 2010 Funda Wang <fwang@mandriva.org> 1:0.4.6-1mdv2011.0
+ Revision: 576421
- update to new version 0.4.6

  + Matthew Dawkins <mattydaw@mandriva.org>
    - new version 0.4.5

* Sat Jul 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.4-2mdv2011.0
+ Revision: 554541
- spec file clean
  build against libgcrypt and libpcap

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1:0.4.4-1mdv2011.0
+ Revision: 553704
- update to new version 0.4.4

* Thu Apr 08 2010 Eugeni Dodonov <eugeni@mandriva.com> 1:0.4.2-2mdv2010.1
+ Revision: 533131
- Rebuild for new openssl

* Mon Mar 22 2010 Emmanuel Andry <eandry@mandriva.org> 1:0.4.2-1mdv2010.1
+ Revision: 526614
- New version 0.4.2
- fix license

* Mon Feb 15 2010 Frederik Himpe <fhimpe@mandriva.org> 1:0.4.1-1mdv2010.1
+ Revision: 506355
- update to new version 0.4.1

* Fri Dec 11 2009 Funda Wang <fwang@mandriva.org> 1:0.4.0-1mdv2010.1
+ Revision: 476387
- new version 0.4.0

* Thu Dec 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.3.92-1mdv2010.1
+ Revision: 472802
- Update to version 0.3.92

* Wed Sep 16 2009 Frederik Himpe <fhimpe@mandriva.org> 1:0.3.4-2mdv2010.0
+ Revision: 443612
- Really update to new version 0.3.4
- Remove literal patch: integrated upstream
- update to new version 0.3.4

* Wed Aug 19 2009 Frederik Himpe <fhimpe@mandriva.org> 1:0.3.3-1mdv2010.0
+ Revision: 418098
- update to new version 0.3.3

* Mon Aug 17 2009 Helio Chissini de Castro <helio@mandriva.com> 1:0.3.0-1mdv2010.0
+ Revision: 417281
- Update to current build cmake based. new version is required to next sftp/ftp
  kioslave in kde
- Add literal wstring patch

* Sun Jul 27 2008 Thierry Vignaud <tv@mandriva.org> 0:0.20-6mdv2009.0
+ Revision: 250585
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sat Jan 19 2008 Anssi Hannula <anssi@mandriva.org> 0:0.20-4mdv2008.1
+ Revision: 155080
- fix libification

* Fri Jan 18 2008 David Walluck <walluck@mandriva.org> 0:0.20-3mdv2008.1
+ Revision: 154528
- fix libname

* Tue Jan 15 2008 David Walluck <walluck@mandriva.org> 0:0.20-2mdv2008.1
+ Revision: 152023
- SVN r132

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 02 2007 David Walluck <walluck@mandriva.org> 0:0.20-1mdv2008.0
+ Revision: 20578
- change version to 0.20 from 0.2 so that it's greater than 0.11


* Mon Oct 16 2006 David Walluck <walluck@mandriva.org> 0.2-0.20060921.2mdv2006.0
+ Revision: 65309
+ Status: not released
- bump release

* Sun Oct 15 2006 David Walluck <walluck@mandriva.org> 0:0.2-0.20060921.1mdv2007.1
+ Revision: 64924
- Import libssh

* Thu Sep 21 2006 David Walluck <walluck@mandriva.org> 0:0.2-0.20060901.1mdv2007.0
- release

