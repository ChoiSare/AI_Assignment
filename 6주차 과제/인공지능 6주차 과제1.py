a = int(input('첫 번째 정수:'))
b = int(input('두 번째 정수:'))
c = input('연산자:')

if c == '+':
    print(a,'+',b,'=',a+b)
    
elif c == '-':
    print(a,'-',b,'=', a-b)

elif c == '*':
    print(a,'*',b,'=', a*b)

elif c == '//':
    print(a,'//',b,'=', a//b)
    
elif c == '/':
    print(a,'==',b,'=', a/b)
    
elif c == '%':
    print(a,'%',b,'=', a%b)

else:
    print('입력 오류입니다. 다시 시작해 주십시오.')
