"""
深層学習モデル定義モジュール

FEMを模した肝臓変形シミュレーション用の深層学習モデルを定義します。
"""

import torch
import torch.nn as nn


class LiverDeformNet(nn.Module):
    """肝臓変形予測ネットワーク。

    入力: ノード座標と境界条件
    出力: 変形後のノード座標
    """

    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int, num_layers: int = 4) -> None:
        """モデルを初期化する。

        Args:
            input_dim: 入力次元数
            hidden_dim: 隠れ層の次元数
            output_dim: 出力次元数
            num_layers: 隠れ層の数
        """
        super().__init__()

        layers: list[nn.Module] = [nn.Linear(input_dim, hidden_dim), nn.ReLU()]
        for _ in range(num_layers - 1):
            layers += [nn.Linear(hidden_dim, hidden_dim), nn.ReLU()]
        layers.append(nn.Linear(hidden_dim, output_dim))

        self.network = nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """順伝播。

        Args:
            x: 入力テンソル (batch_size, input_dim)

        Returns:
            出力テンソル (batch_size, output_dim)
        """
        return self.network(x)


def build_model(config: dict) -> LiverDeformNet:
    """設定からモデルを構築する。

    Args:
        config: モデル設定の辞書

    Returns:
        構築されたモデル
    """
    return LiverDeformNet(
        input_dim=config.get("input_dim", 64),
        hidden_dim=config.get("hidden_dim", 256),
        output_dim=config.get("output_dim", 64),
        num_layers=config.get("num_layers", 4),
    )
