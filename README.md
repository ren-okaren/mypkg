# mypkg: 西暦→和暦変換（ROS 2）

ROS 2 のサービス通信を使って、指定した西暦（例: 2004）を和暦（例: 平成16年）に変換してログに出力するパッケージです。

## 概要
- launch で2つのノードを起動します
- `year` パラメータで与えた西暦を和暦に変換し、結果をログに出力します

## ノード
- `year_pub`
  - パラメータ `year`（西暦）をサービス `/query` に送ります
- `listener`
  - サービス `/query` を受け取り、和暦に変換してログに出力します

## インタフェース
- Service: `/query`（`ren_msgs/srv/Query`）

## 使い方

### 1) ビルド
```bash
cd ~/ros2_ws
colcon build --packages-select ren_msgs mypkg
source install/local_setup.bash

### 2) 実行
`ros2 launch mypkg wareki.launch.py year:=2004`

### 3) 出力確認
ログに次のように表示されます：
- year=2004 -> 平成16年


## 実行
year に西暦を指定して起動します。
ros2 launch mypkg wareki.launch.py year:=2004

## 出力例
ログに次のような形式で表示されます（例）:
- year=2004 -> 平成16年

## ライセンス
MIT License. 詳細は `LICENSE` を参照してください。
各ソースファイル先頭にも SPDX 形式でライセンス情報を記載しています。
