"""
シミュレーションデータ前処理モジュール

シミュレーションデータをパースして必要なデータを抽出し、CSVファイルに保存します。
"""

import argparse
import os
from pathlib import Path

import pandas as pd


def parse_simulation_file(filepath: str) -> dict:
    """シミュレーションファイルをパースしてデータを抽出する。

    Args:
        filepath: シミュレーションファイルのパス

    Returns:
        抽出されたデータの辞書
    """
    # TODO: シミュレーションファイルのパース実装
    return {}


def preprocess(input_dir: str, output_dir: str) -> None:
    """シミュレーションデータを前処理してCSVに保存する。

    Args:
        input_dir: 入力データのディレクトリ (生データ)
        output_dir: 出力先ディレクトリ (処理済みCSV)
    """
    os.makedirs(output_dir, exist_ok=True)

    records = []
    input_path = Path(input_dir)
    for filepath in sorted(input_path.glob("*")):
        if filepath.is_file() and not filepath.name.startswith("."):
            data = parse_simulation_file(str(filepath))
            records.append(data)

    if records:
        df = pd.DataFrame(records)
        output_file = os.path.join(output_dir, "dataset.csv")
        df.to_csv(output_file, index=False)
        print(f"{len(records)} 件のデータを {output_file} に保存しました。")
    else:
        print("処理対象のデータが見つかりませんでした。")


def main() -> None:
    parser = argparse.ArgumentParser(description="シミュレーションデータ前処理")
    parser.add_argument(
        "--input-dir",
        type=str,
        default="data/raw",
        help="入力データのディレクトリ (デフォルト: data/raw)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="data/processed",
        help="出力先ディレクトリ (デフォルト: data/processed)",
    )
    args = parser.parse_args()

    preprocess(args.input_dir, args.output_dir)


if __name__ == "__main__":
    main()
