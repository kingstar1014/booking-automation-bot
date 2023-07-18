import selenium.webdriver as webdriver

from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests

from config import *

# Create Profile
def createProfile(profileName)->str:
    data = {
        "title": profileName,
        "fingerprint": {
                "os": "win",
                "screen": "1920x1080"
        },
        "proxy": PROXY
    }
    response = requests.post(url = OCTO_AUTOMATION_URL, json = data, headers=OCTO_HEADER).json()
    uuid = response.get('data')['uuid']
    return uuid

def deleteProfile(profileUUID)->str:
    data = {
        "uuids": [f"{profileUUID}"],
        "skip_trash_bin": True
    }
    response = requests.delete(url = OCTO_AUTOMATION_URL, json = data, headers=OCTO_HEADER).json()
    uuid = response.get('data')['deleted_uuids'][0]
    return uuid

# Get Profile uuid of OctoBrowser
def fnGetUUID(profileName):
    response_octo = requests.request("GET", f'{OCTO_AUTOMATION_URL}?search={profileName}', headers=OCTO_HEADER)
    data_uuid = response_octo.json()
    uuid = data_uuid.get('data')[0]['uuid']
    return uuid

# Get Debug Port
# Profile id is uuid from fnGetUUID()
def get_debug_port(profile_id):
    data = requests.post(
        f'{LOCAL_API}/start', json={'uuid': profile_id, 'headless': False, 'debug_port': True}
    ).json()
    print(data)
    return data['debug_port']
def stop_profile(profile_id):
    data = requests.post(
        f'{LOCAL_API}/stop', json={'uuid': profile_id}
    ).json()
    print(data)

# Create webdriver
# port is from get_debug_port()
def get_webdriver(port):
    chrome_options = Options()
    chrome_options.add_experimental_option('debuggerAddress', f'127.0.0.1:{port}')
    # Change chrome driver path accordingly
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def fnGetElementXpath(driver, flag, xpath):
    try:
        ele = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if flag == False:
            return ele
        else:
            ele.click()
    except:
        print(f"fnGetElementXpath() is error because {xpath} can't find")
        return False

def fnGetElementsClass(driver, ClassName):
    try:
        eles = WebDriverWait(driver, 60).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, ClassName)))
        return eles
    except:
        print(f"fnGetElementXpath() is error because {ClassName} can't find")
        return False

