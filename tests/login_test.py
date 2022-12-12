import selenium
from selenium import webdriver
import pytest
from pages.LoginPage import LoginPage
from pages.homepage import HomePage
from pages.PIMmodule import PIMmodule
#from pages.Adminmodule import Adminmodule

#from selenium.webdriver.common.by import By

class TestLogin():

    @pytest.fixture(scope='class')

    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/user/PycharmProjects/OrangeHRM/driver/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("completed")

    def test_login(self,test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_add_employee(self,test_setup):

        pimmodule = PIMmodule(driver)
        pimmodule.click_PIM_dashboard()
        pimmodule.click_add_employee()
        pimmodule.enter_employee_first_name("Arunachalam")
        pimmodule.enter_employee_middle_name("k")
        pimmodule.enter_employee_last_name("kuppusamy")
        pimmodule.enter_employee_id("0206")
        pimmodule.click_save_button()

    #def test_add_admin(self,test_setup):

        #adminmodule = Adminmodule(driver)
        #adminmodule.click_admin_module()
        #adminmodule.click_add_system_user()
        ##adminmodule.click_user_role_arrow()
        #adminmodule.select_user_role_admin()
        #adminmodule.enter_employee_name("Arun")
        ##adminmodule.click_status()
        #adminmodule.select_status()
        #adminmodule.enter_username("Arunmozhi")
        #adminmodule.enter_password("Arun@12345")
        #adminmodule.enter_confirm_password("Arun@12345")
        #adminmodule.click_save_button()

    def test_logout(self,test_setup):

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        #driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span").click()
        #driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

    #    driver.find_element(By.NAME,"username").send_keys("admin")
    #    driver.find_element(By.NAME,"password").send_keys("admin123")
    #    driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
