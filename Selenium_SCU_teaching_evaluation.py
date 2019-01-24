# Author: Shreck Ye
# Date: 2019/1/24
# GitHub repository: https://github.com/ShreckYe/Selenium-SCU-teaching-evaluation
from selenium import webdriver
import time
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

print(
    "欢迎使用四川大学新版教务系统评教脚本。\n在运行脚本前请确保已安装Chrome浏览器、Python 3、Selenium包和浏览器Driver。\n若你不熟悉Python语言的使用，请在使用本脚本前阅读README（https://github.com/ShreckYe/Selenium-SCU-teaching-evaluation/blob/master/README.md）。")

browser = webdriver.Chrome()

browser.get("http://zhjw.scu.edu.cn")
while True:
    input_username = browser.find_element_by_id("input_username")
    username = input("输入学号：")
    input_username.send_keys(username)

    input_password = browser.find_element_by_id("input_password")
    password = input("输入密码：")
    input_password.send_keys(password)

    input_checkcode = browser.find_element_by_id("input_checkcode")
    checkcode = input("请对照浏览器窗口输入验证码：")
    input_checkcode.send_keys(checkcode)

    login_button = browser.find_element_by_id("loginButton")
    login_button.click()

    if browser.current_url == "http://zhjw.scu.edu.cn/index.jsp":
        break
    else:
        print("登录失败，请重新输入。")

# 进入评教页面
browser.get("http://zhjw.scu.edu.cn/student/teachingEvaluation/evaluation/index")
WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.ID, 'page_div')))
print("评教页面打开成功。")
subjective = input("请输入统一的主观评价（如：“老师认真负责。”）：")

while True:
    try:
        evaluation_button = browser.find_element_by_class_name("btn-purple")
    except NoSuchElementException:
        print("所有评教已完成。")
        break
    evaluation_button.click()
    # choices = browser.find_elements_by_xpath("//span[contains(text(),'非常同意')]")
    choices = browser.find_elements_by_xpath("//span[contains(text(),'A')]")
    # choices = browser.find_elements_by_xpath("//input[@value='10_1']")
    for choice in choices:
        choice.click()

    input_subjective = browser.find_element_by_name("zgpj")
    input_subjective.send_keys(subjective)

    print("自动等待2分30秒后提交，你可在这2分30秒内手动修改评教内容，但请不要进行其他操作。")
    time.sleep(150)

    # button_submit = browser.find_element_by_id("buttonSubmit")
    # button_submit.click()
    browser.execute_script("toEvaluation()")
    WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located((By.ID, 'page_div')))

    print("提交成功。")
