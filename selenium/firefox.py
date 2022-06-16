from selenium import webdriver
from selenium.webdriver.common.proxy import * 
# 代理
myProxy = '202.202.90.20:8080'
# 代理格式
proxy = Proxy({
  'proxyType': ProxyType.MANUAL, 
  'httpProxy': myProxy, 
  'ftpProxy': myProxy, 
  'sslProxy': myProxy, 
  'noProxy': ''
 })

profile = webdriver.FirefoxProfile()
profile = get_firefox_profile_with_proxy_set(profile, proxy)
profile.set_preference("general.useragent.override", user_agent)

# firefox无头模式
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('window-size=1200x600')
executable_path = os.path.abspath('geckodriver.exe')

driver=webdriver.Firefox(proxy=proxy, profile=profile, 
                         options=options, executable_path=executable_path) 
driver.get('https://www.baidu.com') 
driver.quit()
