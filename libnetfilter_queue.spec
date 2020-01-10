%define libnfnetlink 1.0.1

Name: libnetfilter_queue
Version: 1.0.2
Release: 1%{?dist}
Summary: Netfilter queue userspace library
Group: System Environment/Libraries
# Most files say GPLv2+, one says v2 only.
License: GPLv2
URL: http://netfilter.org
Source0: http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2

BuildRequires: pkgconfig, kernel-headers
BuildRequires: libnfnetlink-devel >= %{libnfnetlink}, libmnl-devel >= 1.0.3

%description
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue. 

%package devel
Summary: Netfilter queue userspace library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, pkgconfig
Requires: libnfnetlink-devel >= %{libnfnetlink}, kernel-headers

%description devel
libnetfilter_queue is a userspace library providing an API to packets that have
been queued by the kernel packet filter. It is is part of a system that
deprecates the old ip_queue / libipq mechanism.

libnetfilter_queue has been previously known as libnfnetlink_queue.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static --disable-rpath
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete
rm %{buildroot}/%{_includedir}/internal.h

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Aug 28 2014 Pavel Šimerda <psimerda@redhat.com> - 1.0.2-1
- Resolves: #1058375 - provide libnetfilter_queue package for RHEL 7.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 17 2012 Paul P. Komkoff Jr <i@stingr.net> - 1.0.1-1
- upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug  4 2010 Paul P. Komkoff Jr <i@stingr.net> - 1.0.0-1
- new upstream version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Mar  7 2009 Paul P. Komkoff Jr <i@stingr.net> - 0.0.17-1
- upstream update

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.16-3
- fix patch/patch0
- depend on specific libnfnetlink version

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.16-2
- fix license tag

* Wed Jul 16 2008 Paul P. Komkoff Jr <i@stingr.net> - 0.0.16-1
- new upstream version

* Fri Feb 22 2008 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-4
- use system header instead of bundled one

* Fri Feb 22 2008 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-3
- fix compilation with newer glibc/headers/whatever

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.15-2
- Autorebuild for GCC 4.3

* Tue Sep 18 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.15-1
- new upstream version

* Mon Mar 26 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-3
- own some directories

* Mon Mar 19 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-2
- fix source url
- add pkgconfig to -devel Requires

* Sat Mar 17 2007 Paul P Komkoff Jr <i@stingr.net> - 0.0.13-1
- Preparing for submission to fedora extras
