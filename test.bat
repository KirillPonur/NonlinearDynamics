1>nul pdflatex.exe -synctex=1 -interaction=nonstopmode %~n0.tex 
pythontex %~n0.tex
1>nul pdflatex.exe -synctex=1 -interaction=nonstopmode %~n0.tex 
start "D:\SumatraPDF\SumatraPDF.exe" %~n0.pdf
