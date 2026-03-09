"""シミュレーションデータ生成モジュールのテスト"""

import os
import tempfile

from src.simulation.generate import generate_simulation_data


def test_generate_simulation_data_creates_output_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        output_dir = os.path.join(tmpdir, "output")
        generate_simulation_data(output_dir, num_samples=1, config={})
        assert os.path.isdir(output_dir)
