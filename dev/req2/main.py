from scr import Scr
from sort import Sort
from tiktok import TikTok
from spreadsheet import SpreadSheet


def main2(word: str, spreadsheet_name: str, order: int):
  # スクレイピング
  scr = Scr()
  video_ids, diggs, dates = scr.videoid_from_word(word=word)

  # いいね数と動画投稿日でVideo IDをソートする
  sort = Sort(order=order)
  sorted_video_ids = sort.route(video_ids, diggs, dates)

  # 動画IDから動画情報を取得する
  tiktok = TikTok()
  matrix = [
    ['動画リンク', 'アカウントリンク', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
  ]
  for video_id in video_ids:
    user_info = tiktok.get_video_info(video_id)
    matrix.append(user_info)
  
  # ['動画リンク', 'アカウントリンク', 'フォロー数', 'フォロワー数', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
  # アカウントリンクからそのユーザーのページに遷移し、フォロー数とフォロワー数を取得する



  # 取得した動画情報をスプレッドシートに入力する
  spreadsheet = SpreadSheet()
  spreadsheet.write(matrix=matrix, spreadsheet_name=spreadsheet_name, sheet_name=f'@{word}')
  spreadsheet.style(spreadsheet_name=spreadsheet_name, sheet_name=f'@{word}')


'''
【実装方法】
1. 検索ワードに対して上位1000件ほどの動画を取得する -> scr.py(完成)
2. 「関連性(デフォルト)」「投稿日」「いいね数」でデータをソートし、上位100件を取得する -> sort.py
3. Google Spreadsheetに記述する -> spreadsheet.py(完成)

【残タスク】
・35件以上の動画を取得する方法 (無限スクロール？)
・XPATHで指定した要素の子要素を順に取得できるか
・各要素から「投稿日」「いいね数」を取得する
・ソートし、上位100件ほどを取得する

【問題点】
・ソートがうまくできるか
'''