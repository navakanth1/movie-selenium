from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

@pytest.fixture
def setUp():
    global moviename,year,director,distributor,producor,driver
    moviename = input("enter the moviename:")
    year = input("year:")
    director = input("enter director:")
    distributor = input("enter distributor:")
    producor = input("enter producor:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
def test_movie(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(moviename)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(director)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(producor)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[4]").click()
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(5)