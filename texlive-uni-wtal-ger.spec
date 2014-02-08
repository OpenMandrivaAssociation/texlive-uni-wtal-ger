# revision 22169
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-uni-wtal-ger
Version:	20111104
Release:	3
Summary:	TeXLive uni-wtal-ger package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-ger.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive uni-wtal-ger package.

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


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 757318
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719854
- texlive-uni-wtal-ger
- texlive-uni-wtal-ger
- texlive-uni-wtal-ger
- texlive-uni-wtal-ger

