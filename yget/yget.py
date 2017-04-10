#!/usr/bin/env python

import sys
import os
import json
import urllib


def main():
	# Variable
	LEN = len(sys.argv)
	Q = "mp4_360"
	
	# Get arguments
	if LEN == 1:
		os.system("clear")
		print "NO YOUTUBE LINK FOUND!"
		exit(0)
	elif LEN == 2:
		LINK = sys.argv[1]
	elif LEN == 3:
		LINK = sys.argv[1]
		QUALITY = sys.argv[2]
	        # Set quality if specified else LOW
	        if QUALITY == "LOW":
	                Q = "mp4_360"
	        elif QUALITY == "HD":
	                Q = "mP4_720"
	        elif QUALITY == "FULL":
	                Q = "best"	
	elif LEN == 4:
		LINK = sys.argv[1]
		NAME = sys.argv[3]
		QUALITY = sys.argv[2]
		# Set quality if specified else LOW
		if QUALITY == "LOW":
	        	Q = "mp4_360"
		elif QUALITY == "HD":
			Q = "mP4_720"
		elif QUALITY == "FULL":
	        	Q = "best"
	
	# Link building mechanism
	HEAD = "http://s2.skyshare.ir/yo|ut|ub|e.|co|m/|wa|tc|h?|v"
	ID = LINK.partition("https://www.youtube.com/watch?v=")[2]
	ID_N = "|{0}|{1}|{2}|{3}|{4}|{5}".format(ID[0]+ID[1],ID[2]+\
						 ID[3],ID[4]+ID[5],\
						 ID[6]+ID[7],ID[8]+\
						 ID[9],ID[10]) 
	
	LINK_IO = HEAD + "=" + ID_N + "&itag=" + Q
	LINK_IO_N = "'{0}'".format(LINK_IO)
	#CALL = "wget -O {0} {1}".format(videoTitle,LINK_IO_N)
	
	#youtube data api mechanism to get title
	token = "AIzaSyAeSYd2Otj_Ku0yrHzGvnJq1E40r0zzfmc"
	url = "https://www.googleapis.com/youtube/v3/videos?id="+ID+\
	"&key="+token+"&fields=items%28snippet%28title%29%29&part=snippet"

	response = urllib.urlopen(url)

	try:
		pyObj = json.loads(response.read())
		for x in pyObj['items']:	
			videoTitle = x["snippet"]["title"]
			print videoTitle
		
	except (ValueError, KeyError, TypeError):
		print "JSON format error"
	
	vi = "'{0}'".format(videoTitle)
	CALL = "wget {1} -O {0}".format(vi,LINK_IO_N)
	# Call downloader app (wget)
	os.system(CALL)
	

if __name__ == '__main__':
	main()
