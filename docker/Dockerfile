# ベースイメージ: PyTorch + CUDA
FROM pytorch/pytorch:2.2.0-cuda12.1-cudnn8-runtime

# 作業ディレクトリの設定
WORKDIR /workspace

# システムパッケージのインストール
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python依存パッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードのコピー
COPY . .

# PYTHONPATHの設定
ENV PYTHONPATH="/workspace:${PYTHONPATH}"

CMD ["bash"]
