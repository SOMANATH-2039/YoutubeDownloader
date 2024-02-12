# importing all the required modules 
from django.shortcuts import render, redirect 
from pytube import *
import os
from django.views.decorators.csrf import csrf_exempt


DOWNLOAD_DIR='D'
# defining function
# @csrf_exempt 
def playlistYoutube(request): 

	# checking whether request.method is post or not 
	if request.method == 'POST': 
		
		# getting link from frontend 
		links = request.POST['link']
		playlist=Playlist(links)
		for link in playlist.video_urls:
			video = YouTube(link) 

			# setting video resolution 
			stream = video.streams.get_highest_resolution() 
			
			# downloads video 
			stream.download() 
			downloaded+=1
		
				# returning HTML page 
		# 	return render(request, 'youtube.html') 
	return render(request, 'youtube.html')
# @csrf_exempt
def oneYoutube(request):
	if request.method =='POST':
		link = request.POST['link']
		video = YouTube(link) 
		# setting video resolution 
		stream = video.streams.get_highest_resolution() 
		# downloads video 
		stream.download()

	return render(request, 'youtube.html')

def home(request):

	return render(request, 'home.html')