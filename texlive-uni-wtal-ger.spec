# revision 31541
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/uni-wtal-ger
# catalog-date 2013-08-30 07:53:51 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-uni-wtal-ger
Epoch:		1
Version:	0.2
Release:	2
Summary:	Citation style for literary studies at the University of Wuppertal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/uni-wtal-ger
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
