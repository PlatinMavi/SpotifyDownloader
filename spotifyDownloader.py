import pytube
import base64
from requests import post, get
import json
import os
from dotenv import dotenv_values

class Spotify():
    def __init__(self) -> None:
        self.client_id = dotenv_values(".env")["CLIENT_ID"]
        self.client_secret = dotenv_values(".env")["CLIENT_SECRET"]

    def GetToken(self):
        auth_string = self.client_id+":"+self.client_secret
        auth_bytes = auth_string.encode("utf-8")
        auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

        url = "https://accounts.spotify.com/api/token"
        header = {
            "Authorization":"Basic "+auth_base64,
            "Content-Type":"application/x-www-form-urlencoded"
        }
        data = {"grant_type":"client_credentials"}
        result = post(url, headers=header,data=data)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token

    def Get_Auth_Header(self,token):
        return {"Authorization":"Bearer "+token}

    def GetTracks(self,playlist_id, token):
        playlistid = playlist_id.split("/")[-1].split("?")[0]
        url = f"https://api.spotify.com/v1/playlists/{playlistid}/tracks"
        headers = self.Get_Auth_Header(token)
        res = get(url,headers=headers)
        json_result = json.loads(res.content)

        tracks = []

        path = f"C:/Users/PC/Desktop/{playlistid}"
        check = os.path.exists(path)
        if check:
            os.remove(path)
            os.mkdir(path)
        else:
            os.mkdir(path)
        
        for track in json_result["items"]:
            artist = track["track"]["artists"][0]["name"]
            tracks.append({"name":track["track"]["name"],"artist":artist})
        return tracks, path
    
class YoutubeD():
    def __init__(self) -> None:
        pass

    def SearchAndDownload(self,playlist,out):
        for song in playlist:
            result = pytube.Search(song["name"]+" "+song["artist"]).results[0].watch_url
            yt = pytube.YouTube(result)
            stream = yt.streams.filter(only_audio=True).first()

            stream.download(output_path=out, filename=song["name"]+".mp3")
            print("downloaded: "+song["name"])

    
sp = Spotify()
yt = YoutubeD()

link = input("Playlist Linki: ")

playlist,name = sp.GetTracks(link,sp.GetToken())
yt.SearchAndDownload(playlist,name)