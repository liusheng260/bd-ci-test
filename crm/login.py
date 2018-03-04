import unittest,time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/Users/liusheng/Desktop/application/geckodriver')
        self.driver.implicitly_wait(40)
        self.driver.set_page_load_timeout(20)
        self.driver.set_script_timeout(20)
        self.driver.maximize_window()
        self.driver.get("http://o2o.baison.com.cn/icrm_test/manage/web")
        time.sleep(5)

    def test_login(self):
        #输入用户名
        self.driver.find_element_by_xpath("//p/input").send_keys("admin")
        #输入密码
        self.driver.find_element_by_xpath("//p[2]/input").send_keys("admin8888")
        #点击登录按钮
        self.driver.find_element_by_xpath("//form/p[4]/button").click()
        time.sleep(2)

    def test_add_customer(self):
        #登录
        self.driver.find_element_by_xpath("//p/input").send_keys("admin")
        self.driver.find_element_by_xpath("//p[2]/input").send_keys("admin8888")
        self.driver.find_element_by_xpath("//form/p[4]/button").click()
        time.sleep(3)
        #锁定菜单栏
        self.driver.find_element_by_xpath("//div[1]/div[1]/div/div[2]/span").click()
        time.sleep(3)
        #点击会员
        self.driver.find_element_by_xpath("//div[1]/div[1]/div/div[3]/ul/li[2]").click()
        time.sleep(3)
        #点击子菜单顾客资料
        self.driver.find_element_by_xpath("//dl/div[1]/div[1]/dd[1]/span[1]").click()
        time.sleep(3)
        #新增顾客资料（鼠标移动上去才可以显示元素）
        ele1 = self.driver.find_element_by_xpath("//*[@id='btn_ico_0']")
        ActionChains(self.driver).move_to_element(ele1).perform()
        self.driver.find_element_by_xpath("//*[@id='btn_ico_0']/span[1]").click()
        #输入'顾客名称'
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='main_box']/div/div[2]/ul/li[2]/input").send_keys('ss04')
        #输入'手机号'
        self.driver.find_element_by_xpath("//*[@id='main_box']/div/div[2]/ul/li[4]/input").send_keys("13100001114")

        #选择渠道
        self.driver.find_element_by_xpath("//*[@id='main_box']/div/div[2]/ul/li[6]/select-single/span/input").click()
        time.sleep(3)
        ele22 = self.driver.find_element_by_xpath("//*[@role='alertdialog']/div[2]/div[1]/div/input")
        ActionChains(self.driver).move_to_element(ele22).perform()
        self.driver.find_element_by_xpath("//*[@role='alertdialog']/div[2]/div[1]/div/input").send_keys('C分公司01')
        self.driver.find_element_by_xpath("//*[@role='alertdialog']/div[2]/div[1]/div/span/button/span").click()
        ele2 = self.driver.find_element_by_xpath("//*[@role='alertdialog']/div[2]/div[1]/table/tbody/tr/td[2]")

        ActionChains(self.driver).move_to_element(ele2).perform()
        self.driver.find_element_by_xpath("//*[@role='alertdialog']/div[2]/div[1]/table/tbody/tr/td[2]").click()
        #选择店铺
        self.driver.find_element_by_xpath("//div[2]/ul/li[7]/select-single/span/input").click()
        time.sleep(2)
        ele3 = self.driver.find_element_by_xpath("//*[ @ role = 'alertdialog']/div[2]/div[1]/table/tbody/tr/td[2]")
        ActionChains(self.driver).move_to_element(ele3).perform()
        self.driver.find_element_by_xpath("//*[ @ role = 'alertdialog']/div[2]/div[1]/table/tbody/tr/td[2]").click()

        #点击生日
        self.driver.find_element_by_xpath("//*[@id='main_box']/div/div[2]/ul/li[12]/select-date/div/input").click()
        #切入iframe页面
        self.driver.switch_to.frame(0)
        # 选择生日为今天
        ele4 = self.driver.find_element_by_xpath("//*[@id='dpTodayInput']")
        ActionChains(self.driver).move_to_element(ele4).perform()
        self.driver.find_element_by_xpath("//*[@id='dpTodayInput']").click()
        #从iframe切回主文档
        self.driver.switch_to.default_content()
        #保存
        self.driver.find_element_by_xpath("//*[@id='main_box']/div/div[2]/div/button[1]").click()
        time.sleep(5)

        self.assertEqual()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    #unittest.main()

    # 构造测试集
    suite = unittest.TestSuite()
    #suite.addTest(LoginTest("test_login"))
    suite.addTest(LoginTest("test_add_customer"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
