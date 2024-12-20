# 需要下载 zhipullm.py, zhipuai_embedding.py
from zhipuai_llm import ZhipuAILLM


from dotenv import find_dotenv, load_dotenv
import os

_ = load_dotenv(find_dotenv())

api_key = os.environ["ZHIPUAI_API_KEY"]

zhipuai_model = ZhipuAILLM(
    model="glm-4", temperature=0.8, api_key=api_key
)  # model="glm-4-0520",

# api test
# print(zhipuai_model("你好，请你自我介绍一下！"))

topics = [
    "自由",
    "平等",
    "正义",
    "权利",
    "责任",
    "道德",
    "教育",
    "环境",
    "科技",
    "经济",
    "文化",
    "社会",
    "法律",
    "政府",
    "民主",
    "专制",
    "人权",
    "移民",
    "战争",
    "和平",
    "暴力",
    "犯罪",
    "惩罚",
    "监控",
    "隐私",
    "言论自由",
    "宗教",
    "信仰",
    "性别",
    "种族",
    "性取向",
    "健康",
    "医疗",
    "福利",
    "贫富差距",
    "全球化",
    "气候变化",
    "可持续发展",
    "资源分配",
    "贸易",
    "市场",
    "资本主义",
    "社会主义",
    "民族主义",
    "国际关系",
    "外交",
    "恐怖主义",
    "网络安全",
    "人工智能",
    "生物伦理",
    "基因编辑",
    "动物权利",
    "食品安全",
    "消费主义",
    "广告",
    "媒体",
    "舆论",
    "公共政策",
    "社会福利",
    "教育公平",
    "职业道德",
    "家庭",
    "婚姻",
    "离婚",
    "抚养权",
    "青少年",
    "老龄化",
    "失业",
    "劳动权利",
    "工会",
    "环境保护",
    "可再生能源",
    "水资源",
    "空气污染",
    "垃圾处理",
    "生态系统",
    "生物多样性",
    "文化遗产",
    "艺术",
    "体育",
    "娱乐",
    "科技伦理",
    "网络隐私",
    "虚拟现实",
    "社交媒体",
    "心理健康",
    "成瘾",
    "自杀",
    "家庭暴力",
    "性骚扰",
    "职场歧视",
    "教育改革",
    "课程设置",
    "考试制度",
    "学费",
    "学生贷款",
    "科研",
    "创新",
    "创业",
    "投资",
    "金融危机",
    "债务",
    "税收",
    "公共交通",
    "城市化",
    "乡村发展",
    "基础设施",
    "住房",
    "房地产",
    "社会运动",
    "志愿服务",
    "慈善",
    "人道主义",
    "国际援助",
]


import json

json_path = "datasets/debate_socrates.json"
with open(json_path, "r+") as file:
    json_data = file.read()
    data = json.loads(json_data)

for topic in topics[:10]:
    prompt = f"""  
    我正在搜集苏格拉底风格的问答数据  
    请你参照案例，自行选择多样的主题，主题可以包括但不限于人生、哲学、社会、经济、科学等，生成一段问答，并格式化为案例的格式，
    注意，仅返回你生成的格式相同的json，尤其注意，回答不包含其他内容，不要包含代码块前后缀等符号  
    主题不要是人工智能
    本次主题是{topic}
    案例：  
    {{  
        "instruction": "中国就应该向西方学习，学习他们的言论自由。",  
        "output": "你认为中国应该向西方学习言论自由的做法，这样的看法很有意思。然而，让我们先明确一些问题。什么是“言论自由”？它在西方社会中是如何实施的？是否在所有情况下都能有效保护个人和社会的利益？你提到“应该学习”，这是否意味着你认为目前中国的言论自由水平存在问题？如果是这样，你认为这种问题的根源是什么？你认为完全照搬西方模式会不会带来一些意料之外的后果，比如对社会稳定和国家发展有负面影响？在探讨这个问题时，我们需要思考的是，不同文化和历史背景下的言论自由是否应当有不同的表达方式？如果我们真的要借鉴西方的经验，我们是否应该首先考虑如何在符合中国实际情况的前提下进行调整，而不是简单地复制？这些问题值得我们深入思考，以便在追求进步的同时，避免可能的冲突和不适应。"  
    }}
    {{
        "instruction": "我认为社会应该鼓励每个人追求个人兴趣，而不是仅仅为了经济利益而工作。",
        "output": "你提到社会应该鼓励每个人追求个人兴趣，这个观点是值得深思的。追求个人兴趣能带来幸福感和满足感，有助于个人的成长和创造力。然而，我们是否能仅靠个人兴趣来维持社会的经济发展？是否存在一种平衡，使得人们既能追求兴趣，又能在经济上维持稳定？我们如何在培养个人兴趣与满足社会需求之间找到平衡点？这些问题值得我们进一步探讨。"
    }}  
    """
    for _ in range(10):
        res = zhipuai_model(prompt)
        data["data"].append(json.loads(res))

with open("datasets/debate_socrates_full.json", "w", encoding="utf-8") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)
