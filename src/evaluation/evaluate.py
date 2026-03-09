"""
モデル評価モジュール

学習済みモデルの評価を行います。
"""

import argparse
import json
import os

import torch
import torch.nn as nn

from src.models.network import build_model


def evaluate(config: dict) -> dict:
    """学習済みモデルを評価する。

    Args:
        config: 評価設定の辞書

    Returns:
        評価指標の辞書 (例: {"mse": ..., "mae": ...})
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用デバイス: {device}")

    model = build_model(config.get("model", {})).to(device)
    checkpoint_path = config.get("checkpoint_path", "outputs/checkpoints/model_final.pth")
    model.load_state_dict(torch.load(checkpoint_path, map_location=device))
    model.eval()

    data_path = config.get("data_path", "data/processed/dataset.csv")

    import pandas as pd

    df = pd.read_csv(data_path)
    # TODO: 実データの列構成に合わせて入力列と出力列を分割する
    # 例: input_cols = [c for c in df.columns if c.startswith("input_")]
    #     target_cols = [c for c in df.columns if c.startswith("target_")]
    #     inputs = torch.tensor(df[input_cols].values, dtype=torch.float32).to(device)
    #     targets = torch.tensor(df[target_cols].values, dtype=torch.float32).to(device)
    raise NotImplementedError("実データの列定義に合わせて入力・出力の分割を実装してください。")

    with torch.no_grad():
        predictions = model(inputs)

    mse = nn.functional.mse_loss(predictions, targets).item()
    mae = nn.functional.l1_loss(predictions, targets).item()

    metrics = {"mse": mse, "mae": mae}
    print(f"評価結果 - MSE: {mse:.6f}, MAE: {mae:.6f}")

    output_dir = config.get("output_dir", "outputs/evaluation")
    os.makedirs(output_dir, exist_ok=True)
    metrics_path = os.path.join(output_dir, "metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(metrics, f, indent=2)
    print(f"評価指標を {metrics_path} に保存しました。")

    return metrics


def main() -> None:
    parser = argparse.ArgumentParser(description="モデル評価")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/evaluation.json",
        help="評価設定ファイルのパス",
    )
    args = parser.parse_args()

    config = {}
    if os.path.exists(args.config):
        with open(args.config) as f:
            config = json.load(f)

    evaluate(config)


if __name__ == "__main__":
    main()
