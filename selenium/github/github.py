#! /usr/bin/python3
'''an automation module to retrieve all project from github'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait


def git_clone(link_txt_s: [str]) -> None:
    '''git clone process'''
    # git clone
    git_links = [
        l.replace('https://github.com/', 'git@github.com')
        for l in link_txt_s
        ]
    import subprocess
    import shlex
    cmds = ['git clone %s' % l for l in git_links]
    len_cmds = len(cmds)
    for idx, cmd in enumerate(cmds, start=1):
        print('%d of %d' % (idx, len_cmds))
        git_proc = subprocess.Popen(shlex.split(cmd))
        git_proc.wait()
        sleep(10)


def main() -> int:
    '''retrive all git project'''
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    wait = WebDriverWait(driver, 30)
    driver.get("https://github.com/")
    # login
    signin = driver.find_element_by_css_selector('a.btn-success')
    signin.click()
    username = driver.find_element_by_css_selector('#username')
    username.send_keys('yourusername')
    passw = driver.find_element_by_css_selector('#password')
    passw.send_keys('yourspassword')
    passw.send_keys(Keys.RETURN)

    # get links
    link_txt_s = []
    while True:
        links = driver.find_elements_by_css_selector('a.project')

        link_txt_s += [l.get_attribute('href') for l in links]
        print('%d items avaliable' % len(link_txt_s))
        try:
            nextpg = driver.find_element_by_css_selector('a[rel="next"]')
            print(nextpg.get_attribute('href'))
            nextpg.click()
            wait.until(staleness_of(nextpg))
        except exceptions.NoSuchElementException:
            break
#    git_clone(link_txt_s)

# close driver
    driver.close()
    return 0


if __name__ == '__main__':
    main()
