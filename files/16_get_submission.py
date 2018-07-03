from PIL import Image
import json
res = []
### 选手提交的文件名称，对应答案集合5个tif文件
file_list = ['03+261mask.tif','03+262mask.tif','04+246mask.tif','04+248mask.tif','04+251mask.tif']

with open('my_submission.json','w') as final: # 创建一个json文件，把pixel的信息存进去
	for i in range(0,len(file_list)):
		tmp_pic = Image.open(file_list[i]).convert('L') # 读取图片，按照要求转化为灰度图
		(x,y) = tmp_pic.size # 找到图片size
		tmp_pixel = [] # 创建一个list，便于记录pixel信息
		data  = {} # 创建一个dict，记录每张图片中，要被写入的信息
		for p in range(x):
			for q in range(y):
				tmp_pixel.append(tmp_pic.getpixel((p,q))) # 遍历每个像素点，把pixel信息存入tmp_pixel
		data['name'] = file_list[i] # 定义dict的key为name，对应的value存入图片的名称
		data['size'] = [x,y] # 定义dict的key为size，对应的value存入图片的size
		data['pixel'] = tmp_pixel # 定义dict的key为pixel，对应的value存入图片的pixel
		res.append(data)
	final.write(json.dumps(res))
final.close()

### 示例json_file
"""
[
{"name": "03+261mask.tif", 
"size": [3, 3], 
"pixel": [1, 1, 1, 
		1, 1, 1, 
		1, 1, 1]},
{"name": "03+262mask.tif", 
"size": [2, 2], 
"pixel": [2, 2, 
		2, 2]}
]
"""