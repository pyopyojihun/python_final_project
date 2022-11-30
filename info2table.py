import pandas as pd
#panads 는 파이썬에서 데이터분석 라이브러리로 사용되며 행과 열로
#이루어진 데이터 객체를 만들어 다룰 수 있는 라이브러리이다.
#대 부분 dataframe의 2차원 이 사용된다.
#딕셔너리를 이용하여 data파일을 만들고 데이터 프레임을 excel로 내보내는 코드 
def info2table(video_title,video_des,video_channelTitle,video_viewCount):

    data = {'영상제목': video_title,
            '영상설명': video_des,
            '채널명': video_channelTitle,
            '조회수': video_viewCount}
    df = pd.DataFrame(data)

    df.to_excel('info.xlsx', encoding='utf-8-sig')
