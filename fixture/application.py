from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
__author__ = 'ioK'


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
        #
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
