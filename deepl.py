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

class Translate:
    def __init__(self, targetLang, stringArray, srcTextArray=[""], targetTextArray=[""]):
        self.targetLang = targetLang
        self.stringArray = stringArray
        self.srcTextArray = srcTextArray
        self.targerTextArray = targetTextArray
        #import paths or let the user input them
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
            self.PATH = ini["Driver"]["Path"]
            if self.PATH[-15:] == "geckodriver.exe":
                browser = "firefox"
                from selenium.webdriver.firefox.options import Options
                self.options = Options()
            elif self.PATH[-16:] == "chromedriver.exe":
                browser = "chromium"
                from selenium.webdriver.chrome.options import Options
                self.options = Options()
            self.options.binary_location = ini["Browser"]["options.binary_location"]
            jsonFile.close()
            self.options.add_argument("--disable-extensions")
        except:
            jsonFile.close()
            os.remove("ini.json")
            sys.exit("Error: (propably) Corrupted ini file, please try again!")
        if browser == "firefox":
            self.driver = webdriver.Firefox(options = self.options, executable_path = self.PATH, service_log_path = "nul")
        elif browser == "chromium":
            self.driver = webdriver.Chrome(options = self.options, executable_path = self.PATH)

    def glossary(self):
        glossaryElement = self.driver.find_element_by_xpath('//*[@id="glossaryButton"]/button')
        glossaryElement.click()
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="glossaryButton"]/button')))
        finally:
            srcTextElement = self.driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/input[1]')
            targetTextElement = self.driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/input[2]')
            glossaryAcceptElement = self.driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[4]/form/div[1]/button[2]')
            glossaryCloseElement = self.driver.find_element_by_xpath('//*[@id="glossaryEditor"]/div[2]/div[3]')
            arrayPos = 0
            for i in range(len(self.srcTextArray)):
                srcTextElement.send_keys(self.srcTextArray[arrayPos])
                targetTextElement.send_keys(self.targerTextArray[arrayPos])
                glossaryAcceptElement.click()
                arrayPos += 1
            glossaryCloseElement.click()
        
    def translate(self):
        arrayPos = 0
        translatedArray = []
        self.driver.get("https://deepl.com/translator")
        languageMenuButtonElement = self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[4]/div[1]/div[1]/div[1]/button')
        languageMenuButtonElement.click()
        time.sleep(0.25)
        languageButton = self.driver.find_elements_by_css_selector('button[dl-lang = "{0}"]'.format(self.targetLang))
        languageButton[1].click()
        if self.srcTextArray:
                self.glossary()
        for i in range(len(self.stringArray)):
            textInputElement = self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[3]/div[2]/div/textarea')
            #try clearing textfield
            try:
                clearElement = self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[3]/div[2]/button')
                clearElement.click()
            except:
                pass
            textInputElement.send_keys(self.stringArray[arrayPos])
            copyElement = self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[4]/div[3]/div[4]/div[1]/button')
            clipboardOld = pyperclip.paste()
            #wait till deepl finished translating
            while self.driver.find_element_by_xpath('//*[@id="dl_translator"]/div[1]/div[6]').get_attribute("class") == "lmt__mobile_share_container lmt__mobile_share_container--inactive":
                time.sleep(0.1)
            copyElement.click()
            translatedArray.append(pyperclip.paste())
            pyperclip.copy(clipboardOld)
            arrayPos += 1
        self.driver.quit()
        return(translatedArray)