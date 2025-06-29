# 创建目录
mkdir coco
cd coco
mkdir images
cd images

# 使用curl下载（等价于wget）
curl -O http://images.cocodataset.org/zips/train2017.zip

# 解压
unzip train2017.zip

# 删除zip文件（可选）
rm train2017.zip

# 移动到datasets目录
mv coco datasets/