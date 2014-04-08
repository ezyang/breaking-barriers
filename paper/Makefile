paper.pdf:
	#texwrapper -l --format pdflatex -b paper.tex
	latexmk -pdf -latexoption=-halt-on-error \
                -latexoption=-file-line-error \
                -latexoption=-synctex=1 paper.tex \
		&& touch $*.dvi || ! rm -f $@

.PHONY: paper.pdf

.PHONY: clean
clean:
	rm -f paper.pdf *.aux *.fdb_latexmk *.log \
		*~ *.dvi *.vrb *.nav *.snm texput.* *.synctex.gz
	latexmk -C paper.tex
