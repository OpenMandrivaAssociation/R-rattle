%define modulename rattle
%define r_library %{_libdir}/R/library

Summary:	Gnome R data mining
Name:		R-cran-%{modulename}
Version:	2.2.91
Release:	%mkrel 6
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://rattle.togaware.com/
Source0:	http://rattle.togaware.com/src/contrib/%{modulename}_%{version}.tar.gz
BuildRequires:	R-base
Requires:	R-base
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Rattle (the R Analytical Tool To Learn Easily) provides a 
simple and logical interface for quick and easy data mining.
It is a new data mining application based on the open source 
and free statistical language R  using the Gnome  graphical 
interface.The aim is to provide an intuitive interface that 
takes you through the basic steps of data mining, as well as 
illustrating the R code that is used to achieve this. Whilst 
the tool itself may be sufficient for all of a user's needs, 
it also provides a stepping stone to more sophisticated 
processing and modelling in R itself, for sophisticated and 
unconstrained data mining.

%prep
%setup -q -c

%build
R CMD build %{modulename}
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{r_library}

# (tpg) install
R CMD INSTALL %{modulename} --library=%{buildroot}/%{r_library}

# (tpg) provided by R-base
rm -rf %{buildroot}/%{r_library}/R.css

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{r_library}/%{modulename}
