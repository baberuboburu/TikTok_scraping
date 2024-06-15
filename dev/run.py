from req1.main import main1
# from req2.main import main2


# 要件①
# user_id = 'nanaaaa_0620'
user_id = 'music_mana5'
spreadsheet_name = 'test01'

main1(user_id, spreadsheet_name)


# 要件②
word = 'カラオケ'
spreadsheet_name = 'test02'
order = 1  # 関連度数
# order = 2  # いいね数
# order = 3  # 動画投稿日

# main2(user_id, spreadsheet_name, order)




'''
【クライアントへの共有事項】
・Google ColaboratoryはTikTokへのスクレイピングの互換性が悪い(versionに対して不安定な)ため利用を避けた
・Google Spreadsheetから音楽URLへのアクセスができず、一度コピーしてブラウザに貼り付ける必要がある
・TikTokのスクレイピング対策に対して、手動で行う操作があること

【開発メモ】
・投稿を35個しか取得できないのは、ライブラリの初期設定の可能性がある
-> 解決
・コメントに対するコメントの内容のスクレイピングはしんどい -> やらない (要件⑤)
'''