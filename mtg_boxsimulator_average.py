# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import numpy as np

# Initialize the Chrome browser
data = np.array([])
driver = webdriver.Chrome()
driver.get("https://www.mtgboxsim.com/set/one/draft")
time.sleep(5)
for i in range(100):
    # Press the button
    button = driver.find_element(By.XPATH, '//button[@class="Simulation_secondaryCTA__2ULTw"]')
    button.click()

    # Wait for the page to load
    time.sleep(5)

    # Extract the data
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, "html.parser")
    price = soup.find("div", class_="Simulation_totalValue__VVNdT").text
    pricewc = price[1:4]
    data = np.append(data,pricewc)

# Close the browser

driver.quit()

# Print the extracted data
print(data)


def average(arr):
    arr = arr.astype(float)
    mask = np.logical_not(np.isnan(arr))
    count = np.count_nonzero(mask)
    if count == 0:
        return None
    return np.sum(arr[mask]) / count


print(average(data))