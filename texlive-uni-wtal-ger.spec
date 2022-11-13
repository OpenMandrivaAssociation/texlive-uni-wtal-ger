Name:		texlive-uni-wtal-ger
Epoch:		1
Version:	31541
Release:	1
Summary:	Citation style for literary studies at the University of Wuppertal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/uni-wtal-ger
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a biblatex citation style based on the
author-title style of biblatex-dw. The citations are optimised
for literary studies in faculty of humanities at the Bergische
Universitat Wuppertal.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uni-wtal-ger/uni-wtal-ger.bbx
%{_texmfdistdir}/tex/latex/uni-wtal-ger/uni-wtal-ger.cbx
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/CHANGES
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/LIESMICH
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/README
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/germanistik.bib
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/germanistik.pdf
%doc %{_texmfdistdir}/doc/latex/uni-wtal-ger/germanistik.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
