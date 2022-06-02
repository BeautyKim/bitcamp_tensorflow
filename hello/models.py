import random

class Quiz01Calculator(object):

    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def calc_res(self):
        if self.opcode == '+':
            return self.num1 + self.num2
        elif self.opcode == '-':
            return self.num1 - self.num2
        elif self.opcode == '*':
            return self.num1 * self.num2
        elif self.opcode == '/':
            return self.num1 / self.num2


class Quiz02Bmi(object):
    @staticmethod
    def getBmi(member):
        this = member
        bmiRes = this.weight/ (this.height**2)*10000
        if bmiRes < 18.5:
            return '저체중'
        elif bmiRes < 23:
            return '정상'
        elif bmiRes < 25:
            return '과체중'
        elif bmiRes < 30:
            return '경도 비만(1단계 비만)'
        elif bmiRes < 35:
            return '중도 비만(2단계 비만)'
        else:
            return '고도 비만'

class Quiz03Grade(object):

    def __init__(self, kor, eng, math, name):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.name = name

    def total(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.total() / 3

    def grade_pass(self):
        return '합격' if self.avg() >= 60 else '불합격'

class Quiz04GradeAuto(object):
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def total(self):
        return self.kor + self.eng + self.math
    def avg(self):
        return self.total()/3
    def grade_pass(self):
        return '합격' if self.avg() >= 60 else '불합격'

def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1, 6)

class Quiz06RandomGenerator(object): # 원하는 범위의 정수에서 랜덤값 1개 추출
    @staticmethod
    def cast():
        pass

class Quiz07RandomChoice(object): # 803호에서 랜덤으로 1명 이름 추출
     @staticmethod
     def choiceMembers():
         members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
         return random.choice(members)
    #def __init__(self):
    #    self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
    #                    "권혜민", "서성민", "조현국", "김한슬", "김진영",
    #                    '심민혜', '권솔이', '김지혜', '하진희', '최은아',
    #                    '최민서', '한성수', '김윤섭', '김승현',
    #                    "강 민", "최건일", "유재혁", "김아름", "장원종"]
    #def choiceMember(self):
    #    return self.members[myRandom(0,23)]

class Quiz08Rps(object): # 1.가위 2.바위 3.보
    def __init__(self, player):
        self.player = player
        self.com = myRandom(1, 3)

    def game(self):
        p = self.player
        c = self.com

        if p == c:
            res = '무승부'
        elif (p == 1 and c == 3) or (p == 2 and c == 1) or (p == 3 and c == 2):
            res = '승리'
        else:
            res = '패배'
        return res

class Quiz09GetPrime(object):
    def __init__(self, number):
        self.number = number
    def primeNum(self):
        pass


class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year
    def leapYear(self):
        a = self.year
        if a%4==0 and a%100!=0 or a%400==0:
            return '윤년'
        else:
            return '평년'


class Quiz11NumberGolf(object):
    def __init__(self, player):
        self.com = myRandom(1, 100)
        self.player = player

    def game(self):
        c = self.com
        p = self.player
        while p != c:
            if p < c:
                p = int(input('Up'))
            elif p > c:
                p = int(input('Down'))
        return '정답입니다'


class Quiz12Lotto(object):
    @staticmethod
    def lotto():
        return random.sample(range(1, 46), 6)


class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass


class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass
