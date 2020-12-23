from selenium import webdriver 
from time import sleep
from selenium.webdriver.chrome.options import Options #added for a quicker configuration 

class covidBot:

    def __init__(self):
        self.zip = "89052"
        self.dob = "03/24/2000"
        self.dos = "12/21/2020"
        options = Options()
        options.add_argument("no-sandbox")#disable sandboxing, really only needed in docker
        #options.add_argument("headless")#for when you have it all working
        self.driver = webdriver.Chrome()
        self.goZip()
    
    def goZip(self):
        self.driver.get("https://www.cvs.com/minuteclinic/covid-19-testing")
        sleep(2)
        self.driver.find_element_by_name('zip-control').send_keys(self.zip)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[2]/div[1]/div/form/div[2]/button').click()
        sleep(4)
        print("in")



covidBot()

