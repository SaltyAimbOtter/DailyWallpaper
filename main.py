import os
import random
import sys

import requests
import ctypes

# Pass the Pexels API key (https://www.pexels.com/api/) as command line argument
if len(sys.argv) == 1:
    print("You MUST supply an API key as a command line parameter.")
    exit(1)
apiKey = sys.argv[1]
header = {'Authorization': apiKey}
photosPerPage = 80
searchSettings = {'query': 'nature', 'orientation': 'landscape', 'per_page': photosPerPage}
wallpaperPath = "C:/Users/" + os.getlogin() + "/.scripts/DailyWallpaper/image.jpg"

photoList = requests.get('https://api.pexels.com/v1/search', headers=header, params=searchSettings)
photos = photoList.json()['photos']
randomPhotoIndex = random.randrange(0, photosPerPage - 1, 1)
selectedPhoto = photos[randomPhotoIndex]

photoURLs = selectedPhoto['src']
maxQualityURL = photoURLs['original']

imageRequest = requests.get(maxQualityURL)
if imageRequest.status_code == 200:
    with open(wallpaperPath, 'wb') as file:
        for chunk in imageRequest:
            file.write(chunk)

# Tells Windows to change the user background
ctypes.windll.user32.SystemParametersInfoW(20, 0, wallpaperPath, 0)
