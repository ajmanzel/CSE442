from googleapiclient.discovery import build
import webbrowser

# Initialize YouTube API
api_key = 'YTAPI_KEY'
youtube = build('youtube', 'v3', developerKey=api_key)


# Uses API to search YouTube and constructs the video URL.
def get_youtube_url(query):
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


# Opens passed url in user default browser.
def load_youtube_url(url):
    # load url in browser
    new = 2
    webbrowser.open(url, new=new)
