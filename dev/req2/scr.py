from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime


class Scr():
  def __init__(self):
    pass


  def videoid_from_word(self, word):
    URL = f'https://www.tiktok.com/search/video?q={word}'

    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")  # 自動操作の検出を回避
    options.add_argument("--disable-infobars")  # 自動操作の通知を非表示にする
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get(URL)

    # ページの読み込みを待つ
    time.sleep(10)
    wait = WebDriverWait(driver, 50)

    # スクロール量を設定
    scroll_height = 550  # スクロールする高さのピクセル数
    driver.execute_script("window.scrollTo(0, 0)")

    # 対象要素を取得する
    video_ids = []
    diggs = []
    dates = []
    for i in range(100):
      if i % 6 == 0:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        j = i / 6
        driver.execute_script(f"window.scrollTo(0, {scroll_height * j})")
      video_url_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[{i+1}]/div[1]/div/div/a'
      digg_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[{i+1}]/div[2]/div/div[2]/div/strong'
      date_xpath = f'/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[{i+1}]/div[1]/div/div/a/div/div[2]/div'
      video_url_element = wait.until(EC.presence_of_element_located((By.XPATH, video_url_xpath)))
      digg_element = wait.until(EC.presence_of_element_located((By.XPATH, digg_xpath)))
      date_element = wait.until(EC.presence_of_element_located((By.XPATH, date_xpath)))
      # Video ID
      video_url = video_url_element.get_attribute('href')
      video_id = video_url.split('/')[-1]
      video_ids.append(video_id)
      # いいね数
      digg = digg_element.text
      digg = self.count_digg(digg)
      diggs.append(digg)
      # 動画投稿日
      date_str = date_element.text
      date = self.normalize_date(date_str)
      dates.append(date)

    return video_ids, diggs, dates
  

  def count_digg(self, digg):
    if digg[-1] == 'K':
      digg = float(digg[:-1]) * 1000
      return digg
    elif digg[-1] == 'M':
      digg = float(digg[:-1]) * 1000000
      return digg
    elif digg[-1] == 'G':
      digg = float(digg[:-1]) * 1000000000
      return digg
    else:
      digg = float(digg)
      return digg
  

  def normalize_date(self, date_str):
    # 現在の年を取得
    current_year = datetime.now().year

    try:
      # フォーマットを試行
      if len(date_str) == 10:  # 例: '2023-10-19'
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
      elif len(date_str) == 4:  # 例: '2-22'
        date_obj = datetime.strptime(f"{current_year}-{date_str}", '%Y-%m-%d')
      else:
          raise ValueError("Unknown date format")

      # フォーマットを統一
      return date_obj.strftime('%Y-%m-%d')
    except ValueError as e:
      print(f"Error parsing date: {e}")
      return None


# 入力欄
word = 'カラオケ'


# スクレイピング
scr = Scr()
video_ids = scr.videoid_from_word(word=word)