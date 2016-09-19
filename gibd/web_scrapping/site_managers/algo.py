#!/usr/bin/env python
import time
from contextlib import closing
from selenium.webdriver import PhantomJS  # pip install selenium
from selenium.webdriver.support.ui import WebDriverWait


def get(url):
    with closing(PhantomJS(executable_path=r".\phantomjs\phantomjs.exe")) as browser:
        browser.get(url)
        time.sleep(7)
        page_source = browser.page_source

    return page_source
