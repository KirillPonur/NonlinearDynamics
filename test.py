import os
svg=[]
for file in os.listdir(path='fig'):
	if file.endswith('.svg'):
		svg.append(file)

os.system('D:/Inkscape/inkscape --file=fig/fig1_2.svg --export-pdf=fig/fig1_2.pdf --export-latex')