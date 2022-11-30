import re
from turtle import title
from urllib import response
import requests
from get_id import get_id 
#api란 application programming interface
#api 키를이용하여 유튜브에 접근을 하고 정보를 얻어오기 위해 정의된 함수.
def get_info(n):
    url1 = "https://www.googleapis.com/youtube/v3/videos"  # youtube v3 api 사용

    params1_snippet = {
    "key": "AIzaSyCBrZ5VTkDJ10shyRllMxfnj5AN6Fo-NEY",  # api키
    "part": ["snippet"],
    "chart": "mostPopular",
    "regionCode": "KR",
    "maxResults": n
    }

    params1_statistics = {
        "key": "AIzaSyCBrZ5VTkDJ10shyRllMxfnj5AN6Fo-NEY",
        "part": ["statistics"],
        "chart": "mostPopular",
        "regionCode": "KR",
        "maxResults": n
    }

    response1_snippet = requests.get(url1, params=params1_snippet).json()['items']
    response1_statistics = requests.get(url1,params=params1_statistics).json()['items']

    video_title = []
    video_des = []
    video_channelTitle = []
    video_viewCount = []
#내가 원하는 정보를 리스트에 추가하는 코드.
#idx 안에 snippet라는 집합 안에 title을 추가하겠다.
#title,channelTitle,description에 관한 정보를 접근하기 위해 사용.
    for idx in range(len(response1_snippet)):
        video_title.append(response1_snippet[idx]['snippet']['title'])
        video_des.append(response1_snippet[idx]['snippet']['description'])
        video_channelTitle.append(response1_snippet[idx]['snippet']['channelTitle'])
        video_viewCount.append(response1_statistics[idx]['statistics']['viewCount'])


    return video_title,video_des,video_channelTitle,video_viewCount
    
