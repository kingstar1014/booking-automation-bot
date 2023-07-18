from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from setting import *
import time
import autoit
import ctypes

from config import *

def welcome(driver)->bool:    
    time.sleep(1)
    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type = \"button\"].air3-btn.air3-btn-primary.mr-7"))
        )
        time.sleep(1)
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Get started") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Get Started Button")
        return False
    return True

def experience(driver)->bool:
    time.sleep(4)
    try:
        js_script = 'eles = document.querySelectorAll("input[type = \\"radio\\"]");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].value.indexOf("FREELANCED_BEFORE") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click I am an expert checkbox")
        return False

    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False    
    return True

def goal(driver)->bool:
    
    time.sleep(2)
    try:
        js_script = 'eles = document.querySelectorAll("input[type = \\"radio\\"]");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].value.indexOf("MONEY_ON_SIDE") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Money on Side checkbox")
        return False
    
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
            print("Can't click Next Button")
            return False
    return True

def work_preference(driver)->bool:
    
    time.sleep(2)
    try:
        js_script = 'eles = document.querySelectorAll("div[data-qa=\\"button-box\\"]");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("d like to find opportunities myself") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click I'd like to find opportunities myself checkbox")
        return False
    
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("div[data-qa=\\"button-box\\"]");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("d like to package up my work for clients to buy") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click I'd like to package up my work for clients to buy checkbox")
        return False
    
    time.sleep(1)
    try:
        js_script = 'document.querySelector("input[type = \\"checkbox\\"].air3-checkbox-input.sr-only").click();'
        driver.execute_script(js_script)
    except:
        print("Can't click I'd like to find opportunities myself checkbox")
        return False
    
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    
    return True

def resume_import(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Upload your resume") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Upload your resume button")
        return False

    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.fe-upload-btn.upload-btn a.up-n-link[href]"))
        )
        driver.find_element(By.CSS_SELECTOR, 'span.fe-upload-btn.upload-btn a.up-n-link[href]').click()
    except:
        print('Can\'t Click choose file link!')
        return False
    
    time.sleep(1)
    try:
        handle = "[CLASS:#32770; TITLE:Open]"
        autoit.win_wait(handle, 60)
        autoit.control_set_text(handle, "Edit1", RESUME_PATH)
        autoit.control_click(handle, "Button1")
    except:
        print('Can\'t upload resume!')
    
    time.sleep(1)
    try:
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.air3-modal-footer button"))
        )
    except:
        print('Can\'t load continue button element!')
        return False
    
    time.sleep(1)

    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'div.air3-modal-footer button')
        ele.click()
    except:
        print("Can't click the continue button!")
        return False
    return True

