import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def click_button(driver, path):
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, path).click()

def send_keys(driver, path, value):
    driver.implicitly_wait(3)
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, path)).send_keys(value)
    driver.find_element(By.XPATH, path).send_keys(value)

def _blackwiki_macro_main():
    driver = uc.Chrome()
    driver.get('https://blackkiwi.net/member/login?redirectUrl=/')  # known url using cloudflare's "under attack mode"
    driver.implicitly_wait(30)
    driver.refresh()
    driver.implicitly_wait(3)
    print(driver.title)

    
    #root > div.style__MemberFormContainer-sc-4c0i84-0.ieeDZC > div > div > input:nth-child(6)
    xpath_email = '//*[@id="root"]/div[2]/div/div/input[1]'
    xpath_password = '//*[@id="root"]/div[2]/div/div/input[2]'

    selector_email = '#root > div.style__MemberForm-sc-4c0i84-2.churSe > input:nth-child(6)'
    selector_password = '#root > div.style__MemberForm-sc-4c0i84-2.churSe > input:nth-child(7)'
    selector_login_button ='#root > div.style__MemberForm-sc-4c0i84-2.churSe > button' #'#root > div.style__MemberFormContainer-sc-4c0i84-0.iefOth > div > div > button'

    send_keys(driver, xpath_email, 'data@jejupass.co.kr')
    send_keys(driver, xpath_password, 'epdlxj1234!!')

        # //*[@id="root"]/div[2]/div/div/button
    xpath_login_button = '//*[@id="root"]/div[2]/div/div/button'
    click_button(driver, xpath_login_button)

    xpath_serch_input = '//*[@id="root"]/main/section[1]/div[1]/div[1]/div/div/input'
    send_keys(driver, xpath_serch_input, '제주렌트카')

    xpath_search_button = '//*[@id="root"]/main/section[1]/div[1]/div[1]/div/div/button'
    click_button(driver, xpath_search_button)

    xpath_trend_choice = '//*[@id="root"]/main/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/span[1]/div/div/div[2]/div'
    click_button(driver, xpath_trend_choice)

    xpath_trend_daily = '//*[@id="react-select-2-option-0"]'
    click_button(driver, xpath_trend_daily)

    # xpath_period = '//*[@id="root"]/main/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/span[2]/div/div'
    # click_button(driver, xpath_period)

    # xpath_2020 = '//*[@id="root"]/main/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/span[2]/div/div[2]/div/div/div[5]/div/div[2]/span/span[3]/select/option[3]'
    # click_button(driver, xpath_2020)

    # # https://stackoverflow.com/questions/61520877/can-we-find-xpath-of-a-text-in-selenium-python
    # driver.find_element(By.XPATH, "//span[text()='1']").click()

    # xpath_done_button = '//*[@id="root"]/main/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/span[2]/div/div[2]/div/div/button'
    # click_button(driver, xpath_done_button)

    xpath_csv_download = '//*[@id="root"]/main/div[2]/div/div[3]/div/div[1]/div/div[1]/div[2]/span[3]/a/div'
    click_button(driver, xpath_csv_download)

_blackwiki_macro_main()