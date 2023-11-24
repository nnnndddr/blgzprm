import time
import pyautogui
from locust import HttpUser, task
from selenium.webdriver.common.by import By
from selenium import webdriver


class RequestTests(HttpUser):
    @task
    def click_button(self):
        for i in range(1, 1500):
            default_layer = 37050 + i
            self.client.get(f"https://portaltest.gismap.by/next/proxy/proxy.ashx?https://portaltest.gismap.by/arcservertest/rest/services/C01_Belarus_WGS84/Belarus_BaseMap_WGS84/MapServer/tile/16/21077/{default_layer}")

        for i in range(166, 171):
            for j in range(288, 302):
                self.client.get(f"https://portaltest.gismap.by/next/proxy/proxy.ashx?https://portaltest.gismap.by/arcservertest/rest/services/C01_Belarus_WGS84/Belarus_BaseMap_WGS84/MapServer/tile/9/{i}/{j}")

        for i in range(1, 550):
            land_info_layers = 37550 + i
            self.client.get(f"https://portaltest.gismap.by/next/proxy/proxy.ashx?https://portaltest.gismap.by/arcservertest/rest/services/A01_ZIS_WGS84/Land_Minsk_public/MapServer/tile/16/21074/{land_info_layers}")
            self.client.get(f"https://portaltest.gismap.by/next/proxy/proxy.ashx?https://portaltest.gismap.by/arcservertest/rest/services/A05_EGRNI_WGS84/Uchastki_Minsk_public/MapServer/tile/16/21076/{land_info_layers}")
