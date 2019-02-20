# AmazonReview
このリポジトリは"書籍レビューに関するネタバレ判定ツールによる実験"で用いたプログラムです。

# 環境
## 動作環境
+ OS : macOs Mojave 10.14
+ 統合開発環境 : 
+ python : 3.6.4

## ライブラリバージョン
+ mecab-python3 0.7
+ scikit-learn 0.20.2
+ pandas 0.23.4
+ selenium 3.141.0
+ numpy 1.14.3

# ソースコードについて
ここでは説明が必要なファイルについて説明します。

## clawler
+ get.review.pyを実行した場合、booklist.csvの書籍レビューを自動で取得します。
  - web driver(chlome)を事前にダウンロードし、~/driver/chromedriver　に置く必要あり

## preprocessing
+ create_train_data.pyでレビューの分かち書きをネタバレ有無に分けて、作品ごとに出力
+ select_rand_novel.pyで15/50作品の場合の作品をランダムで抽出しbooklistを作成する
+ joint_use_traindata.pyで全体データのネタバレ有無のコーパスを出力

## src直下
+ review_classify.pyでNBによる学習および分類を行います
+ correct_answer_rate.pyで正解率とF値を出力します

# 更新情報
以下のGitHubで随時更新を行っています。
エラー等ある場合はpull requestを送っていただければ対応します。
https://github.com/whiteblues1017/AmazonReview
