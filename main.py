import time
import json
import argparse


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from restricted_input import r_input

from setting import *
from config import *
from functions import *

def getText(driver, xpath)->str:
    return fnGetElementXpath(driver, False, xpath).__getattribute__('text')

def setText(driver, xpath, val)->bool:
    #Set up text
    try:
        ele = fnGetElementXpath(driver, False, xpath)

        actions = ActionChains(driver)
        actions.click(on_element = ele)
                
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)            
        actions.send_keys(f'{val}')
        actions.perform()
        return True
    except:
        return False

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Make an account")
    parser.add_argument('-in', '--index_number', help = "Pass --index_number to the name of octo profile", type = int, default = 1, required = True)
    args = parser.parse_args()

    with open('elements.json') as fp:
        elements = json.loads(fp.read())
    
    profile_id = ''

    # Delete Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}{args.index_number:04}')
        deleteProfile(profile_id)
        print(f'Success to delete {OCTO_ID}{args.index_number:04} profile!')
    except:
        print(f'There does not exist with profile name {OCTO_ID}{args.index_number:04}')
    
    # Create Profile
    try:
        profile_id = fnGetUUID(f'{OCTO_ID}{args.index_number:04}')
    except:
        print(f'Create Octo Profile with {OCTO_ID}{args.index_number:04}.')
        profile_id = createProfile(f'{OCTO_ID}{args.index_number:04}')

    port = get_debug_port(profile_id)
    driver = get_webdriver(port)
    driver.get(VISA_URL)
    # driver.get("https://www.upwork.com/nx/create-profile/welcome")
    
    # login button
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, elements['login']))
            )
        except:
            print("Web Driver Error....")
        setText(driver, elements['username'], "liujing12345")
        setText(driver, elements['password'], "ZTdQebzM+L.w54e")
        btnLogin = fnGetElementXpath(driver, False, elements['login'])
        
        try:
            btnLogin.click()
            break
        except:
            print("Cant'click login button")

    
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, elements['germany']))
            )
        except:
            print("can't click working button")

        btnGermany = fnGetElementXpath(driver, False, elements['germany'])
        try:
            btnGermany.click()
            break
        except:
            print("can't click germany button")
        
        
    while True:
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, elements['applynow']))
            )
        except:
            print("can't click working button")

        btnApplyNow = fnGetElementXpath(driver, False, elements['applynow'])
        try:
            btnApplyNow.click()
            break
        except:
            print("can't click germany button")

        field_fName = fnGetElementXpath(driver, False, elements['fName'])
        setText(driver, elements['fName'], "wangming123")
        
    # Accept all cookies
    # while True:
    #     try:
    #         WebDriverWait(driver, 30).until(
    #             EC.element_to_be_clickable((By.XPATH, elements['acceptAll']))
    #         )
    #     except:
    #         print("Web Driver Error.....")
        
    #     btnAcceptAll = fnGetElementXpath(driver, False, elements['acceptAll'])
        
    #     try:
    #         btnAcceptAll.click()
    #         break
    #     except:
    #         print("Can't click the Accept All button!")
    # time.sleep(1)
    # # FreelancerButtonBox Click
    # btn_freelancer = fnGetElementXpath(driver, False, elements['freelancerButtonBox'])

    # try:
    #     btn_freelancer.click()
    # except:
    #     print("Can't click the FreelancerButtonBox!")
        
    # # wait until the ApplyButton is enabled.
    # try:
    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, elements['applyButton']))
    #     )
    # except:
    #     print("Web Driver Error.....")
        
    # btn_apply = fnGetElementXpath(driver, False, elements['applyButton'])
    # try:
    #     btn_apply.click()
    # except:
    #     print("Can't click the FreelancerButtonBox!")
    # time.sleep(1)

    # # Submit the form
    # setText(driver, elements['firstName'], FIRST_NAME)
    # setText(driver, elements['lastName'], LAST_NAME)
    # setText(driver, elements['email'], f'{EMAIL}+{int(args.index_number)}@proton.me')
    # setText(driver, elements['password'], PASSWORD)

    # checkboxSendEmail = fnGetElementXpath(driver, False, elements['sendEmail'])
    # try:
    #     checkboxSendEmail.click()
    # except:
    #     print("Can't click the sendEmail checkbox!")
    
    # checkboxAgreementAndPrivacyPolicy = fnGetElementXpath(driver, False, elements['agreementAndPrivacyPolicy'])
    # try:
    #     checkboxAgreementAndPrivacyPolicy.click()
    # except:
    #     print("Can't click the agreement and privacy policy checkbox!")
    
    # btnCreateAccount = fnGetElementXpath(driver, False, elements['createAccount'])
    # try:
    #     btnCreateAccount.click()
    # except:
    #     print("Can't click the create Account!")

    # print('Enter the redirection url')
    # nURL = r_input("Enter the URL: ")
    # driver.get(nURL)
    
    # oldURL = nURL
    
    # while True:
    #     newURL = driver.current_url
    #     if oldURL == newURL:
    #         continue
    #     print(newURL)
    #     match newURL.split('/')[-1]:            
    #         case 'welcome':
    #             while True:
    #                 if welcome(driver):
    #                     break
    #         case 'experience':
    #             while True:
    #                 if experience(driver):
    #                     break
    #         case 'goal':
    #             while True:
    #                 if goal(driver):
    #                     break
    #         case 'work-preference':
    #             while True:
    #                 if work_preference(driver):
    #                     break
    #         case 'resume-import':
    #             while True:
    #                 if resume_import(driver):
    #                     break
    #         case 'title':
    #             while True:
    #                 if title(driver):
    #                     break
    #         case 'employment':
    #             while True:
    #                 if employment(driver):
    #                     break
    #         case 'education':
    #             while True:
    #                 if education(driver):
    #                     break
    #         case 'certifications':
    #             while True:
    #                 if certifications(driver):
    #                     break
    #         case 'languages':
    #             while True:
    #                 if languages(driver):
    #                     break
    #         case 'skills':
    #             while True:
    #                 if skills(driver):
    #                     break
    #         case 'overview':
    #             while True:
    #                 if overview(driver):
    #                     break
    #         case 'categories':
    #             while True:
    #                 if categories(driver):
    #                     break
    #         case 'rate':
    #             while True:
    #                 if rate(driver):
    #                     break
    #         case 'location':
    #             while True:
    #                 if location(driver):
    #                     break
    #         case 'submit':
    #             while True:
    #                 if submit(driver):
    #                     break
    #         case 'finish':
    #             while True:
    #                 if finish(driver):
    #                     break
    #         case _:
    #             if newURL.split('/')[-2] == 'best-matches':
    #                 break
    #             time.sleep(1)
    #             continue
    #     oldURL = newURL
    