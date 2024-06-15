from req1.scr import Scr
from req1.tiktok import TikTok
from req1.spreadsheet import SpreadSheet


def main1(user_id: str, spreadsheet_name: str):
  # スクレイピング
  scr = Scr()
  video_ids = scr.videoid_from_userid(user_id=user_id)
  print(len(video_ids))

  # 動画IDから動画情報を取得する
  tiktok = TikTok()
  matrix = [
    ['動画リンク', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
  ]
  for video_id in video_ids:
    user_info = tiktok.get_video_info(video_id)
    matrix.append(user_info)

  # 取得した動画情報をスプレッドシートに入力する
  spreadsheet = SpreadSheet()
  spreadsheet.write(matrix=matrix, spreadsheet_name=spreadsheet_name, sheet_name=f'@{user_id}')
  spreadsheet.style(spreadsheet_name=spreadsheet_name, sheet_name=f'@{user_id}')



'''
完成
'''