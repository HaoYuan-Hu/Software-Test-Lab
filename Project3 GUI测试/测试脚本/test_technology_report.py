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

# 测试科技报告页面的表单格式的搜索
def test_technology_report(driver):
    # 1. 打开科技报告页面
    open_button = my_find_by_xpath(driver, '//*[@id="kjbg"]/a')
    open_button.click()

    time.sleep(5)

    windows = driver.window_handles
    driver.switch_to.window(windows[1])

    # 2. 测试左侧复选框
    # 测试全选按钮
    clear_all_button = my_find_by_xpath(driver, '//*[@id="clear_all"]')
    clear_all_button.click()

    time.sleep(1)

    # 测试清除按钮
    select_all_button = my_find_by_xpath(driver, '//*[@id="select_all"]')
    select_all_button.click()

    time.sleep(1)

    # 依次点击每个复选框
    left_names = ['A001', 'A002', 'A003', 'A004', 'A005']
    for left_name in left_names:
        xpath = '//*[@id="' + left_name + '"]/span/input'
        left_button = my_find_by_xpath(driver, xpath)
        left_button.click()

    time.sleep(1)

    for left_name in left_names:
        xpath = '//*[@id="' + left_name + '"]/span/input'
        left_button = my_find_by_xpath(driver, xpath)
        left_button.click()

    # 3. 测试加减表单项
    insert_button = my_find_by_xpath(driver, '//*[@id="txt_1"]/td[1]/a[1]')
    insert_button.click()

    time.sleep(2)

    remove_button = my_find_by_xpath(driver, '//*[@id="txt_1"]/td[1]/a[2]')
    remove_button.click()

    time.sleep(2)
    
    remove_button.click()

    time.sleep(2)

    # 4. 测试表单
    # 依次填写表单内容
    sel_list = my_find_by_xpath(driver, '//*[@id="txt_1_sel"]')
    for i in range(1, 8):
        sel_list.click()

        time.sleep(1)

        xpath = '//*[@id="txt_1_sel"]/option[' + str(i) + ']'
        header_choice = my_find_by_xpath(driver, xpath)
        header_choice.click()

        time.sleep(1)

    sel_list.click()

    xpath = '//*[@id="txt_1_sel"]/option[1]'
    header_choice = my_find_by_xpath(driver, xpath)
    header_choice.click()

    relation_list = my_find_by_xpath(driver, '//*[@id="txt_1_relation"]')
    for i in range(1, 4):
        relation_list.click()

        time.sleep(1)

        xpath = '//*[@id="txt_1_relation"]/option[' + str(i) + ']'
        relation_choice = my_find_by_xpath(driver, xpath)
        relation_choice.click()

        time.sleep(1)

    relation_list.click()

    xpath = '//*[@id="txt_1_relation"]/option[1]'
    relation_choice = my_find_by_xpath(driver, xpath)
    relation_choice.click()

    special_list = my_find_by_xpath(driver, '//*[@id="txt_1_special1"]')
    special_list.click()
    special_choice = my_find_by_xpath(driver, '//*[@id="txt_1_special1"]/option[1]')
    special_choice.click()

    input_bar1 = my_find_by_xpath(driver, '//*[@id="txt_1_value1"]')
    input_bar1.send_keys('heat')

    input_bar2 = my_find_by_xpath(driver, '//*[@id="txt_1_value2"]')
    input_bar2.send_keys('Illness')

    start_year = my_find_by_xpath(driver, '//*[@id="year_from"]')
    for i in range(1, 47):
        start_year.click()

        xpath = '//*[@id="year_from"]/option[' + str(i) + ']'
        start_year_choice = my_find_by_xpath(driver, xpath)
        start_year_choice.click()

    start_year.click()
    xpath = '//*[@id="year_from"]/option[2]'
    start_year_choice = my_find_by_xpath(driver, xpath)
    start_year_choice.click()

    end_year = my_find_by_xpath(driver, '//*[@id="year_to"]')
    for i in range(1, 47):
        end_year.click()

        xpath = '//*[@id="year_to"]/option[' + str(i) + ']'
        end_year_choice = my_find_by_xpath(driver, xpath)
        end_year_choice.click()

    end_year.click()
    xpath = '//*[@id="year_to"]/option[2]'
    end_year_choice = my_find_by_xpath(driver, xpath)
    end_year_choice.click()

    side_button2 = my_find_by_xpath(driver, '//*[@id="txt_extensionCKB_R"]')
    side_button2.click()

    side_button1 = my_find_by_xpath(driver, '//*[@id="txt_extensionCKB"]')
    side_button1.click()

    # 3. 提交表单
    submit_button = my_find_by_xpath(driver, '//*[@id="btnSearch"]')
    submit_button.click()


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.cnki.net/')

test_technology_report(driver)