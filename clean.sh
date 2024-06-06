#!/bin/bash

echo "Cleaning workspace..."

rm -rf **/*.acn
rm -rf **/*.aux
rm -rf **/*.glo
rm -rf **/*.glsdefs
rm -rf **/*.idx
rm -rf **/*.ilg
rm -rf **/*.ind
rm -rf **/*.ist
rm -rf **/*.lof
rm -rf **/*.log
rm -rf **/*.lot
rm -rf **/*.out
rm -rf **/*.pdf
rm -rf **/*.toc
rm -rf **/*.bbl
rm -rf **/*.blg
rm -rf **/*.acr
rm -rf **/*.alg
rm -rf **/*.glg
rm -rf **/*.gls
rm -f *.pdf

echo "Done."