# pra_github_actions

GithubActionの勉強用のメモを記載。

下記youtubeチャンネル、記事を元に勉強。
https://www.youtube.com/watch?v=R7FtZfT6YBI&ab_channel=%E3%81%AF%E3%81%97%E3%81%A8%E3%81%AE%E3%83%A2%E3%83%8E%E4%BD%9C%E3%82%8A%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB

https://zenn.dev/hashito/articles/7c292f966c0b59


# 目標

定期実行で.pyを実行し、printすることができること。


## GithubActionの簡単な動かし方

- レポジトリを作成して、クローンする。

※　2023/1/4現在では、パブリックのGithubActionは無料だが、プライベートのGithubActionはある一定容量を超えると有料になる。


- 「.github/workflows/」を作成する。 

- 「.github/workflows/」配下に「run.yaml」を作成し、以下を記載。


~~~
name: main-name

# pushしたときに以下のJobが実行される。
on: [push]

jobs:
  job-name:
    # Ubuntsuの最新バージョンで動作させる。
    runs-on: ubuntu-latest
    steps:
      - run: echo "this is pen"
~~~

これだけでGithubActionが実行される。


## GithubAction　マーケットプレイスの使い方

以下のように、usesでマーケットプレイスのGithubActionを使用することができる。下記で使用しているのは、Checkoutを使用している。

https://github.com/marketplace/actions/checkout

~~~
name: main-name

# pushしたときに以下のJobが実行される。
on: [push]

jobs:
  job-name:
    # Ubuntsuの最新バージョンで動作させる。
    runs-on: ubuntu-latest
    steps:
      - run: echo "this is pen"
      # マーケティングの指定　バージョンまで指定できると安定
      - uses: actions/checkout@v3
      - run: |
          ls -al
          cd .github/workflows/
          ls -al
~~~

マーケットプレイスは以下から検索可能。
https://github.com/marketplace?type=

## GithubActionの環境変数等

一旦飛ばす

## GithubActionの実行タイミング

「on: [push]」の部分を変更することで対応可能。
具体例としては、以下
https://docs.github.com/ja/actions/using-workflows/events-that-trigger-workflows

例えば、定期実行であれば以下。
~~~
on:
  schedule:
    - cron:  '*/1 * * * *' #1分に1回実行
~~~

マニュアル実行(on: workflow_dispatch)などもすることができる


## 目標物の作成

以下記事を参考に、Pythonコードを作成する。

https://helve-blog.com/posts/git/github-actions-python/






