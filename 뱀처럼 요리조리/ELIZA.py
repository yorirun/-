# 일라이자 알고리즘을 random 모듈로 구현해 본 파일 by yorirun

import random as rn #random(난수 생성 모듈)을 rn으로 축약해 불러옴

core1 = rn.randrange(1,4) #핵심 1은 랜덤.범위 에서 1~3(n-1)까지

print("지금 당신은 어떤 상황인가요?") #지금 당신은 어떤 상황인가요?를 print로 출력
a = input("입력 - ") #input()함수를 입력 받을 a를 만듦

if core1 == 1:  #핵심1에서 랜덤.범위(=난수)가 1 일때
  print(a,"가(이) 당신을 힘들게 하는군요?") #a(대답)이 당신을 힘들게하는군요? (더함)
  
if core1 == 2: #핵심1에서 랜덤.범위(=난수)가 2 일때
  print(a,"를 그만둔다면 도움이 될까요?") #(더함)2

if core1 == 3: #핵심1에서 랜덤.범위(=난수)가 3 일때
  print(a,"를 왜 계속 해야하나요?") #(더함)3
  
#이런 식으로 반복 --> 심리적인 안정감을 줌
  
  '''
참고: print를 띄어서 작성하는 들여쓰기로 안에다가 종속시킴
if core1 == 3: <--이거 일 때
@@print(a,"를 왜 계속 해야하나요?") <--이거를 출력하도록 함 (@는 뛰어쓰기를 의미)

                                                                        by yorirun
  '''
