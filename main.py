import os
svg=[]
lections = ['lect'+str(i) for i in range(11,16)]
for lect in lections:
	for file in os.listdir(path='fig\\' +lect):
		if file.endswith('.svg'):
			svg.append(file[0:-4])
			# print(svg)
	for file in svg:
		# os.system('D:/Inkscape/inkscape --file=fig\\'+lect+'\\'+file+'.svg --export-pdf=fig\\'
		# 			+	lect+'\\'+file+'.pdf --export-latex')

		os.system('D:/Inkscape/inkscape --file=fig\\'+lect+'\\'+file+'.svg  --export-dpi=300 --export-png=fig\\' 
				+	lect+'\\'+file+'.png')


# # lections = ['lect'+str(i) for i in range(1,5)]
# for lect in lections:
# 	svg=[]
# 	for file in os.listdir(path='fig\\' +lect):
# 		if not(file.endswith('.svg')):
# 			svg.append(file)
# 	for file in svg:
# 		os.remove('fig\\'+lect+'\\'+file)	
# # print(svg)