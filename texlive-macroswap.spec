# revision 31498
# category Package
# catalog-ctan /macros/latex/contrib/macroswap
# catalog-date 2013-08-21 23:10:13 +0200
# catalog-license lppl1.2
# catalog-version 1.1
Name:		texlive-macroswap
Version:	1.1
Release:	9
Summary:	Swap the definitions of two LaTeX macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/macroswap
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides simple utility methods to swap the meaning
(token expansion) of two macros by name.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/macroswap/macroswap.sty
%doc %{_texmfdistdir}/doc/latex/macroswap/Makefile
%doc %{_texmfdistdir}/doc/latex/macroswap/README
%doc %{_texmfdistdir}/doc/latex/macroswap/macroswap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/macroswap/macroswap.dtx
%doc %{_texmfdistdir}/source/latex/macroswap/macroswap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
