import random

from hello.domains import myRandom, my100


class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

    def quiz17prime(self) -> str: return None

    def quiz18golf(self):
        c = my100()
        p = int(input('1~100까지 숫자 입력'))
        while p != c:
            if p < c:
                p = int(input('Up'))
            elif p > c:
                p = int(input('Down'))
        return print('정답입니다')

    def quiz19booking(self) -> str: return None