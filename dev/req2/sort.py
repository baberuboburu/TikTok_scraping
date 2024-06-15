


class Sort():
  def __init__(self, order: int):
    self.order = order


  def route(self, video_ids, diggs, dates):
    if self.order == 1:
      return video_ids[:100]
    elif self.order == 2:
      return self.digg(self, video_ids, diggs)
    elif self.order == 3:
      return self.date(self, video_ids, dates)
    else:
      raise ValueError('order変数には、1, 2, 3のみが入ります。型はint型です。')

   # 1000件の動画のうち、いいね数が多い上位100件を配列で返す
  def digg(self, video_ids, diggs):
    return video_ids[:100]


  # 1000件の動画のうち、投稿日が、「24時間以内」「今週」「今月」「3ヶ月以内」「6ヶ月以内」のものを上位100件取得する
  def date(self, video_ids, dates):
    return video_ids[:100]