import datetime

now = datetime.datetime.now() # 現在時刻の取得
today = now.strftime('%Y年%m月%d日') # 現在時刻を年月曜日で表示

print("github-action-sample!!")
print(today)