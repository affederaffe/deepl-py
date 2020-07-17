import os
import os.path
import sys
import time
import json

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

__version__ = "0.0.1"

def translate(targetLang, stringArray, srcTextArray=[""], targetTextArray=[""]):
    ### import paths or let the user input them + browser detection ###
    if not os.path.isfile("ini.json"):
        ini = {}
        ini["Browser"] = {"options.binary_location": input("Location of your browser:")}
        ini["Driver"] = {"Path": input("Location of the driver:")}
        with open("ini.json", "w") as f:
            json.dump(ini, f)
        f.close()
    try:
        jsonFile = open("ini.json")
        ini = json.load(jsonFile)
        PATH = ini["Driver"]["Path"]
        if PATH[-15:] == "geckodriver.exe":
            browser = "firefox"
            from selenium.webdriver.firefox.options import Options
            options = Options()
        elif PATH[-16:] == "chromedriver.exe":
            browser = "chromium"
            from selenium.webdriver.chrome.options import Options
            options = Options()
        options.binary_location = ini["Browser"]["options.binary_location"]
        jsonFile.close()
        options.add_argument("--disable-extensions")
    except:
        jsonFile.close()
        os.remove("ini.json")
        sys.exit("Error: (propably) Corrupted ini file, please try again!")
    if browser == "firefox":
        driver = webdriver.Firefox(options = options, executable_path = PATH, service_log_path = "nul")
    elif browser == "chromium":
        driver = webdriver.Chrome(options = options, executable_path = PATH)
    ### glossary ###
    translatedArray = []
    driver.get("https://deepl.com/translator")
    languageMenuButtonElement = driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[4]/div[1]/div[1]/div[1]/button')
    languageMenuButtonElement.click()
    time.sleep(0.25)
    languageButton = driver.find_elements_by_css_selector('button[dl-lang = "{0}"]'.format(targetLang))
    languageButton[1].click()
    if srcTextArray:
        glossaryElement = driver.find_element_by_xpath('//*[@id="glossaryButton"]/button')
        glossaryElement.click()
        try:
            element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="glossaryButton"]/button')))
        finally:
            srcTextElement = driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/input[1]')
            targetTextElement = driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/input[2]')
            glossaryAcceptElement = driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/button[2]')
            glossaryCloseElement = driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[2]/div[3]')
            glossaryArrayPos = 0
            for i in range(len(srcTextArray)):
                srcTextElement.send_keys(srcTextArray[glossaryArrayPos])
                targetTextElement.send_keys(targetTextArray[glossaryArrayPos])
                glossaryAcceptElement.click()
                glossaryArrayPos += 1
            glossaryCloseElement.click()
    ### actual translator ###
    stringArrayPos = 0
    for i in range(len(stringArray)):
        textInputElement = driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[3]/div[2]/div/textarea')
        # clear textfield #
        try:
            clearElement = driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[3]/div[2]/button')
            clearElement.click()
        except:
            pass
        textInputElement.send_keys(stringArray[stringArrayPos])
        copyElement = driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[4]/div[3]/div[4]/div[1]/button')
        clipboardOld = pyperclip.paste()
        # wait till deepl finished translating #
        while driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[6]').get_attribute("class") == "lmt__mobile_share_container lmt__mobile_share_container--inactive":
            time.sleep(0.1)
        time.sleep(0.5)
        copyElement.click()
        translatedArray.append(pyperclip.paste())
        pyperclip.copy(clipboardOld)
        stringArrayPos += 1
    driver.quit()
    return(translatedArray)
