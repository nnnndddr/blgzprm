import random
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
        response = requests.get(image_url)

        print("Image URL:", image_url)
        print("Status Code:", response.status_code)
        #print("Headers:", response.headers)
        print("----------------------------------------")

        assert response.status_code == 200, "Error"

def test_navigation():
    try:
        browser = webdriver.Chrome()
        browser.maximize_window()

        browser.get("https://portaltest.gismap.by/next")
        time.sleep(5)

        open_data_btn = browser.find_element(By.ID, "dijit_form_Button_1_label")
        open_data_btn.click()
        time.sleep(5)

        zoom_inc = browser.find_element(By.CLASS_NAME, "esriSimpleSliderIncrementButton")
        for i in range(1, 7):
            zoom_inc.click()
            time.sleep(1)

        time.sleep(2)
        screen_width, screen_height = pyautogui.size()
        for i in range(1, 10):
            random_offset = random.randint(700, 1000)
            pyautogui.moveTo(screen_width // 2 - 300, screen_height // 2)
            current_x, current_y = pyautogui.position()
            pyautogui.mouseDown(button='left')
            new_x = current_x + random_offset
            new_y = current_y + 100
            pyautogui.moveTo(new_x, new_y, duration=0.3)
            pyautogui.mouseUp(button='left')

        images = browser.find_elements(By.TAG_NAME, "img")

        analyze_images(images)

    finally:
        time.sleep(3)
        browser.quit()