def title(driver)->bool:
    
    try:
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="title-label"][type = "text"]'))
        )
    except:
        print('Can\'t load professional role input!')
        return False
    
    time.sleep(1)
    
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def employment(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
        
    return True

def education(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def certifications(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Skip for now") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Skip for now Button")
        return False
    return True

def languages(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def skills(driver)->bool:
    # if ctypes.windll.user32.MessageBoxW(0, f'If you finished setting up your skills, press OK!', "Alert", 1) != 1:
    #     return False

    for skill in SKILLS_LIST:
        try:
            ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby = "skills-input"][type = "search"]')
            actions = ActionChains(driver)
            actions.click(on_element = ele)
            actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
            actions.send_keys(skill)
            actions.perform()
            try:
                WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li')))
            except:
                print("Can\'t show skills list!")
            time.sleep(1)
            actions.click(on_element = ele)
            actions.send_keys(Keys.DOWN)
            actions.send_keys(Keys.ENTER)
            actions.perform()
        except:
            print(f"Can't input {skill}")
    

    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def overview(driver)->bool:
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'textarea'))
        )
    except:
        print('Can\'t load overview page!')
        return False
    
    time.sleep(1)
    
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def categories(driver)->bool:
    # if ctypes.windll.user32.MessageBoxW(0, f'If you finished setting up your categories, press OK!', "Alert", 1) != 1:
    #     return False
    
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[aria-labelledby *= "dropdown-search-multi-label"]'))
        )
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'div[aria-labelledby *= "dropdown-search-multi-label"]').click()
    except:
        print('Can\'t Click Search for a servie!')
        return False
    
    # Wait until drop down menu appeared
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.air3-multi-select.air3-nested-menu-list'))
        )
    except:
        print('Drop down menu did not appeared!')
        return False
    
    for category in CATEGORIES:
        time.sleep(1.5)
        try:
            js_script = 'eles = document.querySelectorAll("li.air3-multi-select.air3-nested-menu-list");\
                var i = 0;\
                for (i = 0; i < eles.length; i++) {\
                    if (eles[i].textContent.indexOf("' + category + '") != -1)\
                        break;\
                }\
                eles[i].click();'
            driver.execute_script(js_script)
        except:
            print(f"Can't click {category}")
            continue
        
        # Wait Until subitems appeared
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'li.air3-multi-select.air3-nested-menu-list li.air3-multi-select.air3-menu-item'))
            )
        except:
            print('Sub items did not appeared!')
            return False
        
        for subCategory in CATEGORIES[category]:
            time.sleep(1.5)
            try:
                js_script = 'eles = document.querySelectorAll("li.air3-multi-select.air3-nested-menu-list li.air3-multi-select.air3-menu-item");\
                    var i = 0;\
                    for (i = 0; i < eles.length; i++) {\
                        if (eles[i].textContent.indexOf("' + subCategory + '") != -1)\
                            break;\
                    }\
                    eles[i].click();'
                driver.execute_script(js_script)
            except:
                print(f"Can't click {subCategory}!")
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def rate(driver)->bool:
    time.sleep(1)
    try:
        # js_script = 'document.querySelector("input[aria-describedby *= \\"hourly-rate-description\\"][type = \\"text\\"]").value = "' + str(HOURLY_RATE) + '"'
        # driver.execute_script(js_script)
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-describedby *= "hourly-rate-description"][type = "text"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(HOURLY_RATE)
        actions.perform()
    except:
        print("Can't input the rate!")
        return False

    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Next") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print("Can't click Next Button")
        return False
    return True

def location(driver)->bool:
    time.sleep(1)
    try:
        # js_script = 'document.querySelector("input[aria-labelledby = \\"street-label\\"][type = \\"text\\"]").value = "' + STREET_ADDRESS + '"'
        # driver.execute_script(js_script)
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby = "street-label"][type = "text"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(STREET_ADDRESS)
        actions.perform()
    except:
        print("Can't input the Street Address!")
        return False
    
    time.sleep(1)
    try:
        # js_script = 'document.querySelector("input[aria-labelledby = \\"city-label\\"][type = \\"search\\"]").value = "' + CITY + '"'
        # driver.execute_script(js_script)
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby = "city-label"][type = "search"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(CITY)
        actions.perform()
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul[role="listbox"] li')))
        except:
            print("Can\'t show cities list!")
        time.sleep(1.5)
        actions.click(on_element = ele)
        actions.send_keys(Keys.DOWN)
        actions.send_keys(Keys.ENTER)
        actions.perform()
    except:
        print("Can't input the city")
        return False
    
    # time.sleep(1)
    # try:
    #     # js_script = 'document.querySelector("input[aria-labelledby = \\"state-label\\"][type = \\"text\\"]").value = "' + STATE + '"'
    #     # driver.execute_script(js_script)
    #     ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby = "state-label"][type = "text"]')
    #     actions = ActionChains(driver)
    #     actions.click(on_element = ele)
    #     actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
    #     actions.send_keys(STATE)
    #     actions.perform()
    # except:
    #     print("Can't input State")
    #     return False
    
    time.sleep(1)
    try:
        # js_script = 'document.querySelector("input[aria-labelledby = \\"postal-code-label\\"][type = \\"text\\"]").value = "' + POSTAL_CODE + '"'
        # driver.execute_script(js_script)
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby = "postal-code-label"][type = "text"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(POSTAL_CODE)
        actions.perform()
    except:
        print("Can't input the Postal code!")
        return False
    
    time.sleep(1)
    try:
        # js_script = 'document.querySelector("input[aria-labelledby *= \\"dropdown-label-phone-number\\"][type = \\"tel\\"]").value = "' + PHONE_NUMBER + '"'
        # driver.execute_script(js_script)
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby *= "dropdown-label-phone-number"][type = "tel"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(PHONE_NUMBER)
        actions.perform()
    except:
        print("Can't input the phone number!")
        return False
    
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Upload photo") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print('Can\'t click upload photo button')
        return False
    
    time.sleep(1)
    try:
        js_script = 'document.querySelector("input[type = \\"file\\"][name = \\"imageUpload\\"]").click()'
        driver.execute_script(js_script)
    except:
        print('Can\'t click image crop button')
        return False
    
    time.sleep(1)
    try:
        handle = "[CLASS:#32770; TITLE:Open]"
        autoit.win_wait(handle, 60)
        autoit.control_set_text(handle, "Edit1", PHOTO_PATH)
        autoit.control_click(handle, "Button1")
    except:
        print('Can\'t click upload photo!')
        return False
    
    time.sleep(2)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Attach photo") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print('Can\'t click Attach photo button')
        return False
    
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.air3-wizard-footer button[data-ev-label="wizard_next"]'))
        )
    except:
        print('Can\'t load check your profile button element!')
        return False
    
    while True:    
        time.sleep(1)
        try:
            ele = driver.find_element(By.CSS_SELECTOR, 'div.air3-wizard-footer button[data-ev-label="wizard_next"]')
            ele.click()
            break
        except:
            print("Can't click the check your profile button!")
            pass    
    
    return True

