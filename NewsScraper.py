from subprocess import call
import time
from selenium import webdriver


def scrape(address):
    driver = webdriver.Chrome()
    driver.execute_script('window.focus()')
    driver.maximize_window()
    driver.get(address)
    time.sleep(4)

    call(["screencapture", "Todays News Screenshot.jpg"])
    driver.close


def main():
    address = raw_input("Enter the url you would like to get a screenshot of: ")
    address = ("https://www.%s" % address)
    scrape(address)


if __name__ == "__main__":
    main()
