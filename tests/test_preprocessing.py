"""前処理モジュールのテスト"""

import os
import tempfile

from src.preprocessing.preprocess import preprocess


def test_preprocess_creates_output_dir():
    with tempfile.TemporaryDirectory() as tmpdir:
        input_dir = os.path.join(tmpdir, "raw")
        output_dir = os.path.join(tmpdir, "processed")
        os.makedirs(input_dir, exist_ok=True)
        preprocess(input_dir, output_dir)
        assert os.path.isdir(output_dir)
