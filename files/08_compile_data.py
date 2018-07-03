## 把1000个label对应的json文件按照格式要求，拼接为一个大的json文件，便于选手提交内容和进行评审
## 生成答案文件(选手可按照同样的规范方式，在本地生成自己提交的文件，便于线上测评)
import json 
res = []
file_path_list = [] # you have to make it work
label = [] # you have to make it work
# the codes below indicate how to generate the submision file for evaluation
with open('my_submission.json','w') as final:
	for i in range(0,1000): # totally 1000 files need to be parsed
		with open(file_path_list[i]) as in_put:
			data = json.load(in_put)
			tmp = {}
			tmp['label'] = label[i]
			tmp['data'] = data
		res.append(tmp)
	final.write(json.dumps(res))
final.close()

# 最终生成的json文件参考
"""
[
	{
	"label": "000000.json", # gererate from lablelist
	"data": {
		"lanes_x": [[01, 02, 03, 04, 05, 06, 07, 08, 09], # left_lane 
        [01, 02, 03, 04, 05, 06, 07, 08, 09]], # right_lane
    	"lanes_y":[01, 02, 03, 04, 05, 06, 07, 08, 09], 
    	"raw_file": "/daytime/20180429131040/000000.jpg"}
	},
	{"label": "000001.json", 
	"data": {
		"lanes_x": 
        [[01, 02, 03, 04, 05, 06, 07, 08, 09], 
        [01, 02, 03, 04, 05, 06, 07, 08, 09]], 
    	"lanes_y": [01, 02, 03, 04, 05, 06, 07, 08, 09], 
    	"raw_file": "/daytime/20180429131040/000004.jpg"}
	}
]
"""

