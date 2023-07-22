from instascrape import Reel
import datetime

# link = input("Link: ")
link = "https://www.instagram.com/reel/Cu6khaWqwmt/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=="
sessionid = "5928661736%3AqmWbbS8sfltPlr%3A28%3AAYc1PY_IuDpVH4-7sa_hRfYbxjnKUYv_ElokIuXGRA"
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

header = {"User-Agent":useragent,"cookie":f'sessionid={sessionid}'}

instaReel = Reel(link)
instaReel.scrape(headers=header)
instaReel.download(fp="C:/Users/PC/Desktop/ReelDownloader")
print("Downloaded Succesfully")