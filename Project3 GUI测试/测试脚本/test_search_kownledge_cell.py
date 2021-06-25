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


def test_search_knowledge_cell(driver):
    # 1. 切换到知识元检索
    knowledge_cell = my_find_by_xpath(driver, '/html/body/div[1]/div[2]/ul/li[2]')
    knowledge_cell.click()

    # 2. 测试单选框 依次点击所有单选框
    single_names = ['CRPD', 'CRDD', 'CRMD', 'CRFD', 'IMAGE', 'CSYD', 'CIDX', 'METHOD', 'CONC']
    for single_name in single_names:
        xpath = '//li[@id="' + single_name + '"]/i'
        single = my_find_by_xpath(driver, xpath)
        single.click()

        # time.sleep(1)

    # 3. 测试下方按钮 依次点击
    for single_name in single_names:
        xpath = '//li[@id="' + single_name + '"]'
        single = my_find_by_xpath(driver, xpath)
        single.click()

    # 4. 测试右侧按钮 依次点击
    side_button = my_find_by_xpath(driver, '/html/body/div[1]/div[2]/div/div[2]/a[2]')
    side_button.click()

    # 5. 切换到主界面
    windows = driver.window_handles
    driver.switch_to.window(windows[0])

    # 6. 测试对话框 输入框为空直接点击搜索按钮
    search_button = my_find_by_xpath(
        driver, '/html/body/div[1]/div[2]/div/div[1]/input[2]')
    search_button.click()

    alert = driver.switch_to_alert()
    time.sleep(1)
    alert.accept()

    # 7. 测试输入框 输入关键词到输入框
    input_bar = my_find_by_xpath(driver, '//*[@id="txt_SearchText"]')
    input_bar.send_keys('软件测试')

    # 8. 测试搜索按钮 点击搜索按钮
    search_button = my_find_by_xpath(
        driver, '/html/body/div[1]/div[2]/div/div[1]/input[2]')
    search_button.click()
    time.sleep(2)

    # 9. 切换到主界面
    windows = driver.window_handles
    driver.switch_to.window(windows[0])


chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.cnki.net/')
test_search_knowledge_cell(driver)
