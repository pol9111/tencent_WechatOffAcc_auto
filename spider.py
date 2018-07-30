from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from config import *

class Action():
    def __init__(self):
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": "SM_G9500",
            "appPackage": "com.tencent.mm",
            "appActivity": ".ui.LauncherUI",
            "noReset": True
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def entry(self):
        # 点击进入搜索
        search = self.wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@content-desc="Search"]')))
        search.click()
        # 点击输入搜索内容
        keyword = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/hx')))
        keyword.set_text(KEYWORD)
        sleep(2)
        # 点击搜索
        TouchAction(self.driver).tap(x=1299, y=2605).perform()
        sleep(2)
        # 点击公众号
        TouchAction(self.driver).tap(x=672, y=634).perform()
        # 点击右上角人像
        view_profile = self.wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.ImageButton[@content-desc="Chat Info"]')))
        view_profile.click()
        # 点击查看历史
        view_history = self.wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.LinearLayout[8]//*[@resource-id="android:id/title"]')))
        view_history.click()
        sleep(3)
        # TouchAction(self.driver).press(x=806, y=2500).move_to(x=806, y=2400).release().perform()
        self.driver.swipe(FLICK_START_X, FLICK_START_Y + 960, FLICK_START_X, FLICK_START_Y)
        sleep(1)

        while True:
            t = -450
            for i in range(6):
                try:
                    t += 440
                    sleep(1)
                    # 循环点击每篇文章图片 图片高度500px
                    # x, y根据自己手机屏幕来调整
                    TouchAction(self.driver).tap(x=1019, y=440+t).perform()
                    # 尝试再点击一次, 如果第一次点击到两个图片的中间, 并不会进入文章
                    # 图片与图片间隔180px
                    try:
                        TouchAction(self.driver).tap(x=1150, y=440+t+182).perform()
                    except:
                        pass
                    # 点击退出文章
                    sleep(2)
                    back = self.wait.until(EC.presence_of_element_located((By.ID, 'com.tencent.mm:id/i2')))
                    back.click()
                except:
                    pass
            sleep(1)
            # 模拟拖动
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + 1500, FLICK_START_X, FLICK_START_Y)




if __name__ == '__main__':
    action = Action()
    action.entry()










