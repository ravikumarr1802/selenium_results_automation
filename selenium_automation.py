#Works only for GRIET Students
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
csv_file = "Your's class roll numbers csv file without header"
url = "https://gradesresults.griet.in/results.php?result=GR22:2024-25:A:320:REGULAR:AUGUST"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
with open(csv_file, mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        hallticket = row[0].strip() 
        if not hallticket:
            continue
        print(f"Fetching results for: {hallticket}")
        driver.get(url)
        input_box = driver.find_element(By.NAME, "rollno")
        input_box.clear()
        input_box.send_keys(hallticket)
        input_box.send_keys(Keys.RETURN)
driver.quit()
