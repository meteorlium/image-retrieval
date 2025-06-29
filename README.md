# image-retrieval
a toy project for local image retrieval

hello!

## 数据准备

使用 ShareGPT4V 数据集的图片+caption文本。

简略起见，只使用 datasets/ShareGPT4V/sharegpt4v_instruct_gpt4-vision_cap100k.json 的 10k 数据中的一部分。来自 coco/train2017, sam, llava/llava_pretrain.

```bash
# 下载 coco 图片
bash prepare/download_coco.sh

# 下载 ShareGPT4V caption 文本
python prepare/download_sharegpt4v.py
```