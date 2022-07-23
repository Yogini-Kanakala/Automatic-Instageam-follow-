import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

class InstagramFollowerBot():
    def __init__(self):
        # Setup selelnium and connection to website
        ser = Service("ENTER FILE PATH TO CHROMEDRIVER")
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)

    def login(self):
        # Log in to website
        self.driver.get('https://instagram.com/')
        time.sleep(2)
        # Find username and password field and fill in puch login button
        user_entry = self.driver.find_element(By.NAME, 'username')
        pass_entry = self.driver.find_element(By.NAME, 'password')
        user_entry.send_keys('ENTER YOUR USER NAME')
        pass_entry.send_keys('ENTER YOUR PASSWORD')
        login_button = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        # Finding button names and matching on the text
        for button in login_button:
            if button.text == 'Log In':
                print("Logging in Python style :D")
                button.click()
        time.sleep(3)
        # Telling IG i do not want to sync my profile information
        not_now_button = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in not_now_button:
            try:
                if button.text == 'Not Now':
                    button.click()
                    print('No save info')
                    break
            except StaleElementReferenceException as err:
                print(f'Some error?')
        time.sleep(3)
        # Tellling IG NO i do not want notifications 
        notifications_no = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for button in notifications_no:
            if button.text == 'Not Now':
                button.click()
                print('No notifications')
                break

    def follow_people(self):
        time.sleep(3)
        # Find search bar and ENTER in your keyword and go to first account in list
        search_bar = self.driver.find_element(By.CLASS_NAME, 'XTCLo')
        search_bar.send_keys('python') # Enter your keyword
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(3)
        # Find button on IG page to bring up their follower list
        follow_button = self.driver.find_elements(By.CLASS_NAME, '-nal3')
        for button in follow_button:
            if button.text.split(' ')[1] == 'followers':
                button.click()
        time.sleep(3)
        # Find pop up and make scrolling element
        pop_up = self.driver.find_element(By.CLASS_NAME, 'RnEpo')
        scroller = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        # The Loop below will go until it scrolls the div 5 times, it will scroll through already followed accounts, 
        # if a element falls out the exception prints and the follower list is repopulated with the scrolling div
        # Scroller will keep scrolling each time exception is thrown for X in RANGE for i in range(int(X))
        for i in range(int(10)):
            try:
                followers = pop_up.find_elements(By.CLASS_NAME, 'sqdOP')
                print('line 64')
                for follower in followers:
                    time.sleep(3)
                    if follower.text == 'Following' or follower.text == 'Requested':
                        print('Already following')
                    else:
                        follower.click()
                        print('New Follower')
            except StaleElementReferenceException:
                print('End of scrolling try again?')
            # Scroll div element after every click or pass in the list
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroller)
