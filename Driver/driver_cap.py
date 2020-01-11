from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




class Driver:
   
    def __init__(self, browser):
        self.browser = browser

    def set_browser(self):
        

        if self.browser.lower() == "chrome":
           self.driver = webdriver.Remote("localhost:4444/wd/hub", DesiredCapabilities.CHROME)

#         elif self.browser.lower() == "chrome":
#             options = Options()
#             options.headless = mode
#             # options.add_argument('--disable-gpu')
#             # options.add_argument("--no-sandbox")
#             # options.add_argument("window-size=1400,2100")  # Linux should be activate
#             return webdriver.Chrome(ChromeDriverManager().install(), options=options)


