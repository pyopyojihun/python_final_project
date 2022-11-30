#댓글정보를 저장하기 위해서 만든 코드
import re
from turtle import title
from urllib import response
#URL 이나 HTTP를 여는데 도움이되는 함수와 클래스를 정의한다.
import requests
#따라서 urllib.request를 사용하여 간단하게 웹 페이지 요청 및 데이터를 가져올 수 있음.
from get_id import get_id 

def get_comment(video_list):

    url2 = "https://www.googleapis.com/youtube/v3/commentThreads"

    for id in video_list:

        params2 = {
                "key": "AIzaSyC-EdQIhOL5j0VcUeVgZyARJZOt3cBtzd0",
                "part": ["snippet"],
                "videoId": id
                }

                #response2에 댓글 정보 저장
        response2 = requests.get(url2, params=params2).json()['items']

        #comment_List에 topLevelComment 저장
        comment_List = []
        for item in response2:
            comment_List.append(item['snippet']['topLevelComment']['snippet']['textDisplay'])
        #반복문 comment_List가 생성될 때마다 Comment_List.txt파일로 저장
        with open('Comment_List.txt', 'a', encoding = 'UTF-8') as f:
            for comment in comment_List:
                f.write(comment + '\n')

    return (comment_List)
