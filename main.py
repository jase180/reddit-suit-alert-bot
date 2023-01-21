import praw
import os

# initiate bot from praw.ini
reddit = praw.Reddit('bot1')

def searchReddit(keyword,subName):
    
    # initiate subreddit
    subreddit = reddit.subreddit(subName)
    
    # get posts_checked ls or create if none
    if not os.path.isfile("posts_checked.txt"):
        posts_checked = []
    else:
        with open("posts_checked.txt","r") as f:
            posts_checked = f.read()
            posts_checked = posts_checked.split("\n")
            posts_checked = list(filter(None, posts_checked))
            
    ls = []
    
    for submission in subreddit.search(keyword, time_filter = "day"):
        if submission.id not in posts_checked:
            ls.append('www.reddit.com' + submission.permalink)
            print("Bot added link to: ",submission.title)
            posts_checked.append(submission.id)
            
    with open("posts_checked.txt", "w") as f:
        for post_id in posts_checked:
            f.write(post_id + "\n")
            
    with open("post_links.txt", "a") as f:
        for link in ls:
            f.write(link + "\n")
            
searchReddit('suit', 'frugalmalefashion')
searchReddit('suit', 'frugal')
searchReddit('suit', 'malefashionadvice')