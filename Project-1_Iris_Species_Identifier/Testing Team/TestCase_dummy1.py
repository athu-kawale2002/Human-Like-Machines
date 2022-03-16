from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from multiprocessing.connection import wait
from selenium import webdriver
import HtmlTestRunner
import unittest
import random
import time


entry1 = round(random.uniform(3.5, 8.0), 1)
entry2 = round(random.uniform(2.0, 4.0), 1)
entry3 = round(random.uniform(1.0, 7.0), 1)
entry4 = round(random.uniform(0.1, 2.5), 1)

# Note: Site Taking Invalid Data
# Opening second page directly should give an msg
#


class Iris_Species(unittest.TestCase):
    

    @classmethod
    def setUpClass(cls):

        print("Test Suite has started")

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_case_1_Homepage(self):

        self.driver.get("https://iris-dataset-hlm-project-1.herokuapp.com/")
        self.assertEqual("Human Like Machines", self.driver.title,
                         "Webpage title is not matching")
        print("Fetched Site")
        #time.sleep(2)

    def test_case_2_irisbtn(self):

        wait = WebDriverWait(self.driver, 10)
        irisbtn = wait.until(EC.element_to_be_clickable
            ((By.CLASS_NAME, "btn.btn-outline-dark.ml-3.pt-1")))

        irisbtn.click()
        self.driver.back()
        print("Clicked Iris Btn")
        time.sleep(2)

    def test_case_3_mainUsecase(self):

        self.driver.find_element(By.ID, "inp1").send_keys(entry1)
        self.driver.find_element(By.ID, "inp2").send_keys(entry2)
        self.driver.find_element(By.ID, "inp3").send_keys(entry3)
        self.driver.find_element(By.ID, "inp4").send_keys(entry4)
        self.assertEqual("Human Like Machines", self.driver.title,
                         "Webpage title is not matching")

        time.sleep(2)

        self.driver.find_element(By.CLASS_NAME,"btn.btn-default").click()
         
        '''self.assertEqual("Result", self.driver.title,
                         "Webpage title is not matching")'''
        print("Searched for species.")
        #self.driver.back()


    def test_case_4_wikibtn(self):

        wait=WebDriverWait(self.driver,10)
        wikibtn=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"tag__item")))
        wikibtn.click()
        print("Clicked Wiki Btn")
        time.sleep(2)

    def test_case_5_postcard(self):

        actions=ActionChains(self.driver)
        wait=WebDriverWait(self.driver,10)
        postcard=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"postcard__img")))

        actions.move_to_element(postcard).perform()
        print("Hovered over postcard")
        time.sleep(2)

    def test_case_6_learnbtn(self):

        wait=WebDriverWait(self.driver,10)
        learnbtn=wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"tag__item.play.blue")))
        learnbtn.click()
        print("Clicked learnbtn")
        time.sleep(2)




    @classmethod
    def tearDownClass(cls):

        time.sleep(3)
        print("Test Suite Completed")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:\\HLMPs\\1_Iris_Species\\Report'))
