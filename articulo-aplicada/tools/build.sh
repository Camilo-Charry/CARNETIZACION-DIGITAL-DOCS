#!/bin/sh

# Add TeX Live to PATH
PATH="/opt/texlive/bin:$PATH"
export PATH

mkdir -p build

echo "[build] Compiling IEEE"
latexmk -silent -file-line-error -outdir=build -xelatex main_ieee.tex

echo "[build] Compiling ACM"
latexmk -silent -file-line-error -outdir=build -bibtex -xelatex main_acm.tex

echo "[build] Compiling APA7"
latexmk -silent -file-line-error -outdir=build -xelatex main_apa7.tex

echo "[build] PDFs available in build/"
