from tiktokapipy.api import TikTokAPI


class TikTok():
  def __init__(self):
    pass
  

  def get_video_info(self, video_id):
    try:
      with TikTokAPI() as api:
        video = api.video(f'https://m.tiktok.com/v/{video_id}')

        # 動画リンク
        print('---------- 動画リンク ----------')
        video_link = video.url
        print(video_link)

        # アカウントリンク
        print('---------- アカウントリンク ----------')
        unique_id = video.creator._unique_id
        account_link = f'https://www.tiktok.com/@{unique_id}'
        print(account_link)

        # 投稿日
        print('---------- 投稿日 ----------')
        create_time = str(video.create_time)[:10]
        print(create_time)

        # 投稿文章
        print('---------- 投稿文章 ----------')
        post_sentence = video.desc
        print(post_sentence)

        # 音楽
        print('---------- 音楽 ----------')
        music = video.music.play_url
        print(music)

        # 再生数
        print('---------- 再生数 ----------')
        play_counts = video.stats.play_count
        print(play_counts)

        # いいね数
        print('---------- いいね数 ----------')
        digg_counts = video.stats.digg_count
        print(digg_counts)

        # コメント数
        print('---------- コメント数 ----------')
        comment_counts = video.stats.comment_count
        print(comment_counts)

        # シェア数
        print('---------- シェア数 ----------')
        share_counts = video.stats.share_count
        print(share_counts)

        # 保存数
        print('---------- 保存数 ----------')
        collect_counts = video.stats.collect_count
        print(collect_counts)

        # # 要件①
        # user_info = [video_link, create_time, post_sentence, music, play_counts, digg_counts, comment_counts, share_counts, collect_counts]
        # 要件② (followsとfollowersが足りない)
        user_info = [video_link, account_link, create_time, post_sentence, music, play_counts, digg_counts, comment_counts, share_counts, collect_counts]
        return user_info

    except:
      user_info = None
      return user_info


tiktok = TikTok()
tiktok.search()