def submit(driver)->bool:
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="submit-title-edit-btn"]'))
        )
    except:
        print('Can\'t load submit page!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="submit-title-edit-btn"]')
        ele.click()
    except:
        print('Can\'t click edit title button!')
        return False

    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[aria-labelledby="title-label"]'))
        )
    except:
        print('Can\'t load edit title modal!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'input[aria-labelledby="title-label"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(PROFESSIONAL_ROLE)
        actions.perform()
    except:
        print('Can\'t edit title!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="btn-save"]')
        ele.click()
    except:
        print('Can\'t click save button!')
        return False
    
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="submit-overview-edit-btn"]'))
        )
    except:
        print('Can\'t load submit page!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="submit-overview-edit-btn"]')
        ele.click()
    except:
        print('Can\'t click edit overview button!')
        return False

    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'textarea[aria-labelledby="overview-label"]'))
        )
    except:
        print('Can\'t load edit overview modal!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'textarea[aria-labelledby="overview-label"]')
        actions = ActionChains(driver)
        actions.click(on_element = ele)
        actions.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        actions.send_keys(SUMMARY)
        actions.perform()
    except:
        print('Can\'t edit overview!')
        return False
    
    time.sleep(1)
    try:
        ele = driver.find_element(By.CSS_SELECTOR, 'button[data-qa="btn-save"]')
        ele.click()
    except:
        print('Can\'t click save button!')
        return False
    time.sleep(1)
    try:
        js_script = 'eles = document.querySelectorAll("button");\
            var i = 0;\
            for (i = 0; i < eles.length; i++) {\
                if (eles[i].textContent.indexOf("Submit profile") != -1)\
                    break;\
            }\
            eles[i].click();'
        driver.execute_script(js_script)
    except:
        print('Can\'t click submit profile button')
        return False
    
    return True

def finish(driver)->bool:
    time.sleep(1)
    try:
        js_script = 'document.querySelector("a.up-n-link.air3-btn.air3-btn-primary").click()'
        driver.execute_script(js_script)
    except:
        print('Can\'t click submit profile button')
        return False
    return True
