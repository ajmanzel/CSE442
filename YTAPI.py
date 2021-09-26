from googleapiclient.discovery import build
import webbrowser

api_key = 'KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

# gather stats of a youtube channel
username = 'vevo'
channel_stats_request = youtube.channels().list(
    part='statistics',
    forUsername=username
)
channel_stats_response = channel_stats_request.execute()
print("---Channel Stats---\n", channel_stats_response, "\n")

# search for youtube video
query = "USER QUERY"
video_request = youtube.search().list(
    part='id',
    q=query,
    type='video',
    maxResults=1
)
video_response = video_request.execute()
print("---Video Search Result---\n", video_response, "\n")

url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']['videoId']
print("---YouTube Video URL---\n", url, "\n")

# load url in browser - this could be used for bot to stream video
new = 2
webbrowser.open(url, new=new)
