for x in range(5):
    a = input('학년과 반을 입력하시오:')
    b = int(input('번호:'))
    c = int(input('국어 점수:'))
    d = int(input('영어 점수:'))
    e = int(input('수학 점수:'))
    f = int(input('물리 점수:'))
    
    total = c+d+e+f
    ave = total/4
    
    print('총점:', total)
    print('평균:', ave)
    
    if ave >= 90:
        print('학점: A')    
    elif ave >= 80:
        print('학점: B')
    elif ave >= 70:
        print('학점: C')
    elif ave >= 60:
        print('학점: D')
    else:
        print('학점: D 이하')
    