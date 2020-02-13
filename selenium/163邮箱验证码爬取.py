import time

from selenium import webdriver
import requests,os

driver = webdriver.Chrome()

driver.get('http://mail.163.com')
driver.implicitly_wait(2)


driver.find_element_by_id("switchAccountLogin").click()
xpath = "//iframe[contains(@id, 'x-URS-iframe')]"

driver.switch_to.frame(driver.find_element_by_xpath(xpath))

email = driver.find_element_by_name('email')

email.send_keys('lelian8851')

password = driver.find_element_by_name('password')

password.send_keys('qiej88')

driver.find_element_by_id("dologin").click()

driver.find_element_by_class_name("yidun_tips").click()
i = 2
while i<500:
    time.sleep(1)
    url = driver.find_element_by_class_name("yidun_bg-img").get_attribute('src')
    print(url)
    print(i)
    r = requests.get(url)

    name = str(i) + ".png"
    with open(name, 'wb') as f:
        # 对于图片类型的通过r.content方式访问响应内容，将响应内容写入baidu.png中
        f.write(r.content)
    i+=1
    driver.find_element_by_class_name("yidun_tips").click()
    driver.find_element_by_class_name("yidun_refresh").click()


time.sleep(5)

#driver.quit()