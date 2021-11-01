import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--window-size=1024x730")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/chromedriver/chromedriver.exe')
url = "https://www.pinterest.com/anhthuhoang1804/anime-boy/"
driver.get(url)
time.sleep(3)
Height = driver.execute_script("return document.body.scrollHeight")
preHeight = 0
while preHeight < Height:
    preHeight = Height
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    Height = driver.execute_script("return document.body.scrollHeight")
    time.sleep(4)