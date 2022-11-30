#작성한 함수를 토대로 이미지와 엑셀파일로 내보내기 위한 코드.

import re
from turtle import title
from urllib import response
import requests
import pandas as pd

#밑으로는 전에 작성했던 함수들을 불러온 것이다.
from get_id import get_id 
from get_info import get_info
from get_comment import get_comment
from wdcloud import wordcloud_from_text
from info2table import info2table


import os

video_list=get_id(50)
video_title,video_des,video_channelTitle,video_viewCount=get_info(50)
get_comment(video_list)

#단어구름 작업 ------------------------------------------------------------------------------------------------------
#Comment_List.txt 입력받아 단어구름 이미지 출력
if __name__ == '__main__':
     wordcloud_from_text (input_file='Comment_List.txt')
#-------------------------------------------------------------------------------------------------------------------

#단어구름 작업 후 텍스트파일 삭제
os.remove('./Comment_List.txt')

#info를 엑셀로 내보내기
info2table(video_title,video_des,video_channelTitle,video_viewCount)
