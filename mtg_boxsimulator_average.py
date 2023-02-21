# This is a sample Python script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import numpy as np
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Initialize the Chrome browser
webpage = input("Enter the webpage of the simulator with the desired set (e.g:https://www.mtgboxsim.com/set/one/draft for the set of Phyrexia all will be one) :")
data = np.array([])
driver = webdriver.Chrome()
driver.get(webpage)
time.sleep(5)
for i in range(100):
    # Press the button
    button = driver.find_element(By.XPATH, '//button[@class="Simulation_secondaryCTA__2ULTw"]')
    button.click()

    # Wait for the page to load
    time.sleep(1)

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

data = data.astype(int)
print(average(data))
print(np.std((data)))
mean = np.mean((data))
std_dev = np.std(data)

# Create Poisson distribution
x = np.arange(90, np.max(data) + 1)
pmf = poisson.pmf(x, mu=mean)

# Plot distribution and standard deviation lines
fig, ax = plt.subplots()
ax.plot(x, pmf, label='Poisson distribution')
ax.axvline(mean, color='r', linestyle='--', label='Mean')
ax.axvline(mean + std_dev, color='g', linestyle='--', label='Std dev')
ax.axvline(mean - std_dev, color='g', linestyle='--')
ax.axvline(mean + 2*std_dev, color='b', linestyle='--', label='2 Std dev')
ax.axvline(mean - 2*std_dev, color='b', linestyle='--')
ax.set_xlabel('Value')
ax.set_ylabel('Probability')
ax.legend()
plt.show()