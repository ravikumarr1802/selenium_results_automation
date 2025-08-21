# 📘 GRIET Results Scraper with selenium

This project helps **GRIET students** automatically fetch their results from the official [GRIET Results Portal](https://gradesresults.griet.in).  
It uses **Selenium** with Python to automate the roll number entry and capture results.  

---

## 🚀 Features  
- Reads roll numbers from a **CSV file** (no header required).  
- Automates login into the GRIET results page.  
- Works for **all branches & sections** (you just need the correct URL for your exam session).  
- Easily customizable for your roll numbers.  

---

## 📂 Project Structure  
├── roll_numbers.csv # List of roll numbers (one per line, no header) <br>
├── selenium_automation.py # Python script with Selenium automation <br>
└── README.md # Instruction <br>


---

## 🛠️ Requirements  
1. Install **Python 3.8+**  
2. Install dependencies:  
   ```bash
   pip install selenium webdriver-manager
3. Install Google Chrome (latest version).

--- 

📋 Setup Instructions
1. Prepare Roll Numbers

Create a file named roll_numbers.csv in the project folder. (Pro Tip 😉: Use Chat GPT to make this roll numbers csv file.) <br>
Put one roll number per line, for example:<br>
22241A6666 <br>
22241A6667 <br>
22241A6668 <br>
22241A6669 <br>
...

2. Update Results Page URL

In selenium_automation.py, change the url variable based on your branch/section: <br>
url = "https://gradesresults.griet.in/results.php?result=GR22:2024-25:A:320:REGULAR:AUGUST"

3. Run the Script

Run the script with: <br>
<br>
python selenium_automation.py

📌 Note: <br>
<br>
This tool is only for GRIET students. <br>
Do not misuse it for other colleges or scraping unrelated data. <br>
If GRIET updates their portal, you may need to adjust the By.NAME selector or URL. <br>

