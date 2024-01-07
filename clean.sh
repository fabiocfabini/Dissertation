#!/bin/bash

echo "Cleaning workspace..."

cd msc_latex_template
rm *.tdo *.acn *.aux *.glo *.glsdefs *.idx *.ilg *.ind *.ist *.lof *.log *.lot *.out *.toc *.bbl *.blg *.acr *.alg *.glg *.gls
cd ..
rm dissertation.pdf

echo "Done."