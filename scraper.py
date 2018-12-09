from os import path, makedirs
import praw
import requests

####
# REMOVED SECRET KEY
####

subreddit = reddit.subreddit('wallpapers')
makedirs(f'{subreddit}/',exist_ok=True)

for post in subreddit.hot(limit=10):
        url = post.url
        filename = url.split('/')[-1]
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith('.webm') or filename.endswith('.gifv') or filename.endswith('.giphy') or filename.endswith('.webp') or filename.endswith('.mp4'):
            print(f'Getting {post.title} -- {filename}')
            res=requests.get(url)
            with open(path.join(f'{subreddit}/{filename}'), 'wb') as file:
                file.write(res.content)
