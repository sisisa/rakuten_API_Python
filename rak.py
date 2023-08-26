import requests

# 楽天商品検索API (BooksGenre/Search/)のURL
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

# URLのパラメータ
param = {
    # 取得したアプリIDを設定する
    "applicationId" : "APP_ID",
    "keyword" : "Python",
    "format" : "json"
}

# APIを実行して結果を取得する
result = requests.get(url, param)

# jsonにデコードする
json_result = result.json()

# 整形した結果を格納する辞書型変数を宣言
dict_result = {}

# 取得結果を1件ずつ取り出す
for i in range(0, len(json_result["Items"])):
    item = json_result["Items"][i]["Item"]

    # keyに「商品名（itemName）」、valueに「値段（itemPrice）」を設定する
    dict_result[item["itemName"]] = item["itemPrice"]

# 整形した結果を1件ずつ出力する
for itemName, itemPrice in dict_result.items():
    print(itemName, itemPrice, "円")