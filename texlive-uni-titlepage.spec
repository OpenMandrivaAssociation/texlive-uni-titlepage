Name:		texlive-uni-titlepage
Version:	64306
Release:	1
Summary:	Universal titlepages with configuration options and predefined styles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uni-titlepage
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-titlepage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-titlepage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-titlepage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Creation of title pages is something most authors should not
have to do. But reality is not perfect, so a lot of authors
have to do it. This package not only provides several pages for
the title instead of only one -- at least five are typical for
a thesis! --, it also provides a bunch of predefined titlepage
styles with several standard elements, and optionally
additional elements.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uni-titlepage
%{_texmfdistdir}/tex/latex/uni-titlepage
%doc %{_texmfdistdir}/doc/latex/uni-titlepage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
