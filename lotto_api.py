# requests 불러오기
import requests

# requests 사용해서 로또 api에 데이터 요청
url = 'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
response = requests.get(url).json()

# 요청 보내서 응답 받은 문서를 출력

#print(response)
winners = []
# print(response['drwtNo1'])
# print(response['drwtNo2'])
# print(response['drwtNo3'])
# print(response['drwtNo4'])
# print(response['drwtNo5'])
# print(response['drwtNo6'])
# 1~7 반복
for num in range(1,7):
    #print(response[f'drwtNo{num}'])
    winners.append(response[f'drwtNo{num}'])

print(winners)