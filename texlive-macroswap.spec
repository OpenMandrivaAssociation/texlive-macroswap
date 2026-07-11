%global tl_name macroswap
%global tl_revision 31498

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Swap the definitions of two LaTeX macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/macroswap
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/macroswap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides simple utility methods to swap the meaning (token
expansion) of two macros by name.

