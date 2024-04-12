import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Navigate to the YouTube page
driver.get("https://www.dailymotion.com/tseries2")

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

list1=[]
for i in range(1,501):
    video_ele = driver.find_elements(by=By.XPATH, value='//*[@id="root"]/div/main/div/div[2]/div/a[' + str(i) + ']')
    video_urls = [video.get_attribute('href').split("/")[-1] for video in video_ele]
    
    list1.append(video_urls)

print(len(list1))
combine_str = ''.join([video_id[0] for video_id in list1])
print(combine_str)
s = len(combine_str)/7


char_counts = {}
for char in combine_str:
    char_counts[char] = char_counts.get(char, 0) + 1

#most common element
max_count = max(char_counts.values())
most_common_chars = [char for char, count in char_counts.items() if count == max_count]

#for alpha order
most_common_char = min(most_common_chars)

print(f"The most common character is: {most_common_char}")