# zhipuai_llm here isn't public
from zhipuai_llm import ZhipuAILLM


from dotenv import find_dotenv, load_dotenv
import os

# 读取本地/项目的环境变量。

# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。
_ = load_dotenv(find_dotenv())

# 获取环境变量 API_KEY
api_key = os.environ["ZHIPUAI_API_KEY"]  # 填写控制台中获取的 APIKey 信息

zhipuai_model = ZhipuAILLM(
    model="glm-4", temperature=0.1, api_key=api_key
)  # model="glm-4-0520",

print(zhipuai_model("你好，请你自我介绍一下！"))
