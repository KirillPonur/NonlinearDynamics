import os
svg=[]
for file in os.listdir(path='fig\\lect5'):
	if file.endswith('.svg'):
		svg.append(file[0:-4])
		# print(svg)
for file in svg:
	os.system('D:/Inkscape/inkscape --file=fig\\lect5\\'+file+'.svg --export-pdf=fig\\lect5\\'+file+'.pdf --export-latex')