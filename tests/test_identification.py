from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import pyautogui
from dotenv import load_dotenv

load_dotenv()


def test_identification():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get("https://portaltest.gismap.by/next")
        time.sleep(5)

        open_data_btn = browser.find_element(By.ID, "dijit_form_Button_1_label")
        open_data_btn.click()
        time.sleep(5)

        zoom_inc = browser.find_element(By.CLASS_NAME, "esriSimpleSliderIncrementButton")
        for i in range(1, 10):
            zoom_inc.click()
            time.sleep(1)

        time.sleep(2)
        layers_btn = browser.find_element(By.ID, "layerControl_parent_titleBarNode")
        layers_btn.click()
        time.sleep(1)

        land_info_btn = browser.find_element(By.XPATH, "//div[3]/table/tbody/tr/td[2]/i")
        land_info_btn.click()
        time.sleep(1)

        current_x, current_y = pyautogui.position()

        pyautogui.rightClick(current_x, current_y)
        time.sleep(1)
        identification_btn = browser.find_element(By.ID, "dijit_MenuItem_2")
        identification_btn.click()
        time.sleep(2)
        pop_up = browser.find_element(By.CLASS_NAME, "contentPane")
        pop_up.click()
        if pop_up.value_of_css_property("display") == "none":
            raise AssertionError("Error")

    finally:
        time.sleep(3)
        browser.quit()
