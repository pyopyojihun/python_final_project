import re
from turtle import title
from urllib import response
import requests

# 단어구름에 필요한 작업들 ---------------------------------------------------------------------------------------------
from wordcloud import WordCloud
from konlpy.tag import Okt
#konlpy 모듈은 python으로 구현되어있지만 실제 자연어
#처리는 java에서 처리한다. 한국어 자연어 처리를 위해서 nltk lib을 같이 사용하여
#주로 명사인 단어로 추출한다. 그 후 collection counter() 모듈을 사용하여
#명사가 언급된 횟루를 계산한다.
import nltk
from collections import Counter

def wordcloud_from_text(input_file, output_file='wordcloud.png'):
# def wordcloud_from_text(input_file):
    # get text from file
    try:
        with open(input_file, "rb") as f:
            text=f.read().decode('utf8')
    except Exception as e:      #에러 발생 메세지 출력
        print ('wordcloud_from_text() - %s' %(e))
        return        

    # 예외 처리
    if text == None:    #input 파일에 텍스트가 없는 경우
        print ('wordcloud_from_text() text is None')
        return

    # get noun list
    noun_list = get_noun_list(text)

    # 예외 처리 2
    if len(noun_list) < 10:     #단어 빈도수가 10개가 안 되는 경우
        print ('wordcloud_from_text() - Too small noun list')
        return

    # Generate a word cloud image
    wc = WordCloud(#font_path = './gulim.ttf',
                        background_color = 'white',
                        width=512, height=512,
                        max_font_size=500,
                        max_words=1000)
    wc.generate_from_frequencies(dict(noun_list))   #리스트에 담긴 튜플형태인 noun_list를 딕셔너리로 변환 
    # Save to png
    wc.to_file(output_file)
    print ('Create WordCloud:', output_file)

def get_noun_list(text, method=0):    
    # Sentence to token
    if method == 0:
        # 한국어
        noun = tokenizer_konlpy(text)
    else:
        # 영어
        noun = tokenizer_nltk(text)

    # count word
    count = Counter(noun)

    # get most frequent words
    noun_list = count.most_common(3000)     #3000개의 최빈값 추출
    return noun_list

def tokenizer_nltk(text):
    # NNP: 단수 고유명사, VB: 동사, VBP: 동사 현재형, TO: to 전치사, NN: 명사(단수형 혹은 집합형), DT: 관형사
    is_noun = lambda pos : (pos[:2] == 'NN' or pos[:2] == 'NNP')
    tokenized = nltk.word_tokenize(text)    
    return [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]    #pos_tag: 튜플 형태로 품사 정리

def tokenizer_konlpy(text):
    okt = Okt()
    return [word for word in okt.nouns(text) if len(word) >1]       #nouns: 명사 데이터를 리스트로 받음
