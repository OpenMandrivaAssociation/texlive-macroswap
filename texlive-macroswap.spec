Name:		texlive-macroswap
Version:	31498
Release:	2
Summary:	Swap the definitions of two LaTeX macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/macroswap
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
