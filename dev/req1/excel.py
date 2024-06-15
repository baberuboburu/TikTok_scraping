import openpyxl


class Excel():
  def __init__(self):
    pass


  def write(self, matrix, sheet_name, file_name='test.xlsx'):
    # 新しいワークブックを作成
    wb = openpyxl.Workbook()

    # デフォルトのワークシートを取得
    ws = wb.active

    # ワークシートの名前を変更
    ws.title = sheet_name

    # 行列を書き込む
    for row in matrix:
        ws.append(row)

    # ファイルに保存
    wb.save(file_name)

# 使用例
# matrix = [
#   ['動画リンク', '投稿日', '投稿文章', '音楽', '再生数', 'いいね数', 'コメント数', 'シェア数', '保存数']
# ]
# write_matrix_to_excel(matrix, 'example.xlsx')