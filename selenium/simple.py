'''selenium web model

Author: brucelau.email@gmail.com
Date: Dec 2017
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
    main()
