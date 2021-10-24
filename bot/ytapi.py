import os
import webbrowser

from googleapiclient.discovery import build


# Initialize YouTube API
# from tokens import YouTubeToken
# api_key = YTTOKEN
api_key = os.environ.get('YTTOKEN')
youtube = build('youtube', 'v3', developerKey=api_key)


# Uses API to search YouTube and constructs the video URL.
def get_youtube_data(query):
    # search for YouTube video
    video_request = youtube.search().list(
        part='id,snippet',
        q=query,
        type='video',
        maxResults=1
    )
    video_response = video_request.execute()

    # construct YouTube URL
    url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']['videoId']
    # get song title
    title = video_response['items'][0]['snippet']['title']
    # get song artist
    artist = video_response['items'][0]['snippet']['channelTitle']

    # create and return dictionary with video URL, title, and artist
    video_data = {'video_url': url, 'title': title, 'artist': artist}
    return video_data


# Opens passed url in user's default browser.
def load_youtube_url(url):
    # load url in browser
    new = 2
    webbrowser.open(url, new=new)


"""""
# Local testing gives expected results, bot does not
if __name__ == '__main__':
    data = get_youtube_data("/play happier than ever")
    youtube_url = data['video_url']
    title = data['title']
    artist = data['artist']
    spoken_str = 'YouTube URL: ' + youtube_url + '\n"' + title + '" by ' + artist
    print(spoken_str)
"""""
