"""モデル定義モジュールのテスト"""

import torch

from src.models.network import LiverDeformNet, build_model


def test_liver_deform_net_forward():
    model = LiverDeformNet(input_dim=8, hidden_dim=16, output_dim=4, num_layers=2)
    x = torch.randn(4, 8)
    out = model(x)
    assert out.shape == (4, 4)


def test_build_model():
    config = {"input_dim": 16, "hidden_dim": 32, "output_dim": 8, "num_layers": 3}
    model = build_model(config)
    x = torch.randn(2, 16)
    out = model(x)
    assert out.shape == (2, 8)
