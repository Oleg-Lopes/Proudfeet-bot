import os
import praw
from replit import db
import time

client_id = os.environ['client_id']
client_secret = os.environ['client_secret']
username = os.environ['username']
password = os.environ['password']

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent="<Proudfeet-bot 1.0>")

subreddit = reddit.subreddit("lotrmemes")


def already_commented(comment_id):
  if comment_id in db.keys():
    return True
  return False


def send_message(comment):
  try:
    comment.reply(body="Proudfeet!")
    print("Proudfeet!")
    return True
  except Exception as e:
    print(e)
    return False


comments_parsed = 0
print(f"Total comments parsed: {comments_parsed}", end="\r")

for comment in subreddit.stream.comments(skip_existing=True):
  comments_parsed += 1
  print(f"Total comments parsed: {comments_parsed}", end="\r")

  if "proudfoot" in comment.body.lower() and not already_commented(comment.id):
    print("------------------")
    print(comment.permalink)
    print(comment.body)

    if send_message(comment):
      db[comment.id] = comment.id
      time.sleep(610)
