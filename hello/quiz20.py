import random
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

from hello import Quiz00
from hello.domains import memberlist, myRandom, my100


class Quiz20:

    def quiz20list(self) -> str:
        print('#'*30)
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])

        list3 = [1, '2', [1, 2, 3, ]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2:] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)
        print()
        print('#' * 30)

        return None

    def quiz21tuple(self) -> str:
        print('#' * 30)



        print('#' * 30)
        return None

    def quiz22dict(self) -> str:
        print('#' * 30)

        print('#' * 30)
        return None

    def quiz23listcom(self) -> str:
        print('-----------------legacy----------------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('-----------------Comprension----------------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> {}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        cls_names = ['artist', 'titles']
        # a = [i for i in cls_names]
        ls1 = self.music_chart(soup, 'title')
        ls2 = self.music_chart(soup, 'artist')
        dt = {i:j for i,j in zip(ls1, ls2)}
        l = [i + j for i, j in zip(ls1, ls2)]
        l2 = list(zip(ls1, ls2))
        d1 = dict(zip(ls1, ls2))
        print(d1)
        # self.dict1(ls1, ls2)
        # self.dict2(ls1,ls2)
        # self.dict3(ls1, ls2)

    @staticmethod
    def dict1(ls1, ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2) -> None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    @staticmethod
    def dict3(ls1, ls2) -> None:
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        print(dict)


    def print_music_list(self,soup) -> None:
        artist = soup.find_all('p', {'class':'artist'})
        artist = [i.get_text() for i in artist]
        titles = soup.find_all('p', {'class':'titles'})
        titles = [i.get_text() for i in titles]
        print(''.join(i for i in titles))
        return None

    def find_rank(self, soup) -> None:
        for i, j in enumerate(['artist', 'titles']):
            for i, j in enumerate(self.music_chart(soup, j)):
                print(f'{i}위: {j}')
        return None

    @staticmethod
    def music_chart(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('p', {'class': cls_nm})]

    def quiz25dictcom(self) -> {}:
        # students quiz06memberChoice() 를 import 해서 5명 추출
        # scores 는 0 ~ 100점 사이에서 랜덤
        # students = [memberlist()[i] for i in random.sample(range(0,23),5)]
        q = Quiz00()
        students = set([q.quiz06member_choice() for i in range(5)])
        scores = [my100() for i in range(5)]
        while len(students) != 5:
            students.add(q.quiz06member_choice())
        students = list(students)
        # print(dict(zip(students, scores)))
        return print({i:j for i, j in zip(students, scores)})

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        ls1 = self.melon_music_chart(soup, 'ellipsis rank01')
        ls2 = self.melon_music_chart2(soup, 'checkEllipsis')
        dict = {}
        for i, j in zip(ls1, ls2):
            dict[i] = j
        df = pd.DataFrame.from_dict(dict, orient='index')
        df.to_csv('./save/melon.csv', sep=',', na_rep='NaN')

        return dict

        return None

    @staticmethod
    def melon_music_chart(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('div',{'class': cls_nm})]

    @staticmethod
    def melon_music_chart2(soup, cls_nm) -> []:
        return [i.get_text().strip() for i in soup.find_all('span',{'class': cls_nm})]

    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')

    '''
    다음 결과 출력
        a   b   c
    1   1   3   5
    2   2   4   6
    '''

    def quiz29_pandas_01(self) -> object:
        odds = []
        evens = []
        [odds.append(i) if i % 2 == 1 else evens.append(i) for i in range(1, 7)]
        columns = [chr(i) for i in range(97, 100)]
        d = {'1': odds, '2': evens}
        # d1 = {'1': odds}
        # d2 = {'2': evens}
        # d3 = dict(d1, **d2) 딕셔너리 합치는 방법

        df1 = pd.DataFrame.from_dict(d, orient='index', columns=columns)
        '''
            a   b   c
        1   1   3   5
        2   2   4   6
        '''
        df2 = pd.DataFrame.from_dict(d)
        '''
           1  2
        0  1  2
        1  3  4
        2  5  6
        '''
        df3 = pd.DataFrame.from_dict(d, orient='index')
        '''
           0  1  2
        1  1  3  5
        2  2  4  6
        '''
        df4 = pd.DataFrame.from_dict(d, orient='index', columns=['A', 'B', 'C'])
        '''
           A  B  C
        1  1  3  5
        2  2  4  6
        '''
        df5 = pd.DataFrame.from_dict(d, orient='index', columns=columns)
        print(df5)

        return None