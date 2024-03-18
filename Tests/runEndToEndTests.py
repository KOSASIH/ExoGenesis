from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def runEndToEndTests():
    # Set up the webdriver
    driver = webdriver.Firefox()

    # Navigate to the home page
    driver.get("http://localhost:5000")

    # Find the input field for the search query
    search_input = driver.find_element_by_name("search")

    # Enter a search query and press Enter
    search_input.send_keys("test")
    search_input.send_keys(Keys.RETURN)

    # Find the first search result
    first_result = driver.find_element_by_css_selector(".search-results li:first-child")

    # Check that the first search result's text matches the expected text

    # Additional end-to-end tests can be added here

    # Close the webdriver
    driver.quit()
