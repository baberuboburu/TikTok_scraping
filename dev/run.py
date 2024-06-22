from req1.main import main1
from req2.main import main2


# 要件①
# user_id = 'nanaaaa_0620'
user_id = 'music_mana5'
# user_id = 'bstbs_sports'
spreadsheet_name = 'test02'

# main1(user_id, spreadsheet_name)


# 要件②
word = 'King Gnu'
spreadsheet_name = 'test02'
# order = 1  # 関連度数
# order = 2  # いいね数
order = 3  # 動画投稿日
# filter = 1  # 1日以内
# filter = 2  # 1週間以内
filter = 3  # 1ヶ月以内
# filter = 4  # 3ヶ月以内
# filter = 5  # 6ヶ月以内
# filter = 6  # 全範囲

# main2(word, spreadsheet_name, order, filter)


main1(user_id, spreadsheet_name)

'''
【クライアントへの共有事項】
・Google ColaboratoryはTikTokへのスクレイピングの互換性が悪い(versionに対して不安定な)ため利用を避けた
・Google Spreadsheetから音楽URLへのアクセスができず、一度コピーしてブラウザに貼り付ける必要がある
-> 解決
・TikTokのスクレイピング対策に対して、手動で行う操作があること
-> クライアント承認済み

【クライアントからの指摘】
・要件①
 - Google Colaboratory上でできないか再度検討してほしい
 - 音楽の項目は、URLではなく楽曲名で取得してほしい
 - それ以外はOK

【問題点】
・Internal かつ Testingの場合、Google WorkSpaceのOathが7日で失効してしまい、毎回シークレットキーを再発行する必要がある
-> 解決

【開発メモ】
・コメントに対するコメントの内容のスクレイピングはしんどい -> やらない (要件③)
'''