from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Scr():
  def __init__(self):
    pass


  def videoid_from_userid(self, user_id):
    URL = f'https://www.tiktok.com/@{user_id}'

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # ページの読み込みを待つ
    wait = WebDriverWait(driver, 50)

    # 対象要素を取得する
    elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'css-x6y88p-DivItemContainerV2')))
    print(len(elements))

    video_ids = []
    for i in range(len(elements)):
        video_xpath = f'/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[{i+1}]/div[1]/div/div/a'
        video_element = wait.until(EC.presence_of_element_located((By.XPATH, video_xpath)))

        # 動画のIDを取得する
        video_url = video_element.get_attribute('href')
        video_id = video_url.split('/')[-1]
        video_ids.append(video_id)

    driver.close()

    return video_ids



# 入力欄
user_id = 'music_mana5'


# スクレイピング
scr = Scr()
video_ids = scr.videoid_from_userid(user_id=user_id)