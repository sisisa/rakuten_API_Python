import requests
import json

# 楽天商品検索API (BooksGenre/Search/)のURL
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"

# URLのパラメータ
params = {
    "applicationId": "APP_ID",
    "keyword": "Python",
    "format": "json"
}

# APIを実行して結果を取得する
response = requests.get(url, params=params)

# JSONデータを取得する
json_data = response.json()

# 取得結果を格納する辞書型変数を宣言
dict_result = {}

# 取得結果を1件ずつ取り出す
for item in json_data["Items"]:
    item_info = item["Item"]

    # 商品名をキー、値段を値として辞書に追加する
    dict_result[item_info["itemName"]] = item_info["itemPrice"]

# JSONファイルに出力する
output_filename = "result.json"
with open(output_filename, "w", encoding="utf-8") as output_file:
    json.dump(dict_result, output_file, ensure_ascii=False, indent=4)

# 結果の表示
for itemName, itemPrice in dict_result.items():
    print(itemName, itemPrice, "円")

print("JSONデータを", output_filename, "に保存しました。")
