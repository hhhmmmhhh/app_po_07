from Page.settingPage import SettingPage
from Page.morePage import MorePage
from Page.mobilePage import MobilePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_setting_page(self):
        return SettingPage(self.driver)

    def get_more_page(self):
        return MorePage(self.driver)

    def get_mobile_page(self):
        return MobilePage(self.driver)
