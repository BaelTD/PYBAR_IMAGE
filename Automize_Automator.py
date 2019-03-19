#!/usr/bin/python3

__author__ = "BaelTD"
__copyright__ = "Copyright 2019, Automatize the automator"
__credits__ = ["David Morelli"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "BaelTD"
__email__ = "morelli.d14@gmail.com"
__status__ = "Production"

import sys
import glob
import os
from pyzbar.pyzbar import decode
import pyzbar
import numpy as np
import cv2
import time
from PIL import Image


#Mostra codice a barre e QR core in locazione
def display(im, decodeObjects):

	#cicla per tutti gli oggetti decodificati
	for decodeObject in decodeObjects:
		points= decodeObject.polygon
		# se i punti non sono sono formati da 4 cifre cerca convex null
		if len(points)> 4 :
			hull = cv2.convexHull(np.array([point for point in points], dtype= np.float32))	
			hull = list(map(tuple,np.squeeze(hull)))	
		else :
			hull = points;
	#numeri si punti in convensione Hull
	n = len(hull)
	for j in range(0,n):
		cv2.line(im,hull[j],hull[ (j+1) % n], (255,0,0), 3 )
	cv2.imshow("Barcode Image:", im);
	cv2.waitKey(10);
	
#main dove we search in specific directory every file with extention .jpg

if __name__ =='__main__':
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-.-.-.-Automate the AUTOMATOR-.-.-.-.-.-.-.-.-.-.")
	print("-.-.-.-.-.-CONVERT IMAGE BARCODE IN TEXTBARCODE-.-.-.-.-.-.")
	print("-.-.-.-.-SEARCH IN DIRECTORY BARCODE FILE IMG: *JPG :-.-.-.")
	raw_input("Press key to continue....")
	os.chdir("/home/bael/Develop")
	for file in glob.glob("*.jpg"):
		print(file)

		im = cv2.imread('/home/bael/Develop/bar_image/'+file )
		print("Apertura immagine codice a barre....")
		time.sleep(2)
		if im is not None :

			print("THIS IS MATRIX BARCODE :")
			print(im)
			print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
			print("THIS IS BARCODE DECODIFIED :")	
			print(decode(im))
			print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
			x = decode(im)
			xran =range(0,len(x))
				
							

			if x != [] :

				for n in xran:
					print("Only data ob BARCODE: ")
					print("Data:" + x[n].data)
					print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-")
	
					print("Saving data on File (is do not exit it will create): ")
					text_file = open("barcode.txt","a")
					print("Opening File named Barcode....")
					text_file.write(x[n].data + "\n")
					print("Write in file BARCODE.... ")
					text_file.close()
					print("Succesfully Saved BARCODE. ")
					decodedObjects = decode(im)
					display(im, decodedObjects)
			else : print("ERROR DURING READ OF BARCODE")


		else: print("Nessuna immagine con tale nome...")
	print("Grazie per aver utilzzato il nostro Software")






