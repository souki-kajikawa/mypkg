# ネットワーク受信量監視コマンド
ロボットシステム学　課題2

## 目次
- 概要
- 使用準備
- 実行方法
- ソフトウェア
- テスト環境
- ライセンス

## 概要
3秒ごとのネットワークから受信したデータ量を表示するプログラムです.　　

## 使用準備
以下のコマンドをターミナルで実行します.
```
$ git clone git@github.com:souki-kajikawa/mypkg.git
$ cd mypkg
```

## 実行方法
psutil.net_io_counters()を用いて３秒ごとに受信したデータ量(byte)を取得し出力します.
- 実行例
```
$ ros2 launch mypkg talk_listen.launch.py
[listener-2] [INFO] [1766905354.295706046] [listener]: receive: 1232
```

## ソフトウェア
- Python
  - テスト済みバージョン 3.13.5

## テスト環境
Ubuntu 24.04.3 LTS

## ライセンス
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.



©　2025 Souki Kajikawa
