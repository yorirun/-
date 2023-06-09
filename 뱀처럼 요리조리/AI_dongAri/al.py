while True:
    print('1. 검색', '2. 기능')
    Scount = input('하고 싶은 것을 입력하세요 :')

    if Scount == '1' or '검색' or '1. 검색':
        a = input('검색내용을 입력해주세요 :')
        print(a + "에 대해 검색하는 중")
        #selenium or chromebrowse --> 검색

    elif Scount == '2' or '기능' or '2. 기능':
        print("1.파일 찾기, 2.명령어(cmd) 실행")
        b = input('사용할 기능을 입력해주세요 :')
        print(b + "에 대해 실행하는 중")
        #기능에 맞는 역할 수행 코드
    else:
        print('오류, 입력값에 문제가 있는 것 같습니다..')
