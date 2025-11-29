
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image  
import datetime
import re
from nltk.corpus import stopwords
from kiwipiepy import Kiwi


with open("news.txt", "r", encoding="utf-8", errors="ignore") as file:
    text = file.read()
print("텍스트 길이 : ", len(text))
# 1. 마스크 경로 지정
mask = np.array(Image.open("apple_mask.png")) # 파이썬 파일과 같은 폴더에 저장된 png 파일만


kiwi = Kiwi()
# 영어 단어와 숫자 추출
eng_words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

# 한국어 단어 추출(명사, 동사, 형용사)
ko_tokens = kiwi.tokenize(text)
ko_nouns = [t.form for t in ko_tokens if t.tag.startswith(('NN','VA','VV'))]
    
# 불용어 제거
eng_stop = set(stopwords.words('english'))
eng_filtered = [word for word in eng_words if word not in eng_stop]

# 한국어 불용어 제거
ko_stop = { "이", "그", "저", "것", "수", "등", "들", "때", "중", "더", "고", "한", "된", 
           "된", "와", "과", "의", "가", "은", "는", "를", "에", "에서", "로", "으로",
           "있다", "없다", "이다", "한다", "된다", "됐다", "로부터","까지","만","뿐"}  
ko_filtered = [w for w in ko_nouns if w not in ko_stop]

# 영어 단어 + 한국어 단어
all_words = eng_filtered + ko_filtered

text = " ".join(all_words)



# 3. 워드클라우드 생성 
wc = WordCloud(
    font_path="C:/Windows/Fonts/HMFMPYUN.ttf",        # 맑은 고딕 (윈도우 기본 폰트)
    background_color="white",      # 배경색
    mask=mask,                     # 마스크 씌우기
    contour_width=5,             # 마스크 테두리 설정
    contour_color="coral",          # 테두리 색상 (원하는대로)
    width=800,
    height=800,
    max_words=150,
    min_font_size=0,
    colormap="hot",              # 텍스트 색상 모드
    random_state=42
).generate(text)

# 4. 결과 보기
plt.figure(figsize=(10,10))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.tight_layout()
plt.show()

# 5. 날짜 시간 별 저장 파일 이름 생성 자동화
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"wordcloud_{timestamp}.png"
wc.to_file(filename) # 파일 저장
