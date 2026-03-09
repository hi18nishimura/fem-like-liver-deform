"""
シミュレーションデータ生成モジュール

FEMを模した肝臓変形シミュレーションデータを生成します。
"""

import argparse
import json
import os


def generate_simulation_data(output_dir: str, num_samples: int, config: dict) -> None:
    """シミュレーションデータを生成してファイルに保存する。

    Args:
        output_dir: 出力先ディレクトリ
        num_samples: 生成するサンプル数
        config: シミュレーション設定パラメータ
    """
    os.makedirs(output_dir, exist_ok=True)
    # TODO: FEMシミュレーションの実装
    print(f"{num_samples} サンプルのシミュレーションデータを {output_dir} に生成します。")


def main() -> None:
    parser = argparse.ArgumentParser(description="シミュレーションデータ生成")
    parser.add_argument(
        "--output-dir",
        type=str,
        default="data/raw",
        help="出力先ディレクトリ (デフォルト: data/raw)",
    )
    parser.add_argument(
        "--num-samples",
        type=int,
        default=1000,
        help="生成するサンプル数 (デフォルト: 1000)",
    )
    parser.add_argument(
        "--config",
        type=str,
        default="configs/simulation.json",
        help="シミュレーション設定ファイルのパス",
    )
    args = parser.parse_args()

    config = {}
    if os.path.exists(args.config):
        with open(args.config) as f:
            config = json.load(f)

    generate_simulation_data(args.output_dir, args.num_samples, config)


if __name__ == "__main__":
    main()
