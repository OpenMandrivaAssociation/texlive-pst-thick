# revision 16369
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-thick
# catalog-date 2009-12-14 16:47:24 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-thick
Version:	1.0
Release:	3
Summary:	Drawing very thick lines and curves
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-thick
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-thick.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-thick.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-thick.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports drawing of very thick lines and curves in
PSTricks, with various fillings for the body of the lines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-thick/pst-thick.tex
%{_texmfdistdir}/tex/latex/pst-thick/pst-thick.sty
%doc %{_texmfdistdir}/doc/generic/pst-thick/Changes
%doc %{_texmfdistdir}/doc/generic/pst-thick/README
%doc %{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-thick/pst-thick-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-thick/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755484
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719402
- texlive-pst-thick
- texlive-pst-thick
- texlive-pst-thick
- texlive-pst-thick

