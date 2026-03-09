"""
モデル学習モジュール

深層学習モデルの学習ループを実装します。
"""

import argparse
import json
import os

import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset

from src.models.network import build_model


def load_dataset(data_path: str) -> tuple[torch.Tensor, torch.Tensor]:
    """CSVデータセットを読み込んでテンソルに変換する。

    Args:
        data_path: CSVファイルのパス

    Returns:
        (入力テンソル, ターゲットテンソル) のタプル
    """
    import pandas as pd

    df = pd.read_csv(data_path)
    # TODO: 実データの列構成に合わせて入力列と出力列を分割する
    # 例: input_cols = [c for c in df.columns if c.startswith("input_")]
    #     target_cols = [c for c in df.columns if c.startswith("target_")]
    #     inputs = torch.tensor(df[input_cols].values, dtype=torch.float32)
    #     targets = torch.tensor(df[target_cols].values, dtype=torch.float32)
    raise NotImplementedError("実データの列定義に合わせて入力・出力の分割を実装してください。")


def train(config: dict) -> None:
    """モデルを学習する。

    Args:
        config: 学習設定の辞書
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"使用デバイス: {device}")

    model = build_model(config.get("model", {})).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=config.get("learning_rate", 1e-3))
    criterion = nn.MSELoss()

    data_path = config.get("data_path", "data/processed/dataset.csv")
    inputs, targets = load_dataset(data_path)
    dataset = TensorDataset(inputs, targets)
    dataloader = DataLoader(dataset, batch_size=config.get("batch_size", 32), shuffle=True)

    num_epochs = config.get("num_epochs", 100)
    output_dir = config.get("output_dir", "outputs/checkpoints")
    os.makedirs(output_dir, exist_ok=True)

    for epoch in range(1, num_epochs + 1):
        model.train()
        total_loss = 0.0
        for x_batch, y_batch in dataloader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)
            optimizer.zero_grad()
            pred = model(x_batch)
            loss = criterion(pred, y_batch)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(x_batch)

        avg_loss = total_loss / len(dataset)
        if epoch % 10 == 0 or epoch == 1:
            print(f"Epoch [{epoch}/{num_epochs}] Loss: {avg_loss:.6f}")

    checkpoint_path = os.path.join(output_dir, "model_final.pth")
    torch.save(model.state_dict(), checkpoint_path)
    print(f"モデルを {checkpoint_path} に保存しました。")


def main() -> None:
    parser = argparse.ArgumentParser(description="モデル学習")
    parser.add_argument(
        "--config",
        type=str,
        default="configs/training.json",
        help="学習設定ファイルのパス",
    )
    args = parser.parse_args()

    config = {}
    if os.path.exists(args.config):
        with open(args.config) as f:
            config = json.load(f)

    train(config)


if __name__ == "__main__":
    main()
