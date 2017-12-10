'''this module is to make auto send resume on indeed website
thing to do:
    1. login
    2. search key job
    3. fill form
    4. send resume
'''
import sys
import configparser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Indeed(object):
    '''an web site object'''
    def __init__(self, driver: webdriver, config: configparser.ConfigParser):
        '''give driver'''
        self.driver = driver
        self.config = config

    def _login(self, username: str, password: str) -> None:
        '''internal login with username and password'''
        driver = self.driver
        config = self.config
        username_box = driver.find_element_by_id(config.get('username', 'id'))
        password_box = driver.find_element_by_id(config.get('password', 'id'))
        username_box.send_keys(username)
        password_box.send_keys(password)
        sign_btn = driver.find_element_by_class(config.get('signin-btn',
                                                           'bt-sign'))
        sign_btn.click()

    def login(self):
        '''login with config'''
        config = self.config
        self._login(config.get('user-info', 'username'),
                    config.get('user-info', 'password'))

    def logout(self):
        '''logout user'''
        driver = self.driver
        config = self.config
        profile_nav = driver.find_element_by_text_link('Sign out')





def main() -> int:
    '''a simple example of using selenium'''
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
