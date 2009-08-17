%define lib_major       3
%define lib_name_orig   %mklibname ssh
%define lib_name        %mklibname ssh %{lib_major}
%define dev_name	%mklibname ssh -d
%define sta_name	%mklibname ssh -d -s

Name: libssh
Version: 0.3.0
Release: %mkrel 1
Epoch: 1
Summary: C library to authenticate in a simple manner to one or more SSH servers
Group: System/Libraries
License: GPL
URL: http://0xbadc0de.be/wiki/doku.php?id=libssh:soc
# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source0: http://0xbadc0de.be/libssh/libssh-781.tar.bz2
Patch0: libssh-781-wchar-literal.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: doxygen
BuildRequires: openssl-devel
BuildRequires: cmake

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
Summary: Main library for %{name}
Group: System/Libraries

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
Summary: Development files for %{name}
Group: System/Libraries
Requires: %{lib_name} = %{epoch}:%{version}-%{release}
Provides: ssh-devel = %{epoch}:%{version}-%{release}
Provides: libssh-devel = %{epoch}:%{version}-%{release}

%description -n %{dev_name}
This package contains the development files for %{name}.

%files -n %{dev_name}
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL README
%{_includedir}/%{name}
%{_libdir}/*.so

#----------------------------------------------------------------

%prep
%setup -q -n %{name}
%patch0 -p0 

%build
%cmake

%make

%install
%makeinstall_std -C build

%clean
rm -rf %buildroot


