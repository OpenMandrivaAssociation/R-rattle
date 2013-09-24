%global packname  rattle
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          2.6.26
Release:          1
Summary:          Graphical user interface for data mining in R
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rattle_2.6.26.tar.gz
Requires:         R-RGtk2 R-pmml R-bitops R-colorspace R-ada R-amap R-arules
Requires:         R-arulesViz R-biclust R-cairoDevice R-cba R-descr R-doBy
Requires:         R-e1071 R-ellipse R-fEcofin R-fBasics R-foreign R-fpc
Requires:         R-gdata R-gplots R-graph R-grid R-gtools R-gWidgetsRGtk2
Requires:         R-Hmisc R-kernlab R-latticist R-Matrix R-methods R-mice
Requires:         R-network R-nnet R-odfWeave R-party R-playwith R-psych
Requires:         R-randomForest R-RBGL R-RColorBrewer R-reshape R-rggobi
Requires:         R-RGtk2Extras R-ROCR R-RODBC R-rpart R-rpart.plot
Requires:         R-RSvgDevice R-siatclust R-survival R-timeDate
Requires:         R-verification R-XML R-pkgDepTools R-Rgraphviz
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-RGtk2 R-pmml R-bitops R-colorspace R-ada R-amap R-arules
BuildRequires:    R-arulesViz R-biclust R-cairoDevice R-cba R-descr R-doBy
BuildRequires:    R-e1071 R-ellipse R-fEcofin R-fBasics R-foreign R-fpc
BuildRequires:    R-gdata R-gplots R-graph R-grid R-gtools R-gWidgetsRGtk2
BuildRequires:    R-Hmisc R-kernlab R-latticist R-Matrix R-methods R-mice
BuildRequires:    R-network R-nnet R-odfWeave R-party R-playwith R-psych
BuildRequires:    R-randomForest R-RBGL R-RColorBrewer R-reshape R-rggobi
BuildRequires:    R-RGtk2Extras R-ROCR R-RODBC R-rpart R-rpart.plot
BuildRequires:    R-RSvgDevice R-siatclust R-survival R-timeDate
BuildRequires:    R-verification R-XML R-pkgDepTools R-Rgraphviz
BuildRequires:    x11-server-xvfb

%description
Rattle (the R Analytic Tool To Learn Easily) provides a Gnome (RGtk2)
based interface to R functionality for data mining.  The aim is to provide
a simple and intuitive interface that allows a user to quickly load data
from a CSV file (or via ODBC), transform and explore the data, build and
evaluate models, and export models as PMML (predictive modelling markup
language) or as scores. All of this with knowing little about R. All R
commands are logged and commented through the log tab. Thus they are
available to the user as a script file or as an aide for the user to learn
R or to copy-and-paste directly into R itself.  Rattle also exports a
number of utility functions and the graphical user interface, invoked as
rattle(), does not need to be run to deploy these.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
rm -f %{buildroot}%{rlibdir}/%{packname}/.Rhistory

%check
xvfb-run %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/ChangeLog
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/INSTALL
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/arff
%{rlibdir}/%{packname}/csv
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/odt
%{rlibdir}/%{packname}/po

