#!/usr/bin/env python3
"""
下载 ShareGPT4V 数据集
"""

from huggingface_hub import snapshot_download
import os

def download_sharegpt4v():
    dataset_name = "Lin-Chen/ShareGPT4V"
    local_dir = "./datasets/ShareGPT4V"
    
    print(f"开始下载数据集: {dataset_name}")
    print(f"保存路径: {local_dir}")
    
    # 创建目录
    os.makedirs(local_dir, exist_ok=True)
    
    try:
        # 下载整个数据集
        snapshot_download(
            repo_id=dataset_name,
            repo_type="dataset",
            local_dir=local_dir,
            local_dir_use_symlinks=False
        )
        print(f"✅ 数据集下载完成！保存在: {os.path.abspath(local_dir)}")
        
    except Exception as e:
        print(f"❌ 下载失败: {e}")

if __name__ == "__main__":
    download_sharegpt4v()