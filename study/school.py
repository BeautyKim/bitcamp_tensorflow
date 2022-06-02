import random

from hello.domains import memberlist


class School(object):
    def __init__(self):
        self.student = random.choice(memberlist())
        # self.move =

    def go_school(self):
        return f'{self.student}학생은 000를 타고 학교에 도착했다.' \
               f''
    def bus(self):
        pass
    def subway(self):
        pass
    def taxi(self):
        pass
