import praw
import os
import webbrowser


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
            ls.append('https://www.reddit.com' + submission.permalink)
            print("Bot added link to: ",submission.title)
            posts_checked.append(submission.id)
            
    with open("posts_checked.txt", "w") as f:
        for post_id in posts_checked:
            f.write(post_id + "\n")
            
    with open("post_links.txt", "a") as f:
        for link in ls:
            print("post_links.txt appending: " + link)
            f.write(link + "\n")
            
            
        
def openLinks(): 
    edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    with open("post_links.txt","r") as f:
        links = f.readlines()
    for link in links:
        link = link.strip()
        print("Opening in Chrome: "+ link)
        webbrowser.get('edge').open_new_tab(link)


def cleanTxts(filename):
    with open(filename, "w") as f:
        f.truncate()
    
            
def searchSuits():
    searchReddit('suit', 'frugalmalefashion')
    searchReddit('suit', 'frugal')
    searchReddit('suit', 'malefashionadvice')
    openLinks()

def searchLegion():
    searchReddit('legion', 'laptopdeals')
    searchReddit('legion', 'buildapcsales')
    openLinks()
    
# Driver code
searchSuits()
searchLegion()
cleanTxts("post_links.txt")


