# -*- coding: utf-8 -*-
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

'''
This program will Launch the browser, Login to GitHub user account and perform below test cases


'''


# Test Setup and TearDown
@pytest.fixture(scope='module')
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

# Variables

repo_name = 'selenium'
username = None  # Enter GitHub Username
password = None  # Enter GitHub Password
title1 = 'py'  # Update the title to find folder
title2 = 'test'  # Update the Title to find sub folder of title1 folder
title3 = '__init__.py'  # Update the file name for File under Title2


# Function to  Navigate to GitHub Repo and display the repo name
def test_github_test(setup):
    driver.get("https://github.com/")
    page_title = driver.title
    assert page_title == "The world’s leading software development platform · GitHub"
    #assert page_title.encode('utf-8') == "The world’s leading software development platform · GitHub"     # uncomment to run on mac

    # Log in to Git Hub

    driver.find_element_by_xpath("//div/div/a[@href ='/login']").click()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'login')))
    except:
        print("Login page element not found!")


    if username is None  or password is None:
        print("Please provide username and passowrd inside the variables in order to proceed with the test")

    else:
        driver.find_element_by_name('login').send_keys(username)
        driver.find_element_by_name('password').send_keys(password)
        driver.find_element_by_name('commit').click()
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@class='container-lg px-2'][contains(.,'Incorrect username or password.')]")))
            print("\n Please provide correct username and password in order to proceed.")

        except:
            time.sleep(2)
            page_title_logged_in = driver.title
            print("Page Title after login - {}".format(page_title_logged_in))
            assert page_title_logged_in == "GitHub"

            # TC#1 - search a repository
            print("\nTest Case 1 Initiated!")
            driver.find_element_by_name('q').send_keys(repo_name)
            driver.find_element_by_id('jump-to-suggestion-search-global').click()

            repo_search = "//ul/li[1]/div[2]/div[1]/a[@class='v-align-middle'][contains(@href,'/{}')]".format(repo_name)

            # Validation of search result

            try:
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, repo_search)))
                print("\nGitHub repository found!")
            except:
                print("GitHub repository not found!")

            repo_name_org = driver.find_element_by_xpath(repo_search).text

            # Validation of Repo name and Organisation
            assert repo_name_org == "SeleniumHQ/selenium"
            print("\nName and Organisation of repository = {}".format(repo_name_org))
            time.sleep(2)

            driver.find_element_by_xpath(repo_search).click()

            # TC#2 - Star and Un-star a repository
            print("\nTest Case 2 Initiated!")
            time.sleep(2)

            try:
                number_star = driver.find_element_by_xpath("//div/form[2]/a").get_attribute('aria-label')
                driver.find_element_by_xpath("//div/form[2]/button").click()
                time.sleep(3)
                print("Repo not Marked as Star, we are going to mark it as Star")
                print("Number of stars when repo not marked as Star = {}".format(number_star.split()[0]))

                # Update Star count
                fetch_star_num = driver.find_element_by_xpath("//div[2]/div/ul/li[3]/div/form[1]/a").text
                #fetch_star_num = fetch_star_num.encode('ascii', 'ignore')     Enable this for mac
                fetch_star_num = fetch_star_num.replace(',', '')
                number_star = int(number_star.split()[0])
                fetch_star_num = int(fetch_star_num)
                print("Number of stars after marking as Star = {}".format(fetch_star_num))

                # Validation for start addition
                assert fetch_star_num == number_star + 1

            except:
                time.sleep(3)
                driver.find_element_by_xpath("//li[3]/div/form[1]/button").click()
                number_star = driver.find_element_by_xpath("//div/form[2]/a").get_attribute('aria-label')
                print("Repo already marked as star, we are goning to un mark the star")
                print("Number of stars when repo already marked as Star = {}".format(number_star.split()[0]))

                # Update Star count
                time.sleep(3)
                fetch_star_num = driver.find_element_by_xpath("//div[2]/div/ul/li[3]/div/form[2]/a").text
                #fetch_star_num = fetch_star_num.encode('ascii', 'ignore')  Enab;e this for mac
                fetch_star_num = fetch_star_num.replace(',', '')
                number_star = int(number_star.split()[0])
                fetch_star_num = int(fetch_star_num)
                print("Number of stars after Unstar a repo = {}".format(fetch_star_num))

                # Validation for start addition
                assert fetch_star_num == number_star - 1

            # TC# 3 Search files in the repository
            print("\nTest Case 3 Initiated!")

            # Search and Navigate to java folder

            path = "//td[2]/span/a[@title='{}']".format(title1)

            try:
                # element = driver.find_element_by_xpath(path)
                # element.location_once_scrolled_into_view
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, path.format(title1))))
                driver.find_element_by_xpath(path).click()  # Update the title to choose another file
            except:
                print ("Folder/file not found")

            # Search and Navigate to next folder server

            path2 = "//td[2]/span/a[@title='{}']".format(title2)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, path2)))
                driver.find_element_by_xpath(path2).click()
            except:
                print ("Folder/file not found")


            # Search for file

            path3 = "//td[2]/span/a[@title='{}']".format(title3)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, path3)))
                driver.find_element_by_xpath(path3).click()
            except:
                print ("Folder/file not found")

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//title[contains(.,'{}')]".format(title3))))
                print("File Found")
            except:
                print ("Folder/file not found")

