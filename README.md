# mypkg: 西暦 → 和暦変換（ROS 2）

## 概要
本パッケージは、ROS 2 のサービス通信を用いて 
**西暦（例: 2004）を和暦（例: 平成16年）に変換するサービスを提供するパッケージ**です。

他ノードからのサービス要求に応じて変換処理を行い、
結果をレスポンスとして返します。

---

## 構成
本パッケージは、以下の 2 つのノードから構成されます。

- `wareki_server`
  - サービス `/ad_to_wareki` を提供するノード
  - 西暦を受け取り、対応する和暦文字列をレスポンスとして返します

- `year_pub`
  - 起動時にパラメータとして与えられた西暦を、
    サービス `/ad_to_wareki` にリクエストとして送信するノード

---

## 実行方法

### launch で実行
西暦をパラメータで与えて起動します（例：2004）。

```
ros2 launch mypkg wareki.launch.py year:=2004
```

##動作確認例
起動すると、`year_pub` が指定した西暦をサービス `/ad_to_wareki` にリクエストし、
wareki_server が和暦に変換してレスポンスし、結果がログに表示されます。
例:
`[wareki_server] [INFO] ... service /ad_to_wareki ready`
`[wareki_server] [INFO] ... req: 2004 -> 平成16年`

---

## インタフェース

### Service: `/ad_to_wareki`

使用するサービス型は以下の通りです。

`mypkg_interfaces/srv/AdTowareki`

```text
int32 ad_year
---
string wareki
```
`ad_year`:西暦
`wareki`:変換後の和暦文字
