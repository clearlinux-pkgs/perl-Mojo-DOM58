#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojo-DOM58
Version  : 3.001
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-3.001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-DOM58-3.001.tar.gz
Summary  : 'Minimalistic HTML/XML DOM parser with CSS selectors'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojo-DOM58-license = %{version}-%{release}
Requires: perl-Mojo-DOM58-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Mojo::DOM58 - Minimalistic HTML/XML DOM parser with CSS selectors
SYNOPSIS
use Mojo::DOM58;

# Parse
my $dom = Mojo::DOM58->new('<div><p id="a">Test</p><p id="b">123</p></div>');

# Find
say $dom->at('#b')->text;
say $dom->find('p')->map('text')->join("\n");
say $dom->find('[id]')->map(attr => 'id')->join("\n");

# Iterate
$dom->find('p[id]')->reverse->each(sub { say $_->{id} });

# Loop
for my $e ($dom->find('p[id]')->each) {
say $e->{id}, ':', $e->text;
}

# Modify
$dom->find('div p')->last->append('<p id="c">456</p>');
$dom->at('#c')->prepend($dom->new_tag('p', id => 'd', '789'));
$dom->find(':not(p)')->map('strip');

# Render
say "$dom";

%package dev
Summary: dev components for the perl-Mojo-DOM58 package.
Group: Development
Provides: perl-Mojo-DOM58-devel = %{version}-%{release}
Requires: perl-Mojo-DOM58 = %{version}-%{release}

%description dev
dev components for the perl-Mojo-DOM58 package.


%package license
Summary: license components for the perl-Mojo-DOM58 package.
Group: Default

%description license
license components for the perl-Mojo-DOM58 package.


%package perl
Summary: perl components for the perl-Mojo-DOM58 package.
Group: Default
Requires: perl-Mojo-DOM58 = %{version}-%{release}

%description perl
perl components for the perl-Mojo-DOM58 package.


%prep
%setup -q -n Mojo-DOM58-3.001
cd %{_builddir}/Mojo-DOM58-3.001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojo-DOM58
cp %{_builddir}/Mojo-DOM58-3.001/LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojo-DOM58/3c84d6624185a8425697aa6be532533fba83d755
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojo::DOM58.3
/usr/share/man/man3/Mojo::DOM58::Entities.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojo-DOM58/3c84d6624185a8425697aa6be532533fba83d755

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
