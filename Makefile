version=1.0

ScalableKMeansPlusPlus.pdf: ScalableKMeansPlusPlus.tex ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_16_1.png ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_21_0.png ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_24_0.png ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_31_1.png
	pdflatex ScalableKMeansPlusPlus


ScalableKMeansPlusPlus.tex: ScalableKMeansPlusPlus.ipynb
	@ipython nbconvert --to latex ScalableKMeansPlusPlus.ipynb
	@touch ScalableKMeansPlusPlus.tex

ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_16_1.png: ScalableKMeansPlusPlus.ipynb
	@ipython nbconvert --to latex ScalableKMeansPlusPlus.ipynb
	@touch ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_16_1.png

ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_21_0.png: ScalableKMeansPlusPlus.ipynb
	@ipython nbconvert --to latex ScalableKMeansPlusPlus.ipynb
	@touch ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_21_0.png

ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_24_0.png: ScalableKMeansPlusPlus.ipynb
	@ipython nbconvert --to latex ScalableKMeansPlusPlus.ipynb
	@touch ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_24_0.png

ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_31_1.png: ScalableKMeansPlusPlus.ipynb
	@ipython nbconvert --to latex ScalableKMeansPlusPlus.ipynb
	@touch ScalableKMeansPlusPlus_files/ScalableKMeansPlusPlus_31_1.png

.PHONY: all clean

all: ScalableKMeansPlusPlus.pdf

clean:
	@rm -rf ScalableKMeansPlusPlus_files/
	@rm -f *png *aux *log *out
	@echo "cleaned up"