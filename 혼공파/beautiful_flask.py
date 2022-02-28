# BeautifulSoup 모듈 실습하기

from flask import Flask
from urllib import request
import bs4

# 웹서버 생성
app = Flask(__name__)
@app.route("/") # 특정 URL에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터다.

def hello():
    # urlopen() 함수로 기상청의 전국날씨 읽기
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    
    # 웹페이지 분석
    soup = bs4.BeautifulSoup(target, "html.parser")
    
    # location 태그 찾기
    output = ''
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그 찾아 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string)
        output += "날씨: {}<br/>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string,location.select_one("tmx").string)
        output +="<hr/>"
    return output



