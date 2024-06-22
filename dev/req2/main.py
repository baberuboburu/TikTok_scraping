from req2.scr import Scr
from req2.sort import Sort
from req2.tiktok import TikTok
from req2.spreadsheet import SpreadSheet


def main2(word: str, spreadsheet_name: str, order: int, filter: int):
  # スクレイピング
  scr = Scr()
  video_ids, diggs, dates = scr.videoid_from_word(word=word)

  # いいね数と動画投稿日でVideo IDをソートする
  sort = Sort(order=order)
  sorted_video_ids = sort.route(video_ids, diggs, dates, filter)

  # 動画IDから動画情報を取得する
  tiktok = TikTok()
  matrix = [
    ['動画リンク', 'アカウントリンク', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
  ]
  for video_id in sorted_video_ids:
    user_info = tiktok.get_video_info(video_id)
    if user_info == None:
      pass
    else:
      matrix.append(user_info)
  
  # ['動画リンク', 'アカウントリンク', 'フォロー数', 'フォロワー数', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
  # アカウントリンクからそのユーザーのページに遷移し、フォロー数とフォロワー数を取得する



  # 取得した動画情報をスプレッドシートに入力する
  spreadsheet = SpreadSheet()
  spreadsheet.write(matrix=matrix, spreadsheet_name=spreadsheet_name, sheet_name=f'{word}(order:{order})')
  spreadsheet.style(spreadsheet_name=spreadsheet_name, sheet_name=f'{word}(order:{order})')