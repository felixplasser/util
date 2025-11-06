#!/bin/bash

TEX="pdflatex -interaction=nonstopmode"

for FILE in 2?CM*tex
do
    FROOT=${FILE/.tex/}
    echo " *** Compiling $FILE ***"

    sed -e 's/\\printanswers/%\\printanswers/' $FROOT.tex > ${FROOT}_paper.tex || exit 1

    $TEX ${FROOT}_paper.tex
    $TEX ${FROOT}.tex
    $TEX ${FROOT}_paper.tex
    $TEX ${FROOT}.tex

    rm -v ${FROOT}_*.[a-o,q-z]??
    mv ${FROOT}.pdf ${FROOT}_solutions.pdf
done

for FILE in 2?CM*tex
do
    echo " *** Marks for $FILE ***"
    exam_marks.py $FILE
done
