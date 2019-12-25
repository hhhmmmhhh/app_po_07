from Base.base import Base
from Page.pageElements import PageElements


class MobilePage(Base):

    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_mobile_btn(self):
        self.click_ele(PageElements.mobile_one_network_xpath)

    def click_2G_btn(self):
        self.click_ele(PageElements.mobile_select_2G_btn_xpath)

    def show_result(self):
        results = self.search_eles(PageElements.mobile_get_summary_text_ids)
        return [i.text for i in results]
