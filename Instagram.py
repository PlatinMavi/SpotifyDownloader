from instascrape import Reel
import random


def ReelScraper(Link):
    SESSION_ID = "5928661736%3AqmWbbS8sfltPlr%3A28%3AAYfOrsOpJzXRKiIKbV3BLeUYA4A1jEaJn2HpcnInQg"
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "cookie": f'sessionid={SESSION_ID};'
    }

    Random = random.randint(1,99999999999)

    insta_reel = Reel(Link)
 
    # Using  scrape function and passing the headers
    insta_reel.scrape(headers=headers)
    
    # Giving path where we want to download reel to the
    # download function
    insta_reel.download(fp=f".\\Desktop\\reel{Random}.mp4")
    
    # printing success Message
    print('Downloaded Successfully.')

link = input("Link: ")
ReelScraper(link)