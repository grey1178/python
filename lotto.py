# 1~45 중에 6개 만들어서 리스트에 남기기
# 비복원 추출로 6개 뽑기

import random
winners = [4, 7, 14, 16, 24, 44]
num = list(range(1,46))
#lotto = random.sample(num, 6)
# print(lotto)

for i in range(10000):
    lotto = random.sample(num, 6)
    # 당첨 횟수 기록
    count = 0
    # print(lotto [0]~[5])
    for mynum in lotto:
        #print(mynum)
        # lotto가 가지고 있는 값들이 winners에 있다면
        if mynum in winners:
            count = count + 1
        # 한개 당첨
        # 당첨 횟수를 기록
        # 6개 당첨 == 1등
    if count == 6:
        print('1등!!!!!')


