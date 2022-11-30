# from msilib import sequence

import requests
from bs4 import BeautifulSoup
 
def get_id(n):

    url = "https://www.googleapis.com/youtube/v3/videos"
    
    params = {
        "key": "AIzaSyC-EdQIhOL5j0VcUeVgZyARJZOt3cBtzd0",
        "part": ["snippet"],
        "chart": "mostPopular",
        "regionCode": "KR",
        "maxResults": n
    }
    #json 이란 서버(웹 에플리케이션 or 웹페이지)와 클라이언트사이에서 데이터를
    # dictionary 형으로 주고 받는데 사용한다 . 
    response = requests.get(url, params=params).json()['items']
    video_List=[]
    for idx in range(len(response)):
        video_List.append(response[idx]['id'])

    return(video_List)
