import gspread
from gspread_formatting import set_column_width, cellFormat, textFormat, color, format_cell_range
import os

dir_path = os.path.dirname(__file__) # 作業フォルダの取得
gc = gspread.oauth(
  credentials_filename=os.path.join(dir_path, "../auth/google_secret.json"), # 認証用のJSONファイル
  authorized_user_filename=os.path.join(dir_path, "../auth/google_authorized_user.json"), # 証明書の出力ファイル
)


class SpreadSheet():
  def __init__(self):
    dir_path = os.path.dirname(__file__) # 作業フォルダの取得
    self.gc = gspread.oauth(
      credentials_filename=os.path.join(dir_path, "../auth/google_secret.json"), # 認証用のJSONファイル
      authorized_user_filename=os.path.join(dir_path, "../auth/google_authorized_user.json"), # 証明書の出力ファイル
    )

  
  # 新しいスプレッドシートを作成する
  def create_spreadsheet(self, spreadsheet_name):
    spreadsheet = self.gc.create(spreadsheet_name)
    return spreadsheet
  

  # スプレッドシートにアクセスする
  def open_spreadsheet(self, spreadsheet_name):
    spreadsheet = self.gc.open(spreadsheet_name)
    return spreadsheet


  # 新しいシートを作成する
  def create_sheet(self, spreadsheet, sheet_name):
    try:
      sheet = spreadsheet.add_worksheet(title=sheet_name, rows=100, cols=26)
      return sheet
    except:
      # すでにシートが存在する場合はそのシートを開く
      sheet = spreadsheet.worksheet(sheet_name)
      return sheet
  

  # シートを選択する
  def open_sheet(self, spreadsheet, sheet_name):
    sheet = spreadsheet.worksheet(sheet_name)
    return sheet


  # 新しいシートを作成し，そこに書き込む
  def write(self, matrix, spreadsheet_name, sheet_name):
    spreadsheet = self.open_spreadsheet(spreadsheet_name=spreadsheet_name)
    sheet = self.create_sheet(spreadsheet=spreadsheet, sheet_name=sheet_name)

    # matrix変数の大きさに基づいて範囲を設定
    num_rows = len(matrix)
    num_cols = len(matrix[0]) if matrix else 0
    end_col_letter = chr(64 + num_cols)  # 列番号を文字に変換 (A=65, B=66, ...)
    cell_range = f'A1:{end_col_letter}{num_rows}'
    cell_list = sheet.range(cell_range)

    # cell_listを取得
    flat_values = [item for sublist in matrix for item in sublist]

    # セルに値を代入
    for i, cell in enumerate(cell_list):
      cell.value = flat_values[i]

    # スプレッドシートに更新のリクエストを送信
    sheet.update_cells(cell_list)


  # 既存のシートを取得し，デザインを整える
  def style(self, spreadsheet_name, sheet_name):
    spreadsheet = self.open_spreadsheet(spreadsheet_name=spreadsheet_name)
    sheet = self.open_sheet(spreadsheet=spreadsheet, sheet_name=sheet_name)
    
    # 1行目を固定する
    sheet.freeze(rows=1)
    
    # 特定の列の横幅を長くする (要件①)
    set_column_width(sheet, 'A', 400)
    set_column_width(sheet, 'C', 500)
    set_column_width(sheet, 'D', 400)

    # 1行目のstyleを調整する
    range_notation = 'A1:Z1'
    fmt = cellFormat(
      backgroundColor=color(0.9, 0.9, 0.9),
      textFormat=textFormat(
        bold=True, 
        foregroundColor=color(1, 0, 0),
        fontSize=12
      ),
      horizontalAlignment='CENTER'
    )
    format_cell_range(sheet, range_notation, fmt)