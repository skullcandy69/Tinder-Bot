from selenium import webdriver
from time import sleep



class TinderBot():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:\\Users\\skullcandy\\Desktop\\tinder_bot\\chromedriver.exe')
        
    def login(self):
        self.driver.get('http://tinder.com')    
        sleep(5)
        try:
            self.login_google()
            
        except Exception:
            self.login_fb()
        sleep(10)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        sleep(5)
        self.auto_swipe()    
            
    def login_google(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button').click()
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])
        email_in= self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys('shiv.ahuja1494@gmail.com')
        self.driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
        sleep(2)
        password= self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        password.send_keys('frenchtoast')
        login_bttn=self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        login_bttn.click()
        sleep(10)
        self.driver.switch_to_window(base_window)
        
    def login_fb(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button').click()        
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])        
        email_in= self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('9718529289')   
        password= self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys('frenchtoast')
        login_bttn=self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_bttn.click()
        sleep(5)
        #cont = self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
        self.driver.switch_to_window(base_window)        
       
       
    def like(self):
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button').click()
    def close_pop(self):
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]').click()
        
    def auto_swipe(self):
        while True:
            sleep(5)
            try:
                self.like()
            except Exception:
                self.close_pop()
                
bot= TinderBot()
bot.login()
