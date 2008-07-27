%define lib_major       2
%define lib_name_orig   %mklibname ssh
%define lib_name        %mklibname ssh %{lib_major}
%define dev_name	%mklibname ssh -d
%define sta_name	%mklibname ssh -d -s

# (Anssi 01/2008)
# Exercise caution when changing package names and provides here.
# There is another more used ssh library called libssh2, we do not
# want to clash with it.

Name:           libssh
Version:        0.20
Release:        %mkrel 6
Epoch:          0
Summary:        C library to authenticate in a simple manner to one or more SSH servers
Group:          System/Libraries
License:        GPL
URL:            http://0xbadc0de.be/wiki/doku.php?id=libssh:soc
# svn checkout svn://svn.berlios.de/libssh/trunk libssh
Source0:        http://0xbadc0de.be/libssh/libssh-132.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  doxygen
BuildRequires:  openssl-devel

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
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name}
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl).

%package -n %{dev_name}
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       ssh-devel = %{epoch}:%{version}-%{release}
Provides:       libssh-devel = %{epoch}:%{version}-%{release}

%description -n %{dev_name}
This package contains the development files for %{name}.

%package -n %{sta_name}
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       libssh-static-devel = %{epoch}:%{version}-%{release}
Provides:       ssh-static-devel = %{epoch}:%{version}-%{release}

%description -n %{sta_name}
This package contains the static development files for %{name}.

%prep
%setup -q -n %{name}
%{_bindir}/autoreconf -i -v --force

%build
%{configure2_5x}
%{make}
%{_bindir}/doxygen

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__perl} -pi -e 's|/usr/lib|%{_libdir}|' %{buildroot}%{_libdir}/*.la

%check
%{make} check

%clean
%{__rm} -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%defattr(-,root,root,-)
%{_libdir}/*.so.%{lib_major}*

%files -n %{dev_name}
%defattr(0644,root,root,0755)
%{_includedir}/%{name}
%defattr(-,root,root,0755)
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %{sta_name}
%defattr(-,root,root,0755)
%{_libdir}/*.a
