from datetime import datetime, timedelta


class Sort():
  def __init__(self, order: int):
    self.order = order


  def route(self, video_ids, diggs, dates, filter=1):
    if self.order == 1:
      return self.rele(video_ids, dates, filter)
    elif self.order == 2:
      return self.digg(video_ids, dates, filter, diggs)
    elif self.order == 3:
      return self.date(video_ids, dates, filter)
    else:
      raise ValueError('order変数には、1, 2, 3のみが入ります。型はint型です。')
  

  # 1000件の動画のうち、関連度上位100件を配列で返す
  def rele(self, video_ids, dates, filter):
    # フィルタリング
    date_range = self.filtering(filter)

    # フィルタリングが不要な場合 (全ての動画を対象に、関連度順にソートする)
    if date_range == None:
      video_ids_sorted = video_ids

    else:
      # 各時間範囲のリストを初期化
      within_date_range = []

      # 動画の投稿日をdatetimeオブジェクトに変換し、そのインデックスをを取得し、tupleにする  (index, datetime)
      dates_tuple = [(i, datetime.strptime(d, '%Y-%m-%d')) for i, d in enumerate(dates)]

      # 24時間以内、今週、今月、3ヶ月以内、6ヶ月以内に該当する日付を抽出
      now = datetime.now()
      for index, date_obj in dates_tuple:
        if date_obj > now - date_range:
          within_date_range.append((index, date_obj.strftime('%Y-%m-%d')))

      # 対応するvideo_idsを新しい配列に追加
      video_ids_sorted = [video_ids[index] for index, _ in within_date_range]

    return video_ids_sorted[:100]


  # 1000件の動画のうち、いいね数が多い上位100件を配列で返す
  def digg(self, video_ids, dates, filter, diggs):

    # フィルタリング
    date_range = self.filtering(filter)

    # フィルタリングが不要な場合
    if date_range == None:
      # 全ての動画を対象に、diggsを小さい順にソートし、そのインデックスを取得 -> diggsのソート順にvideo_idsをソート
      sorted_indices = sorted(range(len(diggs)), key=lambda i: diggs[i], reverse=True)
      video_ids_sorted = [video_ids[i] for i in sorted_indices]
      diggs_sorted = [diggs[i] for i in sorted_indices]
      print(diggs_sorted)

    else:
      # date_rangeに含まれる動画のみを取得し、それをさらにいいね順にソートする
      now = datetime.now()
      filtered_indices = [i for i, d in enumerate(dates) if datetime.strptime(d, '%Y-%m-%d') > now - date_range]
      filtered_video_ids = [video_ids[i] for i in filtered_indices]
      filtered_diggs = [diggs[i] for i in filtered_indices]
      sorted_indices = sorted(range(len(filtered_diggs)), key=lambda i: filtered_diggs[i], reverse=True)
      video_ids_sorted = [filtered_video_ids[i] for i in sorted_indices]
      print("Filtered and sorted diggs:", [filtered_diggs[i] for i in sorted_indices])

    return video_ids_sorted[:100]


  # 1000件の動画のうち、投稿日が、「24時間以内」「今週」「今月」「3ヶ月以内」「6ヶ月以内」のものを上位100件取得する
  def date(self, video_ids, dates, filter):
    # 動画の投稿日をdatetimeオブジェクトに変換し、そのインデックスをを取得し、tupleにする  (index, datetime)
    dates_tuple = [(i, datetime.strptime(d, '%Y-%m-%d')) for i, d in enumerate(dates)]

    # フィルタリング
    date_range = self.filtering(filter)

    # フィルタリングが不要な場合
    if date_range == None:
      # 全ての動画を日付順でソートする
      sorted_dates = sorted(dates_tuple, key=lambda x: x[1])
      sorted_indices = [index for index, _ in sorted_dates]
      video_ids_sorted = [video_ids[i] for i in sorted_indices]

    else:
      # 各時間範囲のリストを初期化
      within_date_range = []

      # 24時間以内、今週、今月、3ヶ月以内、6ヶ月以内に該当する日付を抽出
      now = datetime.now()
      for index, date_obj in dates_tuple:
        if date_obj > now - date_range:
          within_date_range.append((index, date_obj.strftime('%Y-%m-%d')))

      # 対応するvideo_idsを新しい配列に追加
      video_ids_sorted = [video_ids[index] for index, _ in within_date_range]

    return video_ids_sorted[:100]
  

  # filter変数から対象動画の期間を指定する関数
  def filtering(self, filter: int):
    date_range = timedelta()

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
    else:  # 投稿日の指定が全範囲の場合
      date_range = None

    return date_range