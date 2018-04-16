from __future__ import unicode_literals
import os
import shutil
import sys
import re
import urllib 
import requests
import json
import youtube_dl
from bs4 import BeautifulSoup

def get_video_URL(movieName,movieYear):
	BASE_URL = "https://www.youtube.com/results?"
	
	soup = BeautifulSoup(requests.get(BASE_URL + urllib.urlencode({"search_query":"allintitle:" + "\"" + movieName + "\"" + " " + "+\"" + movieYear + "\"" + " " +  "+\"trailer\",hd,short"})).text,"html.parser")
	data = soup.findAll("a",{"class":"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})
	if(len(data) > 0):
		return ("https://www.youtube.com" + data[0]['href'])
	else:
		soup = BeautifulSoup(requests.get(BASE_URL + urllib.urlencode({"search_query":"allintitle:" + "\"" + movieName + "\"" + " " +  "+\"trailer\",hd,short"})).text,"html.parser")	
		data = soup.findAll("a",{"class":"yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})
		if(len(data) > 0): 
			return ("https://www.youtube.com" + data[0]['href'])
	return None
def get_trailers():
	
	path = os.path.dirname(os.path.realpath(sys.argv[0]))
	os.chdir(path)
	processedFile = open("processed_movies.txt","a+")
	trailerNames = processedFile.read().split('\n')
	for dirpath, dirnames, filenames in os.walk(u'.'):
		try:
			if dirpath != '.' and not dirpath.endswith('extrafanart') and not dirpath.endswith('extrathumbs'):
				if(dirpath[2:] not in trailerNames):
					movieName,movieYear = [entry.strip() for entry in re.split("((?:\S+ )+)+(\(\d+\))",dirpath[2:]) if entry != ' ' and entry != '']
					currURL = get_video_URL(movieName,movieYear)
					if(currURL != None):			
						ydl_opts = {
							'format':'bestvideo+bestaudio',
							'outtmpl':"{}/{}-trailer.%(ext)s".format(dirpath,dirpath[2:])
						}
						with youtube_dl.YoutubeDL(ydl_opts) as ydl:
							ydl.download([currURL])
							processedFile.write(dirpath[2:] + "\n")
				else:
					print("Already downloaded trailer for: " + dirpath[2:])
		except Exception as e:
			print("Issue downloading trailer: " + str(e))
			

def remove_trailers():
	for dirpath,dirnames,filenames in os.walk(u'.'):
		if dirpath != '.' and not dirpath.endswith('extrafanart') and not dirpath.endswith('extrathumbs'):
			for file in [os.path.join(dirpath,file) for file in filenames if "trailer" in file]:
				os.remove(file)


if __name__=="__main__":
	get_trailers()
