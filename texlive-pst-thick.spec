# revision 16369
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-thick
# catalog-date 2009-12-14 16:47:24 +0100
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-pst-thick
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package supports drawing of very thick lines and curves in
PSTricks, with various fillings for the body of the lines.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
