from googleapiclient.discovery import build
# import webbrowser

# Use YouTube API key to access information
api_key = 'KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

# Search for a YouTube video based on users query
query = "USER QUERY"
video_request = youtube.search().list(
    part='id',
    q=query,
    type='video',
    maxResults=1
)
video_response = video_request.execute()

# Create YouTube URL with returned YouTube Video ID
url = "https://www.youtube.com/watch?v=" + video_response['items'][0]['id']['videoId']
print("---YouTube Video URL---\n", url, "\n")

# OPTIONAL: Automatically open YouTube URL in a browser
# load url in browser - this could be used for bot to stream video
# new = 2
# webbrowser.open(url, new=new)
