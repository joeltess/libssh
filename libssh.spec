%define lib_major       4
%define lib_name_orig   %mklibname ssh
%define lib_name        %mklibname ssh %{lib_major}
%define dev_name	%mklibname ssh -d

Summary:	C library to authenticate in a simple manner to one or more SSH servers
Name:		libssh
Version:	0.4.5
Release:	%mkrel 1
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
