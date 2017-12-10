# how to use selenium package

auto testing on browser

## dowload python package

```sh
$ pip3 install selenium
```

### install webdriver

[geckodriver](https://github.com/mozilla/geckodriver/releases)

run it at background
 ```sh
 $ geckodriver &
 ```

### writing your code

```py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
```

[tutorial
link](http://selenium-python.readthedocs.io/getting-started.html#simple-usage)
