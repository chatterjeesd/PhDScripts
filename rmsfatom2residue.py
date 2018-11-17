#!/usr/bin/env python
# This program extracts the atomic information from the rms fluctuations from the two largest eigenvectors obtained from 
# Principal Component Analysis (PCA) and traces those atoms back from the Protein atomic coordinates to give us the amino acid 
#residues involved in essential dynamics. (Soumya Deep Chatterjee, Leiden University)

# Insert the following information 
rmsffile='eigrmsf.xvg'
avgpdbfile='average.pdb'     
rmsfcutoff= 0.15
residcol=3       # column position for residue name in averagepdbffile
residnumcol=5    # column position for residue number in averagepdbfile


#---------Program starts below. Do not Change without permission------
linedlist=[]
finalresiduelist=[]
avgpdb= open(avgpdbfile).read().split('\n')
for lined in avgpdb:
	if 'ATOM' in lined:
		linedlist.append(lined)


rmsfilesplit = open(rmsffile).read().split('&')
for lines in range(len(rmsfilesplit)-1):
	a= rmsfilesplit[lines].split('\n')
	atomnumlist=[]
	eigvecresiduelist=[]
	for i in a:
		if '@' not in i and len(i.split())>0:
			if float(i.split()[1])>=rmsfcutoff:
				atomnum= int(float(i.split()[0]))
				atomnumlist.append(atomnum)
				dynatom= linedlist[atomnum-1].split()
				print dynatom
				#print dynatom[residcol]+dynatom[residnumcol]+"-"+dynatom[2]+",",
				if str(dynatom[residcol]+dynatom[residnumcol]) not in eigvecresiduelist:
					eigvecresiduelist.append(str(dynatom[residcol]+dynatom[residnumcol]))
				if str(dynatom[residcol]+dynatom[residnumcol]) not in finalresiduelist:	
					finalresiduelist.append(str(dynatom[residcol]+dynatom[residnumcol]))
	#print "'\n'"
	print len(eigvecresiduelist),"residues have high rms fluctuations in eigenvector",lines+1,":-"
	print eigvecresiduelist, "\n"
print len(finalresiduelist), "residues have high rms fluctuations in all eigenvectors:-"	
print finalresiduelist

	
