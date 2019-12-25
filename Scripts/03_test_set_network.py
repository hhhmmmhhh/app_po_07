import pytest, sys, os

sys.path.append(os.getcwd())
from Base.page import Page
from Base.getDriver import get_android_driver


class TestSetNetwork:

    def setup_class(self):
        self.driver = get_android_driver('com.android.settings', '.Settings')
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.fixture(scope="class", autouse=True)
    def goto_set_network_page(self):
        self.page_obj.get_setting_page().click_more_btn()
        self.page_obj.get_more_page().click_mobile_btn()

    def test_set_network(self):
        self.page_obj.get_mobile_page().click_mobile_btn()
        self.page_obj.get_mobile_page().click_2G_btn()

        assert "2G" in self.page_obj.get_mobile_page().show_result()
