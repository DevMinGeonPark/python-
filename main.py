import requests
import time

url = "http://cent.dongseo.ac.kr:8088/servlets/stud/sugang?attribute=sugang_save"
session = requests.Session()

##쿠키설정
cookie = {"JSESSIONID":"CyWacJCipj8D11x5CnUSyI1lHQGMhQK6ONR3t5ckz4GB1XOF74cXZmuWi14D2d1S.web2_servlet_engine3"}

##과목번호, 분산, 과목이름 넣기(과목이름 ecu-kr url 인코딩)

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.3987.132 Safari/537.36"
    }
recent_time = time.strftime('%c', time.localtime(time.time()-1))


 ##원하는 시간 넣기
# while(recent_time != '9:00:00'):
recent_time = time.strftime('%c', time.localtime(time.time()-1))
recent_time = recent_time[12:19]
print(recent_time)


##신청requests보내는 부분
## 과목토드랑 분반만 넣어도 될듯
# data = [{"gwamok_cd":"120006","bunban":"101","gwamok_nm":"%C3%A4%C7%C36"},
#     {"gwamok_cd":"120027","bunban":"302","gwamok_nm":"%BF%B5%BE%EE2"},
#     {"gwamok_cd":"140258","bunban":"101","gwamok_nm":"%BB%E7%B0%ED%BF%CD%B3%ED%B8%AE%3A%B0%B3%B3%E4%2C%B8%ED%C1%A6%2C%B3%ED%C1%F5"},
#     {"gwamok_cd":"320138","bunban":"101","gwamok_nm":"%BF%EE%BF%B5%C3%BC%C1%A6%28%C4%B8%BD%BA%C5%E6%B5%F0%C0%DA%C0%CE%29"},
#     {"gwamok_cd":"321451","bunban":"102","gwamok_nm":"%BC%D2%C7%C1%C6%AE%BF%FE%BE%EE%B0%B3%B9%DF%BD%C7%BD%C04%28%C4%B8%BD%BA%C5%E6%B5%F0%C0%DA%C0%CE%29"},
#     {"gwamok_cd":"321457","bunban":"101","gwamok_nm":"%BB%E7%C0%CC%B9%F6%C6%F7%B7%BB%BD%C4%28%C4%B8%BD%BA%C5%E6%B5%F0%C0%DA%C0%CE%29"},
#     {"gwamok_cd":"321458","bunban":"101","gwamok_nm":"%BD%C3%BD%BA%C5%DB%BA%B8%BE%C8"},
#     {"gwamok_cd":"321459","bunban":"101","gwamok_nm":"IoT%C0%C0%BF%EB%C7%C1%B7%CE%C1%A7%C6%AE1%28%C4%B8%BD%BA%C5%E6%B5%F0%C0%DA%C0%CE%29"}]
data = [{"gwamok_cd":"140020","bunban":"101"}]

for i in data:
    req = session.post(url = url,headers = header, data = i, cookies = cookie)
    print(req.text)