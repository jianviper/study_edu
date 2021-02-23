#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
from BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from time import sleep, ctime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class StudyPage(BasePage):
    btn_wx_loc = (By.CLASS_NAME, 'wx-login')
    leftMenu_result_loc = (By.CSS_SELECTOR, '#left_menu_ul>li:nth-child(4)')
    topMenu_study_loc = (By.CSS_SELECTOR, '#menu_tag_ul>li:nth-child(2)')
    link_kecheng_loc = (By.CSS_SELECTOR, '#frame_learning_content_1 #tr_tblDataList_0 a')
    chapter_nums_loc = (By.CSS_SELECTOR, '#_JS_TREE_0_0_SubTree>td:nth-child(3)>table>tbody>tr')

    iframe_loc = (By.NAME, 'w_main')
    f_left_loc = (By.ID, 'w_code')
    f_right_loc = (By.ID, 'w_lms_content')
    f_video1_loc = (By.ID, 'w_sco')
    f_video2_loc = (By.ID, 'w_content')
    f_video3_loc = (By.ID, 'w_sco')
    f2_chapter_loc = (By.CSS_SELECTOR, '.chapter>span')
    f2_chapter_last_loc = (By.CSS_SELECTOR, '.chapter>span:last-child')

    text_loc = (By.CSS_SELECTOR, 'body>table>tbody>tr:last-child>td>table>tbody>tr>td')

    def open(self):
        self._open(self.baseurl)

    def login_wx(self):  #切换到微信登录
        self.find_element(*self.btn_wx_loc).click()
        sleep(8)
        # self.wait_login()

    def go_online_study(self):
        self.find_element(*self.leftMenu_result_loc).click()

    def click_menu_study(self, id=0):  #进入在线学习
        # self.find_element(*self.menu_online_loc).click()
        # btn_start_loc = (By.CSS_SELECTOR, '#tr_tblDataList_{0}>td:nth-child(8)>a:first-child'.format(id))
        # el_idt = self.find_element(*btn_start_loc).get_attribute('onclick')
        # el_id = el_idt[4:-2]
        # url1 = 'http://learning.uestcedu.com/learning3/console/?urlto='
        # url2 = 'http://learning.uestcedu.com/learning3/course/course_learning.jsp?course_id={
        # 0}&course_name=&0.5510414015524125'.format(id)
        # self.driver.get(url1 + url2)
        sleep(3)

    def switch_to_a(self):  #切换到弹窗
        # i = 0
        # while (not self.driver.switch_to.alert):
        #     sleep(2)
        #     i += 1
        #     if i > 5: break
        Alert(self.driver).accept()
        # al = self.driver.switch_to.alert
        # al.accept()
        sleep(2)

    def go_study(self, i):
        btn_start_loc = (By.CSS_SELECTOR, '#tr_tblDataList_{0}>td:nth-child(8)>a:first-child'.format(i))
        self.find_element(*btn_start_loc).click()
        sleep(2)

    def switch_to_w(self):
        whs = self.driver.window_handles
        if len(whs) > 1:
            self.driver.switch_to.window(whs[1])
        sleep(3)

    def switch_to_f(self, el):  #切换iframe
        self.driver.switch_to.frame(self.find_element(*el))
        sleep(2)
    def switch_to_p(self):
        self.driver.switch_to.parent_frame()
        sleep(1)

    def click_kecheng(self):
        self.find_element(*self.link_kecheng_loc).click()
        sleep(3)

    def get_chapter_nums(self) -> int:
        chapter_nums = 1
        page_source = self.driver.page_source
        if self.find_element(*self.chapter_nums_loc):
            chapter_nums = len(self.find_elements(*self.chapter_nums_loc))
            for i in range(0, chapter_nums):
                if '_JS_TREE_0_0_{0}_SubTree'.format(i) in page_source:
                    chapter_nums -= 1
        return chapter_nums

    def click_chapter(self, num):  #点击章
        chapter = (By.ID, '_JS_TREE_0_0_{0}'.format(num))
        print('【{0}】'.format(ctime()), self.find_element(*chapter).text)
        print('_JS_TREE_0_0_{0}'.format(num))
        self.find_element(*chapter).click()
        sleep(2)

    def get_items(self, num):  #获取节数
        mulu = (By.CSS_SELECTOR, '#_JS_TREE_0_0_{0}+tr>:last-child>table>tbody>tr'.format(num))
        if (self.find_element(*mulu)):
            return len(self.find_elements(*mulu))
        else:
            return 0

    def get_subTree(self, num1, count) -> int:  #获取节下面还有子目录的节的数量
        sum = 0
        page_source = self.driver.page_source
        for i in range(0, count):
            #subTree_loc = (By.ID, '_JS_TREE_0_0_{0}_{1}_SubTree'.format(num1, i))
            # if self.driver.find_element_by_id('_JS_TREE_0_0_{0}_{1}_SubTree'.format(num1, i)):
            #if self.driver.find_element(*subTree_loc):
            if '_JS_TREE_0_0_{0}_{1}_SubTree'.format(num1, i) in page_source:
                sum += 1
        print('sum:{0}'.format(sum))
        return sum

    def get_sonSection(self, num1, num2):  #节的下级目录
        subTree_loc = (By.ID, '_JS_TREE_0_0_{0}_{1}_SubTree'.format(num1, num2))
        tree_loc = (By.CSS_SELECTOR, '#_JS_TREE_0_0_{0}_{1}_SubTree tr'.format(num1, num2))
        if self.find_element(*subTree_loc):
            return len(self.find_elements(*tree_loc))
        return False

    def get_sonTree(self, num1, num2, count):
        sum = 0
        page_source = self.driver.page_source
        for i in range(0, count):
            pass

    def get_sonSonTree(self, num1, num2, num3):  #节的下级的下级
        s_subTree_loc = (By.ID, '_JS_TREE_0_0_{0}_{1}_{2}_SubTree'.format(num1, num2, num3))
        treeTree = (By.CSS_SELECTOR, '#_JS_TREE_0_0_{0}_{1}_{2}_SubTree tr'.format(num1, num2, num3))
        if self.find_element(*s_subTree_loc):
            return len(self.find_elements(*treeTree))
        return False

    def click_section(self, num1, num2):  #点击节
        # mulu = (By.CSS_SELECTOR, '#_JS_TREE_0_0_{0}+tr>:last-child>table>tbody>tr:nth-child({1})'.format(num1, num2))
        mulu = (By.ID, '_JS_TREE_0_0_{0}_{1}_text'.format(num1, num2))
        print('【{0}】'.format(ctime()), self.find_element(*mulu).text)
        print('_JS_TREE_0_0_{0}_{1}_text'.format(num1, num2))
        self.find_element(*mulu).click()
        sleep(2)

    def click_section2(self, num1, num2, i):  #点击节下的子目录
        subTree_loc = (By.ID, '_JS_TREE_0_0_{0}_{1}_{2}'.format(num1, num2, i))
        print('【{0}】'.format(ctime()), self.find_element(*subTree_loc).text)
        print('_JS_TREE_0_0_{0}_{1}_{2}'.format(num1, num2, i))
        self.find_element(*subTree_loc).click()
        sleep(2)

    def click_sonSection2(self, num1, num2, num3, n):  #点击节的下级的下级
        sonTree2_loc = (By.ID, '_JS_TREE_0_0_{0}_{1}_{2}_{3}'.format(num1, num2, num3, n))
        print('【{0}】'.format(ctime()), self.find_element(*sonTree2_loc).text)
        print('_JS_TREE_0_0_{0}_{1}_{2}_{3}'.format(num1, num2, num3, n))
        self.find_element(*sonTree2_loc).click()
        sleep(2)

    def get_text(self):
        return str(self.find_element(*self.text_loc).text)

    def wait_study(self):
        i = 0
        if self.get_text().find('累计获取0') >= 0:
            #-------多个视频进入最后一个视频--------
            self.switch_to_f(self.f_video1_loc)  #切到播放视频的iframe
            self.switch_to_f(self.f_video2_loc)  #切到播放视频的iframe
            self.switch_to_f(self.f_video3_loc)  #切到播放视频的iframe
            if self.find_element(*self.f2_chapter_loc):
                if len(self.find_elements(*self.f2_chapter_loc)) > 1:
                    self.find_element(*self.f2_chapter_last_loc).click()
                    sleep(2)
            self.switch_to_p()
            self.switch_to_p()
            self.switch_to_p()
            #------------------------------------
        while (self.get_text().find('累计获取0') >= 0):
            if EC.alert_is_present()(self.driver):
                self.switch_to_a()
            sleep(5)
            if EC.alert_is_present()(self.driver):
                self.switch_to_a()
            i += 1
            if i > 25:
                break
        else:
            print('【{0}】'.format(ctime()), self.get_text())

    def wait_login(self):
        i = 0
        while ('电子科技大学继续教育学院、网络教育学院、职业教育学院学生平台' != self.driver.title):
            sleep(2)
            i += 1
            if i > 10:
                break
        print(self.driver.title)
