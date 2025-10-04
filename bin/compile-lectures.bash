#!/bin/bash
# compile latex lectures using presentation / gapped handout / final handout

TEX="/Library/TeX/texbin/pdflatex -interaction=nonstopmode"

if [[ $# -ne 1 ]]
then
   echo "Enter tex-file name as argument"
   exit 1
fi

FILE=$1
FROOT=${FILE/.tex/}

sed -e 's/%,handout/,handout/' -e 's/%SED_OPTIONS/\\setbeamercolor{background canvas}{bg=white}\n\\setbeamertemplate{blocks}[rounded]/' $FROOT.tex > ${FROOT}_handout.tex || exit 1
sed 's/\\newcommand{\\ho}{|handout:0}/\\newcommand{\\ho}{}/' ${FROOT}_handout.tex > ${FROOT}_final.tex || exit 1

$TEX ${FROOT}.tex
$TEX ${FROOT}_handout.tex
$TEX ${FROOT}.tex
$TEX ${FROOT}_final.tex
$TEX ${FROOT}_handout.tex
$TEX ${FROOT}_final.tex

rm -v ${FROOT}_*.[a-o,q-z]??
