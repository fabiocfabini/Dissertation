#!/bin/bash

set -xe

cd msc_latex_template

xelatex dissertation.tex
bibtex dissertation.aux
makeindex dissertation
makeglossaries dissertation
xelatex dissertation.tex

cd ..
