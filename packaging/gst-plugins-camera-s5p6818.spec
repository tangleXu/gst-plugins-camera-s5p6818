Name:    gst-plugins-camera-s5p6818
Version: 0.0.1
Release: 0
License: Apache 2.0
Summary: gstreamer plugin camera
Group: Development/Libraries
Source:  %{name}-%{version}.tar.gz

BuildRequires:  pkgconfig automake autoconf libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:	gstreamer1-devel
BuildRequires:	glibc-devel
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:	gst-plugins-renderer-devel
BuildRequires:	nx-drm-allocator-devel
BuildRequires:	nx-v4l2-devel

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
gstreamer plugin camera

%package devel
Summary: gstreamer plugin camera
Group: Development/Libraries
License: Apache 2.0
Requires: %{name} = %{version}-%{release}

%description devel
gstreamer plugin camera (devel)

%prep
%setup -q

%build
autoreconf -v --install || exit 1
%configure --with-extrapath=%{_prefix} --with-extrapath_lib=%{_libdir} \
	--with-extrapath_include=%{_includedir}
make %{?_smp_mflags}

%postun -p /sbin/ldconfig

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

find %{buildroot} -type f -name "*.la" -delete

%files
%{_libdir}/libgstnxcamerasrc.so
%{_libdir}/libgstnxcamerasrc.so.*

%files devel
%{_includedir}/gstcamerasrc.h