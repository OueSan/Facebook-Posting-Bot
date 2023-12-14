from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def configure_chrome_options():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,
    })

    return chrome_options

def start_driver():
    chrome_options = configure_chrome_options()
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def navigate_to_facebook(driver):
    driver.get('https://www.facebook.com/')
    sleep(5)

def login_to_facebook(driver, email, password):
    email_field = driver.find_element(By.ID, 'email')
    email_field.send_keys(email)
    sleep(5)

    password_field = driver.find_element(By.ID, 'pass')
    password_field.send_keys(password)
    sleep(5)

    login_button = driver.find_element(By.XPATH, "//button[@name='login']")
    login_button.click()
    sleep(5)

def post_status(driver, status):
    status_field = driver.find_element(By.XPATH, "//div[@class='m9osqain a5q79mjw gy2v8mqq jm1wdb64 k4urcfbm qv66sw1b']")
    status_field.click()
    sleep(5)

    inside_status_field = driver.find_element(By.XPATH, "//p[@class='i1ao9s8h hcukyx3x oygrvhab cxmmr5t8 kvgmc6g5']")
    inside_status_field.click()
    sleep(1)

    inside_status_field.send_keys(status)
    sleep(3)

    publish_button = driver.find_element(By.XPATH, "//div[@class='l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv d1544ag0 tw6a2znq s1i5eluu tv7at329']")
    publish_button.click()
    sleep(2)

def main():
    driver = start_driver()
    
    navigate_to_facebook(driver)
    
    # Put your Facebook email and password here
    login_to_facebook(driver, 'put email here', 'put password here')

    # Put your status message here
    post_status(driver, 'Hello! have a good day!')

    input('Press Enter to close the browser.')
    driver.close()

if __name__ == "__main__":
    main()
