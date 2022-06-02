from study.baekjoon import Baekjoon
from study.school import School

if __name__ == '__main__':
    q1 = School()
    b = Baekjoon()
    while 1:
        menu = input('1,가진돈 2.백준문풀(1)')
        if menu == '1': q1.taxi()
        elif menu == '2': b.quiz01()
