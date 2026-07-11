%global tl_name uni-wtal-ger
%global tl_revision 31541

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Citation style for literary studies at the University of Wuppertal
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/uni-wtal-ger
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a BibLaTeX citation style based on the author-title
style of biblatex-dw. The citations are optimised for literary studies
in faculty of humanities at the Bergische Universitat Wuppertal.

