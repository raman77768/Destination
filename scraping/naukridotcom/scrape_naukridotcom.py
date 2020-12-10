from selenium import webdriver
driver = webdriver.PhantomJS(executable_path="C:\users\raman\appdata\local\programs\python\python37\lib\site-packages\phantomjs\phantom.py")

class naukridotcom:

    def start(self,count):
        driver.get("https://www.hirist.com/search/Internship-0-0-0-1.html")
        p_element = driver.find_element_by_id(class_='job-title')
        print(p_element.text)


obj=naukridotcom()
obj.start(100)