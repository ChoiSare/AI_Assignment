import sys
class student:
    def __init__(self, name='NULL', hakbun = 'NULL', korea = 0, math = 0, english = 0, grade = 'F'): #클래스의 초기화 부분
        self.__name = name
        self.__hakbun = hakbun
        self.__korea = korea
        self.__math = math
        self.__english = english
        self.__total = self.__korea + self.__math + self.__english
        self.__avg = self.__total/3
        self.__grade = grade

    def SetName(self,name): #이름을 설정할 수 있는 함수
        self.__name = name

    def SetHakbun(self,hakbun): #학번을  설정할 수 있는 함수
        self.__hakbun = hakbun

    def SetKorea(self,korea): #국어성적을 설정할 수 있는 함수
        self.__korea = korea

    def SetMath(self,math): #수학성적을 설정할 수 있는 함수
        self.__math = math

    def SetEnglish(self,english): #영어 성적을 설정할 수 있는 함수
        self.__english = english

    def CalGrade(self): #총점,  평균, 등급을 계산하기 위한 함수
        self.__total = self.__korea + self.__math + self.__english
        self.__avg = self.__total / 3
        self.__avg = round(self.__avg, 2)
        if self.__avg > 90:
            self.__grade = 'A'
        elif self.__avg > 80:
            self.__grade = 'B'
        elif self.__avg > 70:
            self.__grade = 'C'
        elif self.__avg > 60:
            self.__grade = 'D'
        else:
            self.__grade = 'F'
    def __str__(self): #print되었을 때 출력되는 부분
        return("%s\t%s\t\t%s\t%s\t%s\t%s\t%3s\t%s" %(self.__hakbun, self.__name, str(self.__korea), str(self.__math), str(self.__english),
                                                   str(self.__total), str(self.__avg), self.__grade))

stulist =[]
for x in range(5):
    stulist.append(student())
while True:
    for i in range(5):
        a = input("학번을 입력하세요 프로그램 종료시에는 0을 입력하세요: ")
        if a == '0':
            sys.exit()
        stulist[i].SetHakbun(a)
        b = input("이름을 입력하세요: ")
        stulist[i].SetName(b)
        c = int(input("국어 성적을 입력하세요"))
        stulist[i].SetKorea(c)
        d = int(input("수학 성적을 입력하세요"))
        stulist[i].SetMath(d)
        e = int(input("영어 성적을 입력하세요"))
        stulist[i].SetEnglish(e)
        stulist[i].CalGrade()
    print("=" * 70)
    print("학번\t이름\t\t국어\t수학\t영어\t총점\t평균\t학점")
    for p in range(5):
        print(stulist[p])
    print("=" * 70)