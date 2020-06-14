# -*- coding: utf-8 -*-
import pytest
import time
from selenium import webdriver

'''
This program will Launch the browser and navigate to Github repo to extract Stars, Releases and Last Release

'''


# Test Setup and TearDown
@pytest.fixture(scope='module')
def setup():
    global driver
    driver = webdriver.Chrome(executable_path="drivers/chromedriver.exe")  # Update for browser change
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


# Variables

repo_name = 'appium-desktop'
release_link = "https://github.com/appium/appium-desktop/releases/tag/v1.18.0-beta.0"


# Function to  Navigate to GitHub Repo and display the repo name
def test_github_test(setup):
    driver.get("https://github.com/")
    page_title = driver.title
    print("the title {}".format(page_title))
    assert page_title == "The world’s leading software development platform · GitHub"

    # search the repo
    driver.find_element_by_name('q').send_keys(repo_name)
    driver.find_element_by_id('jump-to-suggestion-search-global').click()

    repo_search = "//a[@class='v-align-middle'][contains(@href,'/{}')]".format(repo_name)

    driver.find_element_by_xpath(repo_search).click()

    # Print <organization/repository name>

    org_text = driver.find_element_by_xpath("//a[@data-hovercard-type='organization']").text
    print("\n\n" + org_text + "/" + repo_name)

    assert org_text + "/" + repo_name == "appium/appium-desktop"

    # Stars: <number of stars>
    star_search = '//a[@class=\'social-count js-social-count\']'

    star_count = driver.find_element_by_xpath(star_search).text
    print('\nStars: {}'.format(star_count))

    # Print Releases: < number of releases >

    release_search = "//div/div/div/ul/li[4]/a/span[@class='num text-emphasized']"

    release_number = driver.find_element_by_xpath(release_search).text
    print("Releases: {}".format(release_number))

    # Print Last release: < link to the last  release >

    driver.find_element_by_xpath("//div/div/div/ul/li[4]").click()
    time.sleep(2)

    last_release_link= driver.find_element_by_xpath("//div[1]/div/div[2]/div[1]/div/div/a").get_attribute("href")

    print("Last release: {}".format(last_release_link))

    assert last_release_link == release_link
