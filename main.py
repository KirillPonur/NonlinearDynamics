import os
svg=[]
for file in os.listdir(path='fig'):
	if file.endswith('.svg'):
		svg.append(file[0:-4])
		# print(svg)
for file in svg:
	os.system('D:/Inkscape/inkscape --file=fig/'+file+'.svg --export-pdf=fig/'+file+'.pdf --export-latex')