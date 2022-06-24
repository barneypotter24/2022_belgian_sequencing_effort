rm *.log* *.pdf *.aux *.bbl *.log *.out *.synctex.gz *.blg

pdflatex manuscript.tex
pdflatex manuscript.tex
bibtex manuscript
pdflatex manuscript.tex
