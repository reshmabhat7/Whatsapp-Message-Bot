from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Open WhatsApp Web
driver.get("https://web.whatsapp.com")

# Step 3: Wait 15 seconds for QR code scan
print("Scan the QR code now...")
time.sleep(15)

# Step 4: Find and click on chat
search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
search_box.click()
search_box.send_keys("Babu")  # Replace with actual contact
search_box.send_keys(Keys.ENTER)
time.sleep(2)

# Step 5: Send 5 messages
message_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")

for i in range(1, 6):
    message = f"Hi, this is message {i}"
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)

print("All messages sent!")

