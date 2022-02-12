import time,json
from loguru import logger
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        option = webdriver.ChromeOptions()
        # option.add_argument('--headless')
        # option.add_argument('--disable-dev-shm-usage')
        # option.add_argument('window-size=1920x3000') #指定浏览器分辨率
        # option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        option.add_argument('--no-sandbox')

        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.add_argument("--disable-blink-features=AutomationControlled")

        # option.add_experimental_option("excludeSwitches", ["enable-automation"])
        # option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument("--disable-blink-features=AutomationControlled")
        # option.add_argument('--verbose')
        # option.add_argument('--single-process')
        # option.add_argument('user-agent="{ua}"'.format(ua=self.UA))
        # option.add_argument('headless')  # 加载浏览器的静默模式
        # option.add_argument('--disable-infobars') #禁用浏览器正在被自动化程序控制的提示
        # option.add_argument("–incognito") #启动无痕/隐私模式

        # 添加保持登录的数据路径：安装目录一般在C:\Users\黄\AppData\Local\Google\Chrome\User Data
        # option.add_argument(r'user-data-dir=C:\Users\admins\AppData\Local\Google\Chrome\User Data')

        # 设置代理
        # json_str = utils.post(URL_PROXY_IP_GET, None)
        # json_obj = json.loads(json_str)
        # print(json_obj)
        # if 'data' in json_obj:
        #     if 'ip' in json_obj['data'] and json_obj['data']['ip'] != '':
        #         print("setProxy:")
        #         ip_port = str(json_obj['data']['ip'])+":"+str(json_obj['data']['port'])
        #         print(ip_port)
        #         option.add_argument("--proxy-server=http://{ip_port}".format(ip_port=ip_port))
        #         self.PROXY = json_obj['data']
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        # ip_port = '113.96.223.240:4004'
        # option.add_argument("--proxy-server=http://{ip_port}".format(ip_port=ip_port))

        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities['loggingPrefs'] = {'performance': 'ALL'}
        desired_capabilities["pageLoadStrategy"] = "none"

        cls.selenium = WebDriver(chrome_options=option, desired_capabilities=desired_capabilities, keep_alive=True)
        cls.selenium.implicitly_wait(10)

    def getCookie(cls):
        # 获取请求头信息
        agent = cls.selenium.execute_script("return navigator.userAgent")
        logger.info(f'selenium \'s user-agent:{agent} ')  # 查看请求头是否更改。

        webdriver_flag = cls.selenium.execute_script("return navigator.webdriver")
        logger.info(f'selenium \'s navigator.webdriver:{webdriver_flag} ')


        # info = cls.selenium.get_log('performance')
        #
        # # 用 for循环读取列表中的每一项元素。每个元素都是 json 格式。
        # for i in info:
        #     dic_info = json.loads(i["message"])  # 把json格式转成字典。
        #     info = dic_info["message"]['params']  # request 信息，在字典的 键 ["message"]['params'] 中。
        #     if 'request' in info:  # 如果找到了 request 信息，就终断循环。
        #         logger.info(f'selenium \'s load url:{info["request"]} ')
        #         break

        cookies_str = ''
        for item in cls.selenium.get_cookies():
            cookies_str += '{0}={1};'.format(item['name'], item['value'])
        logger.info(f'selenium \'s cookies:{cookies_str} ')

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % ('http://127.0.0.1:8000', '/admin/login/?next=/admin/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('huangxiaoming')
        time.sleep(2)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('admin123456')
        time.sleep(5)
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
        self.getCookie()
        time.sleep(300)

