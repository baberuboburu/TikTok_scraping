from tiktokapipy.api import TikTokAPI
import pprint
import os
import logging

logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), "./tiktok.log"), encoding="utf-8",
                    level=logging.DEBUG)
cur_dir = os.path.dirname(os.path.abspath(__file__))


def search():
    creator_list = []
    with TikTokAPI() as api:
        challenge = api.challenge("ダンス", video_limit=1)
        for video in challenge.videos:
          # print(video)
          # 動画リンク
          print(video.url)
          # アカウントリンク
          print(video.creator._unique_id)
          # フォロー数
          # フォロワー数
          # 投稿日
          print(video.create_time)
          # 投稿文章
          # 音楽
          print(video.music)
          # 再生数
          print(video.stats.play_count)
          # いいね数

          # コメント数
          print(video.stats.comment_count)
          # シェア数
          print(video.stats.share_count)
          # 保存数
          print(video.stats.collect_count)
          # creator_list.append(video.creator._unique_id)
          # #追加したい項目 、タイトル（概要）、タグ、ID（リンク→アカウント）、動画ID（リンク→動画）
    # print(creator_list)
    
def paste_video_html():
    """
    <blockquote class="tiktok-embed" style="max-width: 605px; min-width: 325px;" \
        cite="https://www.tiktok.com/@{user_id}/video{videoID}" data-video-id="{videoID}"><section></section></blockquote>
<script async src="https://www.tiktok.com/embed.js"></script>
    """

    
def get_video_info():
    with TikTokAPI() as api:
        video = api.video("https://m.tiktok.com/v/7369122552901356821")
        # print(video.desc)
        # print(video.url)
        # print(video.id)
        # print(video.challenges)
        # print(video.music)
        # print(video.item_comment_status)
        # print(video.author)
        for comment in video.comments:
          # text = comment['text']
          # user_id = comment['user']['unique_id']
          # nickname = comment['user']['nickname']
          # create_time = comment['create_time']
          # digg_count = comment['digg_count']
          # reply_count = comment['reply_comment_total']

          # print(f"Comment: {text}")
          # print(f"User ID: {user_id}, Nickname: {nickname}")
          # print(f"Created at: {create_time}")
          # print(f"Digg Count: {digg_count}, Replies: {reply_count}")
          print(comment)

        comments = [comment.text for comment in video.comments]
        print(comments)
        print(len(comments))
        # print(video.tags._challenge_names)
        # print(video.creator._unique_id)
        # print(video.create_time)
        # print(video.stats.digg_count)
        # print(video.stats.comment_count)
        # print(video.stats.play_count)
        # print(video.video.ratio)
        # print(video.video.duration)
        # print(video.video.download_addr)
        # video.download()

        # クリエーター情報
        print('---------- クリエーター情報 ----------')
        creator = video.creator
        a = creator._api
        print(dir(creator._api))
        print(creator._unique_id)
        print(dir(a._scrape_data))
        print(dir(a.user))
        print(dir(a.video))
        print(dir(a.challenge))
        print(a.context)
        # creator_id = creator._unique_id
        # creator_sec = creator._
        # creator_nickname = creator._nickname
        # print(creator_id)
        # print(creator_sec)
        # print(creator_nickname)
        print(creator)
        # 動画リンク
        print('---------- 動画リンク ----------')
        print(video.url)
        # アカウントリンク
        print('---------- アカウントリンク ----------')
        unique_id = video.creator._unique_id
        account_link = f'https://www.tiktok.com/@{unique_id}'
        print(account_link)
        # フォロー数
        print('---------- フォロー数 ----------')
        # フォロワー数
        print('---------- フォロワー数 ----------')
        # 投稿日
        print('---------- 投稿日 ----------')
        create_time = str(video.create_time)[:10]
        print(create_time)
        # 投稿文章
        print('---------- 投稿文章 ----------')
        print(video.desc)
        # 音楽
        print('---------- 音楽 ----------')
        print(video.music.play_url)
        # 再生数
        print('---------- 再生数 ----------')
        print(video.stats.play_count)
        # いいね数
        print('---------- いいね数 ----------')
        print(video.stats.digg_count)
        # コメント数
        print('---------- コメント数 ----------')
        print(video.stats.comment_count)
        print(len(comments))
        # シェア数
        print('---------- シェア数 ----------')
        print(video.stats.share_count)
        # 保存数
        print('---------- 保存数 ----------')
        print(video.stats.collect_count)




def do_something():
    username = "user62218766038151"  # ここに対象のユーザー名を入力
    with TikTokAPI() as api:
        user = api.user(username, video_limit=1)
        print(user)
        # for video in user.videos:
        #     num_comments = video.stats.comment_count
        #     num_likes = video.stats.digg_count
        #     num_views = video.stats.play_count
        #     num_shares = video.stats.share_count
            
            # # 取得した情報を表示
            # print(f"Video ID: {video.id}")
            # print(f"Comments: {num_comments}")
            # print(f"Likes: {num_likes}")
            # print(f"Views: {num_views}")
            # print(f"Shares: {num_shares}")
            # print("------")
    
if __name__ == "__main__":
    # print(cur_dir)
    # search()
    get_video_info()
    # do_something()