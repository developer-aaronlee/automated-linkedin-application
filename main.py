from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

email = "automations.python@gmail.com"
password = "lsr211425"
phone = "9876543210"

chrome_driver = Service("/Applications/chromedriver")
driver = webdriver.Chrome(service=chrome_driver)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3203703179&"
           "f_AL=true&f_WT=2&keywords=Python%20developer&refresh=true")


time.sleep(1)

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(email)

password_input = driver.find_element(By.ID, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(1)

close_messaging = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header")
close_messaging.click()

# time.sleep(1)
#
# listing_title = driver.find_element(By.CSS_SELECTOR, ".scaffold-layout__list-container li")
# listing_title.click()
#
# time.sleep(1)
#
# save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
# save_button.click()
# save_button.send_keys(Keys.PAGE_DOWN)
#
# time.sleep(1)
#
# follow_button = driver.find_element(By.CLASS_NAME, "follow")
# follow_button.click()


all_listings = driver.find_elements(By.CLASS_NAME, "ember-view.jobs-search-results__list-item.occludable-update.p0")
for x in all_listings:
    time.sleep(1)
    # driver.execute_script("arguments[0].scrollIntoView();", x)
    action = ActionChains(driver)
    action.move_to_element(x).perform()
    x.click()

    time.sleep(1)
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()

    time.sleep(1)
    close_notification = driver.find_element(By.CLASS_NAME, "artdeco-toast-item__dismiss")
    close_notification.click()

    time.sleep(2)
    save_button.send_keys(Keys.END)

    try:
        time.sleep(1)
        follow_button = driver.find_element(By.CLASS_NAME, "follow")
        follow_button.click()

        time.sleep(1)
        close_notification = driver.find_element(By.CLASS_NAME, "artdeco-toast-item__dismiss")
        close_notification.click()

    except NoSuchElementException:
        continue


# driver.quit()


