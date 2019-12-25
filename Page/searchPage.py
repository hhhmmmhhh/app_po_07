from selenium.webdriver.common.by import By

from Base.base import Base
from Page.pageElements import PageElements


class SearchPage(Base):

    def __init__(self, driver):
        # 实例化Base类
        Base.__init__(self, driver)
        """搜索页面元素"""

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageElements.search_btn)

    def search_text(self, text):
        """
        搜索内容
        :param text: 输入文本内容
        :return:
        """
        self.send_ele(PageElements.search_input, text)

    def ge_search_result(self):
        """
        获取搜索结果
        :return: 列表
        """
        # 定位
        results = self.search_eles(PageElements.search_result)
        # 返回
        return [i.text for i in results]
