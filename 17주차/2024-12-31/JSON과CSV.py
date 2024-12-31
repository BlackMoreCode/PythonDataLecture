import json
# [] : 리스트 --> 시퀀스형 데이터 관리. 크기를 지정하지 않아도 자동 크기 조절, Mutable(읽기, 쓰기)
# {} : 딕셔너리 --> 키와 값의 쌍을 구성되어 있음
# () : 튜플 --> 시퀀스형 데이터. Immutable (읽기만 가능). Packing/Unpacking

# person = 10, "M", "경기도 수원시", "곰돌이", True # packing
# print(person)
# age, gender, addr, name, adult = person # unpacking
#
# print(divmod(23, 5)) # (4, 3)

customer = {
    "id" : 100,
    "name" : "DIO",
    "history" : [
        {"date" : "2023-05-05", "Product" : "iPhone 14 Pro"},
        {"date" : "2023-05-10", "Product" : "Galaxy S23 Ultra"}
    ]
}

#Python 객체를 JSON 문자열로 변환
# json.dumps : 객체를 JSON 문자열로 변환
# ensure_ascii=False : ASCII 문자열이 아님.
# indent=4 : 들여쓰기 4칸
jsonString = json.dumps(customer, ensure_ascii=False, indent=4)
print(jsonString)

dict = json.loads(jsonString)
print(dict["name"])
for e in dict["history"]:
    print(e["date"], e["Product"])

# Python 의 for 문의 range() 기반, 그리고 시퀀스형 데이터를 순회하는 for 문이 있다.

for i in range(10): # range(시작 인덱스, 종료 인덱스, 증감값)
    print(f"{i}", end=" ")
print()

cars = ["모델 Y", "X4", "폴스타4", "EV3", "마칸", "팬텀", "에어로시티"]
for e in cars: #시퀀스형(리스트, 튜플, 문자열, 입력) 데이터 순회
    print(f"{e}", end=" ")
print()

#범위 기반 for로 cars 출력하기
for i in range(0, len(cars)):
    print(f"{cars[i]}", end=" ")


#CSV 파일: Comma-Separator-Value / Comma Separated Values
# 콤바로 구분된 텍스트 형태의 파일
f = open("output.csv", "w", encoding="utf-8", newline="")
wr = csv.writer(f)
wr.writerow([1, "안유진", "서울시 강남구 삼성동", "리더"])
wr.writerow([2, "장원영", "서울시 강남구 삼성동", "댄서"])
wr.writerow([3, "모름", "서울시 강남구 삼성동", "넌 누구냐"])