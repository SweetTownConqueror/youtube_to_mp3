import urllib.request
from bs4 import BeautifulSoup
import os

file1 = open('mylist.txt', 'r') 
Lines = file1.readlines() 

for line in Lines: 
	textToSearch = line.strip()
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	#print("url: "+url)
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		print("Downloading " + textToSearch + " at https://www.youtube.com" + vid['href'] + " ...")
		os.system("python3 yt2mp3.py https://www.youtube.com"+ vid['href'])
		break;