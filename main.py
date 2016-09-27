#!/usr/bin/env python

import sys, os


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
	ID_N = "|{0}|{1}|{2}|{3}|{4}|{5}".format(ID[0]+ID[1],ID[2]+ID[3],ID[4]+ID[5],ID[6]+ID[7],ID[8]+ID[9],ID[10]) 
	
	LINK_IO = HEAD + "=" + ID_N + "&itag=" + Q
	LINK_IO_N = "'{0}'".format(LINK_IO)
	CALL = "wget {0}".format(LINK_IO_N)
	
	# Call downloader app (wget)
	os.system(CALL)
	
	#N = LINK_IO.partition("http://s2.skyshare.ir/yo|ut|ub|e.|co|m/")[2]
	
	#if NAME:
	#	os.system("mv '{0}' '{1}'".format(N,NAME))

if __name__ == '__main__':
	main()
