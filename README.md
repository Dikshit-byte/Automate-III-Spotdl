# Automation-III-Spotdl

STEP 1: Clone this repo on your local machine.

STEP 2: Install Spoti-dl with this cmd ```pip install spoti-dl```

STEP 3: Install [FFmpeg](https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z) and after installation, unzip it then find bin file and add this it in your user environment variable path.

STEP 4: Get Developers keys from spotify.

 Steps to make a Spotify developer account:
 
a. Go to [Spotify Dev Dashboard](https://developer.spotify.com/dashboard/applications)

b. Login with your credentials and click on "create an app".

c. Enter any name of choice, app description, tick the checkbox and proceed.

d. Now you have access to your client ID. Click on "Show client secret" to get your client secret.

e. Now click on "edit settings" and in the "redirect URIs" section add ```http://localhost:3000/callback```

STEP 5: Define these three environment variables: 
```
SPOTIPY_CLIENT_ID - <client id that you get from spotify developer account>
SPOTIPY_CLIENT_SECRET - <client secret>
SPOTIPY_REDIRECT_URI - http://localhost:3000/callback
```

STEP 6: Now just run ```py index.py``` and boom enjoy!!

STEP 7: You can also change the saving directory path where you wish to keep your downloads.

STEP 8: Thank me later!!

                                                                                         ~Dikshit Singh
