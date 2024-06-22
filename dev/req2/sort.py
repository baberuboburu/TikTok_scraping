from datetime import datetime, timedelta


class Sort():
  def __init__(self, order: int):
    self.order = order


  def route(self, video_ids, diggs, dates, filter=1):
    if self.order == 1:
      return self.rele(video_ids)
    elif self.order == 2:
      return self.digg(video_ids, diggs)
    elif self.order == 3:
      return self.date(video_ids, dates, filter)
    else:
      raise ValueError('order変数には、1, 2, 3のみが入ります。型はint型です。')
  

  # 1000件の動画のうち、関連度上位100件を配列で返す
  def rele(self, video_ids):
    return video_ids[:100]


  # 1000件の動画のうち、いいね数が多い上位100件を配列で返す
  def digg(self, video_ids, diggs):
    # diggsを小さい順にソートし、そのインデックスを取得 -> diggsのソート順にvideo_idsをソート
    sorted_indices = sorted(range(len(diggs)), key=lambda i: diggs[i])
    video_ids_sorted = [video_ids[i] for i in sorted_indices]

    return video_ids_sorted[:100]


  # 1000件の動画のうち、投稿日が、「24時間以内」「今週」「今月」「3ヶ月以内」「6ヶ月以内」のものを上位100件取得する
  def date(self, video_ids, dates, filter):
    # 動画の投稿日をdatetimeオブジェクトに変換し、そのインデックスをを取得し、tupleにする  (index, datetime)
    dates_tuple = [(i, datetime.strptime(d, '%Y-%m-%d')) for i, d in enumerate(dates)]

    # フィルタリング
    if filter == 1:
      date_range = timedelta(days=1)
    elif filter == 2:
      date_range = timedelta(weeks=1)
    elif filter == 3:
      date_range = timedelta(days=30)
    elif filter == 4:
      date_range = timedelta(days=90)
    elif filter == 5:
      date_range = timedelta(days=180)

    # 各時間範囲のリストを初期化
    within_date_range = []

    # 24時間以内、今週、今月、3ヶ月以内、6ヶ月以内に該当する日付を抽出
    now = datetime.now()
    for index, date_obj in dates_tuple:
      if date_obj > now - date_range:
        within_date_range.append((index, date_obj.strftime('%Y-%m-%d')))

    # 対応するvideo_idsを新しい配列に追加
    video_ids_within_date_range = [video_ids[index] for index, _ in within_date_range]

    return video_ids_within_date_range[:100]


# # テスト
# sort = Sort(order=2)
# video_ids = ['7338387769154309378', '7291648296278412552', '7317974982577900818', '7378063689741503761', '7253020686300531975', '7263775808970345729', '7266019070183525639', '7349541304419847425', '7338012157067447559', '7335009040839298322']
# video_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# diggs = [63400.0, 30700.0, 178500.0, 37100.0, 76600.0, 119700.0, 147800.0, 719100.0, 62300.0, 93000.0]
# dates = ['2024-02-22', '2023-12-29', '2023-10-19', '2024-02-13', '2024-06-08', '2023-10-22', '2023-07-07', '2023-08-05', '2024-03-23', '2024-02-21']
# # sort.route(video_ids, diggs, dates)
# print('------------------------')
# sort = Sort(order=3)
# video_ids = sort.route(video_ids, diggs, dates, filter=5)
# print(video_ids)