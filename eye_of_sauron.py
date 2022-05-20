from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


PATH = '/Users/zhandosmanapov/Desktop/search_engine/chromedriver'
option_Chr = webdriver.ChromeOptions()
option_Chr.add_argument('headless')

def get_result(query):
    query = query.replace(' ', '+')
    driver = webdriver.Chrome(PATH, options=option_Chr)
    driver.get('http://www.google.com/search?q=' + query)

    answer = driver.execute_script(
        "return document.elementFromPoint(arguments[0], arguments[1]);",
        350, 230).text

    # execute_script("return document.elementFromPoint(350, 230);").text
    
    try:
        answer += "\n" + driver.find_element(by=By.XPATH, value='//div[@data-dobid="dfn"]/span').text
    except: pass

    return answer

question = input('Enter your question: ')

while question:
    print(get_result(question))
    question = input('Enter your question: ')