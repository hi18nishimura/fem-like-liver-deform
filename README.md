# fem-like-liver-deform

FEMを模した深層学習による臓器変形シミュレーション

## プロジェクト概要

有限要素法 (FEM) を模した深層学習モデルにより、肝臓の変形をシミュレーションするリポジトリです。

## ディレクトリ構成

```
fem-like-liver-deform/
├── src/
│   ├── simulation/     # シミュレーションデータ生成
│   ├── preprocessing/  # データ前処理・CSV変換
│   ├── models/         # 深層学習モデル定義
│   ├── training/       # モデル学習
│   └── evaluation/     # モデル評価
├── data/
│   ├── raw/            # 生のシミュレーションデータ
│   └── processed/      # 前処理済みCSVデータ
├── configs/            # 設定ファイル (JSON)
├── notebooks/          # Jupyter Notebook (探索・可視化)
├── tests/              # ユニットテスト
├── docker/             # Docker設定
│   ├── Dockerfile
│   └── docker-compose.yml
├── requirements.txt
└── README.md
```

## セットアップ

### Docker を使う場合 (推奨)

```bash
# コンテナのビルドと起動
cd docker
docker compose up -d app

# コンテナに入る
docker compose exec app bash
```

Jupyter Lab を使う場合:

```bash
cd docker
docker compose up jupyter
# ブラウザで http://localhost:8888 を開く
```

### ローカル環境の場合

```bash
pip install -r requirements.txt
export PYTHONPATH=$(pwd)
```

## 使い方

### 1. シミュレーションデータの生成

```bash
python -m src.simulation.generate --output-dir data/raw --num-samples 1000 --config configs/simulation.json
```

### 2. データの前処理 (CSV変換)

```bash
python -m src.preprocessing.preprocess --input-dir data/raw --output-dir data/processed
```

### 3. モデルの学習

```bash
python -m src.training.train --config configs/training.json
```

### 4. モデルの評価

```bash
python -m src.evaluation.evaluate --config configs/evaluation.json
```

## テストの実行

```bash
pytest tests/
```

## 開発ガイドライン

- 各モジュールは `src/` 以下の対応するディレクトリで管理します。
- 設定値はコードにハードコードせず `configs/` 内のJSONファイルで管理します。
- 大きなデータファイルは `data/` に置き、Gitにはコミットしません。
- 学習済みモデルや評価結果は `outputs/` に出力されます (Gitには含みません)。
