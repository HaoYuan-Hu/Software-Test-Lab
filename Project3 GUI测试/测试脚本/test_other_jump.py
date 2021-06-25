from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def my_find_by_id(driver, id):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.ID, id)))
    element = driver.find_element_by_id(id)

    return element


def my_find_by_class_name(driver, class_name):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    element = driver.find_element_by_class_name(class_name)

    return element


def my_find_by_xpath(driver, xpath):
    WebDriverWait(driver,
                  10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    element = driver.find_element_by_xpath(xpath)

    return element


def open_and_close(driver, xpath):
    link = my_find_by_xpath(driver, xpath)
    link.click()

    time.sleep(2)

    windows = driver.window_handles
    driver.switch_to.window(windows[1])
    driver.close()

    windows = driver.window_handles
    driver.switch_to.window(windows[0])


def test_other_jump(driver):
    driver.maximize_window()
    # 测试页表中其他跳转超链接
    # 1. 行业知识服务与知识管理平台
    open_and_close(driver, '/html/body/div[1]/div[3]/div[1]/ul/li[1]/h6/a[1]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[1]/ul/li[1]/h6/a[2]')

    count = [0, 12, 9, 13, 11, 12]
    for i in range(2, 7):
        for j in range(1, count[i - 1] + 1):
            print(i, j)
            xpath = ' /html/body/div[1]/div[3]/div[1]/ul/li[' + str(i) + ']/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    # 2. 研究学习平台
    count = [6, 8]
    for i in range(1, 3):
        for j in range(1, count[i - 1] + 1):
            xpath = '/html/body/div[1]/div[3]/div[2]/dl[1]/dd/ul/li[' + str(i) + ']/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    count = [3, 3]
    for i in range(3, 5):
        for j in range(1, count[i - 3] + 1):
            xpath = '/html/body/div[1]/div[3]/div[2]/dl[1]/dd/ul/li[' + str(i) + ']/h6/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/map/area[1]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/map/area[2]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/map/area[3]')

    count = [9, 9]
    for i in range(1, 3):
        for j in range(1, count[i - 1] + 1):
            xpath = '/html/body/div[1]/div[3]/div[2]/dl[2]/dd/ul/li[' + str(i) + ']/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/dl[2]/dd/ul/li[2]/h6/a')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/dl[2]/dd/ul/li[3]/h6/a')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[2]/dl[2]/dd/ul/li[4]/h6/a')

    # # 3. 专题知识库

    open_and_close(driver, '/html/body/div[1]/div[3]/div[3]/ul/li[1]/h6/div/a[1]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[3]/ul/li[1]/h6/div/a[2]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[3]/ul/li[1]/h6/a[1]')
    open_and_close(driver, '/html/body/div[1]/div[3]/div[3]/ul/li[1]/h6/a[2]')

    count = [13, 12, 6]
    for i in range(2, 5):
        for j in range(1, count[i - 2] + 1):
            print(i, j)
            xpath = '/html/body/div[1]/div[3]/div[3]/ul/li[' + str(i) + ']/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    count = [2, 3]
    for i in range(5, 7):
        for j in range(1, count[i - 5] + 1):
            print(i, j)
            xpath = '/html/body/div[1]/div[3]/div[3]/ul/li[' + str(i) + ']/h6/span/a[' + str(j) + ']'
            open_and_close(driver, xpath)

    for i in range(7, 8):
        for j in range(1, 5):
            xpath = '/html/body/div[1]/div[3]/div[3]/ul/li[' + str(i) + ']/a[' + str(j) + ']'
            open_and_close(driver, xpath)


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.cnki.net/')

test_other_jump(driver)