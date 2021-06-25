from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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


# 测试知网文献检索操作所有交互元素
def test_search_paper(driver):

    # 1. 依次点击所有复选框
    multi_names = [
        'CJFQ', 'CDMD', 'CIPD', 'CCND', 'CYFD', 'SCOD', 'CISD', 'SNAD', 'BDZK'
    ]
    for multi_name in multi_names:
        xpath = '//li[@id="' + multi_name + '"]/i[1]'
        multi = my_find_by_xpath(driver, xpath)
        multi.click()
    #    time.sleep(1)

    # 2. 依次点击下拉框所有按钮
    for i in range(2, 17):
        # 鼠标悬停下拉框才能打开
        field_list = my_find_by_xpath(driver, '//*[@id="DBFieldBox"]/div[1]')
        ActionChains(driver).move_to_element(field_list).perform()
        # 依次点击
        xpath = '//div[@id="DBFieldList"]/ul/li[' + str(i) + ']'
        field_choice = my_find_by_xpath(driver, xpath)
        field_choice.click()
    #   time.sleep(1)

    field_list = my_find_by_xpath(driver, '//*[@id="DBFieldBox"]/div[1]')
    ActionChains(driver).move_to_element(field_list).perform()
    xpath = '//div[@id="DBFieldList"]/ul/li[1]'
    field_choice = my_find_by_xpath(driver, xpath)
    field_choice.click()

    # 3. 输入框为空直接点击搜索按钮 测试对话框
    search_button = my_find_by_xpath(
        driver, '/html/body/div[1]/div[2]/div/div[1]/input[2]')
    search_button.click()

    alert = driver.switch_to_alert()
    time.sleep(1)
    alert.accept()

    # 4. 输入关键词
    input_bar = my_find_by_xpath(driver, '//*[@id="txt_SearchText"]')
    input_bar.send_keys('软件测试')

    # 5. 点击搜索按钮
    search_button = my_find_by_xpath(
        driver, '/html/body/div[1]/div[2]/div/div[1]/input[2]')
    search_button.click()

    # 6. 返回
    driver.back()

    # 7. 点击其他按钮并返回
    multi_names = [
        'CJFQ',
        'CDMD',
        'CIPD',
        'CCND',
        'CYFD',
        'SCOD',
        'CISD',
        'SNAD',
        'BDZK',
        'CLKD',
        'gwkt',
        'scef',
        'kjbg',
        'cgxx'
    ]

    for multi_name in multi_names:
        xpath = '//li[@id="' + multi_name + '"]'
        multi = my_find_by_xpath(driver, xpath)
        multi.click()
        time.sleep(1)

    # 8. 点击搜索按钮右边的两个按钮
    side_button = my_find_by_xpath(driver, '//*[@id="highSearch"]')
    side_button.click()
    side_button = my_find_by_xpath(driver, '/html/body/div[1]/div[2]/div/div[2]/a[2]')
    side_button.click()

    # 9. 返回主界面
    windows = driver.window_handles
    driver.switch_to.window(windows[0])


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.cnki.net/')

test_search_paper(driver)
