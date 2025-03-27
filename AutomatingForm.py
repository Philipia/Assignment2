import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

#variable declaration
Email = 'phil@gmail.com'
Password = 'phil123'
URL = 'https://automationplayground.com/crm/login.html'
Wait_time = 4
FirstName = "Philip"
LastName = "Iyolibo"
City = "Ikeja"
State = "Lagos"

#initializing browser to run testing and choice of browser here is chrome
driver = webdriver.Chrome()
driver.get(URL)
driver.maximize_window()
time.sleep(Wait_time)

# Enter the login details to gain access to the site
driver.find_element(By.ID, "email-id").send_keys(Email)
driver.find_element(By.ID, "password").send_keys(Password)
Remember = driver.find_element(By.ID, "remember")
Remember.click()

Submit = driver.find_element(By.ID, "submit-id")
Submit.click()
time.sleep(Wait_time)

# add new customer
NewCustomer = driver.find_element(By.ID, "new-customer")
NewCustomer.click()
driver.find_element(By.ID, "EmailAddress").send_keys(Email)
driver.find_element(By.ID, "FirstName").send_keys(FirstName)
driver.find_element(By.ID, "LastName").send_keys(LastName)
driver.find_element(By.ID, "City").send_keys(City)
State_Dropdown = Select(driver.find_element(By.ID, "StateOrRegion"))
State_Dropdown.select_by_visible_text("Florida")
driver.find_element(By.Css.SELECTOR, "new-customer").click()

time.sleep(Wait_time)