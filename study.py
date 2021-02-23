#!/usr/bin/env python
#coding:utf-8
import unittest
from studyPage import StudyPage
from time import sleep, ctime


class CDNrefresh(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'https://student.uestcedu.com/console/'
        self.s_PO = StudyPage(base_url=self.url)
        self.s_PO.open()

    def tearDown(self) -> None:
        self.s_PO.driver.quit()

    def test_s(self):
        self.s_PO.login_wx()
        # print(self.s_PO.driver.title)
        sleep(10)
        whs = self.s_PO.driver.window_handles
        if len(whs) > 1:
            self.s_PO.driver.switch_to.window(whs[1])
            sleep(3)
        self.s_PO.switch_to_f(self.s_PO.iframe_loc)  #切换到主iframe
        self.s_PO.switch_to_f(self.s_PO.f_left_loc)  #切换到左侧
        section_count = 0
        max = self.s_PO.get_chapter_nums()
        print('max:{0}'.format(max))
        for i in range(0, max):  #章，实际+1
            self.s_PO.click_chapter(i)  #进入章
            section_count = self.s_PO.get_items(i)  #节数量
            if section_count:
                st = self.s_PO.get_subTree(i, section_count)
                section_count = section_count - st  #数量减掉节下面还有子级的节
                print('section_count:{0}'.format(section_count))
            else:  #只有章的情况
                self.s_PO.switch_to_p()
                self.s_PO.switch_to_f(self.s_PO.f_right_loc)  #切换到右侧
                self.s_PO.wait_study()  #等待学习时间到
                self.s_PO.switch_to_p()
                self.s_PO.switch_to_f(self.s_PO.f_left_loc)  #切换到左侧
                continue
            for j in range(0, section_count):  #节
                self.s_PO.click_section(i, j)
                trees = self.s_PO.get_sonSection(i, j)  #节的子级数量
                print('tress:{0}-{1}-{2}'.format(trees, i, j))
                if trees:  #节下面还有子目录
                    ttrees = 0
                    for m in range(0, trees):
                        if trees > ttrees and m > trees - ttrees - 1:
                            break
                        self.s_PO.click_section2(i, j, m)
                        ts = self.s_PO.get_sonSonTree(i, j, m)  #节的子级的子级的数量
                        print('treetree:{0}-{1}-{2}-{3}'.format(ttrees, i, j, m))
                        if ts:  #节下面的目录还有子级目录
                            ttrees = ttrees + ts
                            for n in range(0, ts):
                                self.s_PO.click_sonSection2(i, j, m, n)
                                self.s_PO.switch_to_p()
                                self.s_PO.switch_to_f(self.s_PO.f_right_loc)  #切换到右侧
                                self.s_PO.wait_study()
                                self.s_PO.switch_to_p()
                                self.s_PO.switch_to_f(self.s_PO.f_left_loc)  #切换到左侧
                        else:
                            self.s_PO.switch_to_p()
                            self.s_PO.switch_to_f(self.s_PO.f_right_loc)  #切换到右侧
                            self.s_PO.wait_study()
                            self.s_PO.switch_to_p()
                            self.s_PO.switch_to_f(self.s_PO.f_left_loc)  #切换到左侧
                else:
                    self.s_PO.switch_to_p()
                    self.s_PO.switch_to_f(self.s_PO.f_right_loc)  #切换到右侧
                    self.s_PO.wait_study()  #等待学习时间到
                    self.s_PO.switch_to_p()
                    self.s_PO.switch_to_f(self.s_PO.f_left_loc)  #切换到左侧

        sleep(3)


if __name__ == '__main__':
    unittest.main()
