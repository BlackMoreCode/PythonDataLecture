import requests # http 통신을 위한 모듈
import json

member = {
    "email": "anyj@gmail.com",
    "pwd": "test123456",
    "name": "안유진",
    "imgPath": ""
}

# 서버 URL 및 헤더 설정
url = "http://localhost:8111/auth/signup"
headers = {"Content-Type": "application/json"}

# POST 요청 보내기
response = requests.post(url, data=json.dumps(member), headers=headers)

# 응답 처리
if response.status_code == 200:
    #서버에서 전달 받은 JSON을 객체로 변환하고 내용을 출력
    data = response.json()
    print(f"이메일 : {data["email"]}")
    print(f"이름 : {data["name"]}")
    print(f"가입일 : {data["regDate"]}")
else:
    print("회원 가입 실패.")