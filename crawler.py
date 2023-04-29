from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pandas as pd

df = pd.read_csv('final1.csv')
i = 19658
keywords = df['all_keywords'][i]
keywords_str = ''.join(r for r in keywords)
input_string = 'write a statement of purpose for me, I am applying for' + keywords_str

path = "//chromedriver.exe"
s = Service(executable_path=path)
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\Acer\\AppData\\Local\\Google\\Chrome\\User Data")
prefs = {"profile.managed_default_content_settings.images": 2}
options.page_load_strategy = 'normal'
page = webdriver.Chrome(service=s, chrome_options=options)


# https://colab.research.google.com/drive/1oCWjPUxpeiQR0izLFik_uMSA2woWASn9?usp=sharing
if __name__ == '__main__':
    page.get("https://app.copy.ai/?")
    sleep(1)
    create_new_project = page.find_element(By.CSS_SELECTOR,
                                           'a.sm\:w-1\/2')
    sleep(2)
    # #chat-editor > div:nth-child(1)
    next_page = create_new_project.get_attribute('href')  # /projects/new?sidebar=tools&tool=chat
    page.get(next_page)

    sleep(2)
    submit = WebDriverWait(page, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".prompt-container")))
    prompt = page.find_element(By.CSS_SELECTOR, "#chat-editor > div:nth-child(1) > p:nth-child(1)")
    prompt.send_keys(input_string)
    prompt.send_keys(Keys.ENTER)
    sleep(2)
    # #editor-content > div:nth-child(1) > p:nth-child(1)
    submit = WebDriverWait(page, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                       "#__next > div > div > div.flex.w-full.flex-wrap > "
                                                                       "div.top-0.w-full.max-w-full.self-start.text"
                                                                       "-blue-900.md\:pt-0.false > "
                                                                       "div.flex.flex-1.flex-col.h-full > div > div > "
                                                                       "div > div > div > "
                                                                       "div.relative.mx-auto.flex.w-full.max-w-3xl"
                                                                       ".flex-col.overflow-hidden > div > "
                                                                       "div:nth-child(3) > "
                                                                       "div.flex.w-full.flex-col.p-1 > div > "
                                                                       "div.flex-1.overflow-x-auto.pl-3 > div")))

    sleep(10)

    output = page.find_elements(By.TAG_NAME, 'p')
    output = output[2:9]
    for p in output:
        print(p.text)


