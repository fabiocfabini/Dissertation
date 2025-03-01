#!/bin/bash

cd msc_latex_template

echo "RUNNING: xelatex dissertation.tex"
xelatex dissertation.tex
echo "RUNNING: bibtex dissertation.aux"
bibtex dissertation.aux
echo "RUNNING: makeindex dissertation"
makeindex dissertation
echo "RUNNING: makeglossaries dissertation"
makeglossaries dissertation
echo "RUNNING: xelatex dissertation.tex"
xelatex dissertation.tex

mv dissertation.pdf ..

cd ..
