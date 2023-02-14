from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd
import re
import random

def get_driver_instance():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    return driver

def get_page(driver, url):
    driver.get(url)
    title = driver.title
    print(title)
    driver.implicitly_wait(2.0)
    time.sleep(1.0)
    frame = driver.find_element(By.ID, "youzy_part_view")
    if not frame:
        return
    #print(frame)

    driver.switch_to.frame("youzy_part_view")

    time.sleep(1.0)
    total_num = driver.find_element(By.CLASS_NAME, "total-num")

    print(total_num.text)
    time.sleep(1.0)

    tab_first = driver.find_element(By.ID, "tab-first")
    tab_second = driver.find_element(By.ID, "tab-second")
    tab_third = driver.find_element(By.ID, "tab-third")

    ActionChains(driver)\
        .click(tab_first)\
        .perform()

    print("clicked")
    while True:
        col_ele = driver.find_element(By.CLASS_NAME, "colleges-list-component")
        print(col_ele.rect)
        scroll_origin = ScrollOrigin.from_element(col_ele, 0, -20)

        ActionChains(driver).scroll_from_origin(scroll_origin, 0, 600).perform()

        #footer = driver.find_element(By.TAG_NAME, "footer")
        #delta_y = footer.rect['y']
        ActionChains(driver)\
            .scroll_by_amount(0, 20)\
            .perform()
        #js="window.scrollTo(0,document.body.scrollHeight)"
        #driver.execute_script(js)
        #driver.implicitly_wait(10.0)
        print("scroll")
        r_sleep = float(random.randint(500, 2200))/1000.00

        print(r_sleep)
        time.sleep(r_sleep)
        #s = BeautifulSoup(driver.page_source, 'lxml')
        #print(s)

        col_list = driver.find_elements(By.CLASS_NAME, "college-list")
        print(len(col_list))
        if len(col_list) == int(total_num.text):
            print("get all")
            break

        
    return s

def get_colleges(s):
    #c = c.find_all("li")
    #x = list(map(lambda x: x.select("li > a")[0].get_text(), c))
    #y = list(map(lambda x: x.get("id"), c))    
    #return list(zip(x, y))
    return list()

def get_one_cat_items(tds):
    href = tds[0].select("a")[0].get("href")
    name = tds[0].select("a")[0].get_text()
    company_number = tds[1].get_text()
    avg_price = tds[2].select("span")[0].get_text()
    diff_value = tds[3].select("span")[0].get_text()
    diff_percent = tds[4].select("span")[0].get_text()
    volume_batch = tds[5].get_text()
    volume_value = tds[6].get_text()

    leader_name = tds[7].select("a")[0].get_text()
    leader_symbol = tds[7].get_text()
    m = re.match("^.*\((.*)\)$", leader_symbol)
    leader_symbol = m.group(1)

    leader_diff_value = tds[8].select("span")[0].get_text()
    leader_current_price = tds[9].select("span")[0].get_text()
    leader_diff_ratio = tds[10].select("span")[0].get_text()
    
    r = (name, company_number, avg_price, diff_value, diff_percent, volume_batch, volume_batch, leader_name, leader_symbol, leader_diff_ratio, leader_current_price, leader_diff_value)
    return r

def get_one_cat(driver, cat):
    one_cat = driver.find_element(By.CSS_SELECTOR, "#" + cat[1])
    if not one_cat:
        return
    driver.implicitly_wait(10.0)
    time.sleep(1.0)
    one_cat.click()
    time.sleep(0.5)
    driver.implicitly_wait(10.0)
    s = BeautifulSoup(driver.page_source, 'lxml')
    s = s.find_all("div", class_="tblOuter")
    s = s[0].select("tbody>tr")
    items = []
    for i in s:
        d = i.find_all("td")
        items.append(get_one_cat_items(d))
    return items
    

if __name__ == "__main__":
    driver = get_driver_instance()
    url = "https://youzy.cn/tzy/search/colleges/collegeList"
    s = get_page(driver, url)
    cols = get_colleges(s)
    time.sleep(1) 
    #for cat in cats:
    #    print(cat)
    #    items = get_one_cat(driver, cat)
    #    print(len(items))
    #    cols = ["name", "companys", "avg_price", "diff_price", "diff_ratio", "volume_units", "volume_value", "leader_name", "leader_symbol", "leader_diff_ratio", "leader_current_price", "leader_diff_price"]
     #   dataframe = pd.DataFrame(columns=cols, data=items)
     #   print(dataframe)
     #   dataframe.to_csv(cat[0] + ".csv")
    #driver.quit()
        

