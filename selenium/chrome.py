from selenium import webdriver
import os

# 进入浏览器设置
options = webdriver.ChromeOptions()
# 谷歌无头模式
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# 设置页面大小
options.add_argument('window-size=1200x600')
# 设置中文
options.add_argument('lang=zh_CN.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
# 设置代理
options.add_argument('proxy-server=' + proxy)
# 不加载图片
options.add_argument('"profile.managed_default_content_settings.images":2')
# 导入当前py文件目录下的chromedriver
executable_path = os.path.abspath('chromedriver.exe')

browser = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
url = "https://httpbin.org/get?show_env=1"
browser.get(url)
# 设置浏览器窗口大小
browser.set_window_size(1552, 800)
# 删除原来的cookie
browser.delete_all_cookies()
# 添加cookie
browser.add_cookie({'name':'ABC','value':'DEF'})
# 刷新当前页面
browser.refresh()
# 关闭当前窗口
browser.close()
# 关闭浏览器
browser.quit()
