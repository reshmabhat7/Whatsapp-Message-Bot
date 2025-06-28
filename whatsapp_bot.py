from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch Chrome and open WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")

# Step 2: Wait for chat list to appear (confirms login is successful)
print("⏳ Waiting for WhatsApp Web to fully load...")
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Chat list']")))

# Step 3: Click the search icon (if needed)
try:
    search_icon = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@title='Search input textbox']")))
    search_icon.click()
except:
    pass  # Sometimes it's already open

# Step 4: Type contact name "Babu" into search
search_input = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")))
search_input.click()
search_input.send_keys("Babu")
search_input.send_keys(Keys.ENTER)
time.sleep(2)

# Step 5: Locate message input and send messages
message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")))
message_box.click()

for i in range(1, 6):
    text = f"Hi, this is message {i}"
    message_box.send_keys(text)
    message_box.send_keys(Keys.ENTER)
    time.sleep(1)

print("✅ Messages sent successfully to Babu!")

