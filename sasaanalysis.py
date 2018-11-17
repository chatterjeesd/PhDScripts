# This program calculates Solvent excluded and solvent accessible 
# surface area from saved reply log of chimera. The steps are-
# 1. Open the trajectory from Tools-->MD/Ensemble Analysis--> MD movie.
# 2. When the trajectory is loaded, enter the starting frame and step size
#    if you do not want the default values. 
# 3. Hide all other structural representations and show surface. (Actions-->Surface-->show)
# 4. Favorites--> Reply Log
# 5. Deselect Loop in MD movie player and Click on play. the Surface area 
#    will be updated for every frame.
# 6. After all the frames have been played, save the reply log.
# 7. Use this program to open the reply log and extract the area information
#    into a new file. 
#-----------------------SOUMYA DEEP CHATTERJEE (Leiden University)----------------------------

#Enter the name of the reply log file that you saved.
fo=open("sasa-per10frames.txt",'r')

#Enter the name of the output file that will contain all the extracted 
#surface area information per frame.
fr=open("surfacearea.txt", 'a')

#Enter the starting frame and step size
startingframe=1
stepsize=10


#########--------DO NOT CHANGE BELOW THIS LINE----------############



fr.write("Frames"+"\t"+"Solvent-excluded-SA"+"\t"+"Solvent-accessible-SA"+"\n")
for lines in fo:
	if "Surface calculation failed" in lines:
		startingframe+=stepsize
	if "excluded surface area" in lines:
		fr.write(str(startingframe)+"\t"+lines.split()[-1]+"\t")
		startingframe+=stepsize
	if "accessible surface area" in lines:
		fr.write(lines.split()[-1]+"\n")
fr.close()
fo.close()
