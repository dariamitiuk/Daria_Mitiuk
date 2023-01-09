from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class Login:
    browser = webdriver.Chrome()
    def login(self):
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)
        self.browser.get('https://opensource-demo.orangehrmlive.com/')
        username = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[1]').text.replace('Username : ', '')
        password = self.browser.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div/p[2]').text.replace('Password : ', '')
        
        element = self.browser.find_element(By.NAME, 'username')
        element.click()
        element.send_keys(username)

        element = self.browser.find_element(By.NAME, 'password')
        element.click()
        element.send_keys(password)
        
        click_send = self.browser.find_element(By.CLASS_NAME, 'orangehrm-login-button')
        click_send.click()

class Main(Login):
    def scenario(self):

        element = self.browser.find_element(By.PARTIAL_LINK_TEXT, 'Admin')
        element.click()
        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
        element.click()
        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a')
        element.click()
        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/div/button')
        element.click()

        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input')
        element.click()
        element.send_keys('Intern')

        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea')
        element.click()
        element.send_keys('Testing job adding')

        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea')
        element.click()
        element.send_keys('One note')

        element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]')
        element.click()

        box_list = self.browser.find_elements(By.CLASS_NAME, "oxd-table-card")
        for card in box_list:
            element = card.find_elements(By.CLASS_NAME, 'oxd-padding-cell')
            if element[1].text == 'Intern' and element[2].text == 'Testing job adding':
                sleep(2)
                element = element[3].find_element(By.CLASS_NAME, 'oxd-table-cell-action-space')
                element.click()
                element = self.browser.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')
                element.click()
                break
        sleep(4)
        self.browser.quit()

if __name__ == '__main__':
    test = Main()
    test.login()
    test.scenario()
