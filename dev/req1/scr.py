from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class Scr():
  def __init__(self):
    pass


  def videoid_from_userid(self, user_id):
    URL = f'https://www.tiktok.com/@{user_id}'

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    driver.set_window_size(1200, 762)  # ウィンドウサイズを指定 (この値はデフォルト)

    # ページの読み込みを待つ
    time.sleep(10)
    wait = WebDriverWait(driver, 10)

    # スクロール量を設定
    scroll_height = 600  # スクロールする高さのピクセル数
    driver.execute_script("window.scrollTo(0, 0)")

    # プレイリストを作成しているユーザーとそうでないユーザーでXPATHが異なる
    k = self.playlist_is(wait)

    # 対象要素を取得する
    video_ids = []
    for i in range(2000):
      # 少しずつスクロールする
      if i % 8 == 0:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        j = i / 8
        driver.execute_script(f"window.scrollTo(0, {scroll_height * j})")
        time.sleep(3)

      # プレイリストを作成しているユーザーとそうでないユーザーでXPATHが異なる
      video_xpath = f'/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[{k}]/div/div[{i+1}]/div[1]/div/div/a'
      
      # 動画IDの取得
      try:
        video_element = wait.until(EC.presence_of_element_located((By.XPATH, video_xpath)))
        video_url = video_element.get_attribute('href')
        video_id = video_url.split('/')[-1]
        video_ids.append(video_id)
      except TimeoutException as e:
        driver.close()
        return video_ids

    driver.close()

    return video_ids


  def playlist_is(self, wait):
    k = 2
    # プレイリストがないユーザー
    try:
      video_xpath = f'/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div[{k}]/div/div[1]/div[1]/div/div/a'
      wait.until(EC.presence_of_element_located((By.XPATH, video_xpath)))
      return k
    # プレイリストがあるユーザー
    except:
      k = 3
      return k


# # 入力欄
# user_id = 'music_mana5'


# # スクレイピング
# scr = Scr()
# video_ids = scr.videoid_from_userid(user_id=user_id)