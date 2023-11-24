from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import pyautogui
from dotenv import load_dotenv

load_dotenv()


def analyze_images(images):
    for image in images:
        image_url = image.get_attribute('src')

        if "Land_Minsk_public" in image_url:
            response = requests.get(image_url)
            print("Image URL:", image_url)
            print("Status Code:", response.status_code)
            print("----------------------------------------")

            assert response.status_code == 200, "Error"


def analyze_is_layers_off(images):
    for image in images:
        image_url = image.get_attribute('src')
        response = requests.get(image_url)
        print("Image URL:", image_url)
        print("Status Code:", response.status_code)
        print("----------------------------------------")
        if "Land_Minsk_public" in image_url:
            raise AssertionError("Error")


def test_landInfo():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get("https://portaltest.gismap.by/next")
        time.sleep(5)

        open_data_btn = browser.find_element(By.ID, "dijit_form_Button_1_label")
        open_data_btn.click()
        time.sleep(5)

        zoom_inc = browser.find_element(By.CLASS_NAME, "esriSimpleSliderIncrementButton")
        for i in range(1, 4):
            zoom_inc.click()
            time.sleep(1)

        time.sleep(2)
        screen_width, screen_height = pyautogui.size()
        for i in range(1, 2):
            pyautogui.moveTo(screen_width // 2 - 300, screen_height // 2)
            current_x, current_y = pyautogui.position()
            pyautogui.mouseDown(button='left')
            new_x = current_x + 900
            new_y = current_y + 0
            pyautogui.moveTo(new_x, new_y, duration=0.3)
            pyautogui.mouseUp(button='left')

        for i in range(1, 6):
            zoom_inc.click()
            time.sleep(1)

        layers_btn = browser.find_element(By.ID, "layerControl_parent_titleBarNode")
        layers_btn.click()
        time.sleep(1)

        land_info_btn = browser.find_element(By.XPATH, "//div[3]/table/tbody/tr/td[2]/i")
        land_info_btn.click()
        time.sleep(1)

        images = browser.find_elements(By.TAG_NAME, "img")
        analyze_images(images)

    finally:
        time.sleep(3)
        browser.quit()


def test_landInfo_off():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()
        browser.get("https://portaltest.gismap.by/next")
        time.sleep(5)

        open_data_btn = browser.find_element(By.ID, "dijit_form_Button_1_label")
        open_data_btn.click()
        time.sleep(5)

        zoom_inc = browser.find_element(By.CLASS_NAME, "esriSimpleSliderIncrementButton")
        for i in range(1, 4):
            zoom_inc.click()
            time.sleep(1)
        time.sleep(2)

        screen_width, screen_height = pyautogui.size()
        for i in range(1, 2):
            pyautogui.moveTo(screen_width // 2, screen_height // 2)
            current_x, current_y = pyautogui.position()
            pyautogui.mouseDown(button='left')
            new_x = current_x + 900
            new_y = current_y + 0
            pyautogui.moveTo(new_x, new_y, duration=0.3)
            pyautogui.mouseUp(button='left')

        for i in range(1, 6):
            zoom_inc.click()
            time.sleep(1)

        layers_btn = browser.find_element(By.ID, "layerControl_parent_titleBarNode")
        layers_btn.click()
        time.sleep(1)

        land_info_btn = browser.find_element(By.XPATH, "//div[3]/table/tbody/tr/td[2]/i")
        land_info_btn.click()
        time.sleep(1)

        images = browser.find_elements(By.TAG_NAME, "img")
        time.sleep(1)

        land_info_btn.click()

        pyautogui.moveTo(screen_width // 2 + 200, screen_height // 2)
        current_x, current_y = pyautogui.position()
        pyautogui.mouseDown(button='left')
        new_x = current_x - 900
        new_y = current_y + 0
        pyautogui.moveTo(new_x, new_y, duration=0.3)
        pyautogui.mouseUp(button='left')
        layer_off_img = browser.find_elements(By.TAG_NAME, "img")

        temp_arr = [element for element in layer_off_img if element not in images]

        analyze_is_layers_off(temp_arr)


    finally:
        time.sleep(3)
        browser.quit()
