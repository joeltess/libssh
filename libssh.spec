%define lib_major       2
%define lib_name_orig   %mklibname libssh
%define lib_name        %{lib_name_orig}%{lib_major}

Name:           libssh
Version:        0.20
Release:        %mkrel 2
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
Provides:       %{lib_name_orig} = %{epoch}:%{version}-%{release}
Provides:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name}
The ssh library was designed to be used by programmers needing a working
SSH implementation by the mean of a library. The complete control of the
client is made by the programmer. With libssh, you can remotely execute
programs, transfer files, use a secure and transparent tunnel for your
remote programs. With its Secure FTP implementation, you can play with
remote files easily, without third-party programs others than libcrypto
(from openssl).

%package -n %{lib_name}-devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       ssh-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-devel
This package contains the development files for %{name}.

%package -n %{lib_name}-static-devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-static-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-static-devel = %{epoch}:%{version}-%{release}
Provides:       ssh-static-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-static-devel
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

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(0644,root,root,0755)
%{_includedir}/%{name}
%defattr(-,root,root,0755)
%{_libdir}/*.la
%{_libdir}/*.so

%files -n %{lib_name}-static-devel
%defattr(-,root,root,0755)
%{_libdir}/*.a
