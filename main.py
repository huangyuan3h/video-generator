from llm.llm_client import get_llm_client
from prompts.get_keywords import get_keywords
from prompts.translator import translator
from service.main_process import generate_video
from video.pexels import search_video_by_keyword

# generate_video()


# ['Quebec Immigration', 'PEQ', 'Canadian Immigration', 'Quebec French', 'Immigration Reform']


# response = search_video_by_keyword("Quebec Immigration")
#
# print(response)


text_content = """
2019年被称为魁北克移民政策的“转折之年”，这一年魁北克政府对移民政策进行了大刀阔斧的改革，尤其是针对PEQ快速移民项目的调整，让人印象深刻。

首先在2019年2月，魁北克政府宣布取消18000份技术移民申请，这些申请早在2016年提交，申请者等待了长达三年，但最终被拒之门外。这一决策让人感叹，低成本、低门槛的移民加拿大时代似乎已成过去。

然而这仅是开始。同年11月1日，魁北克政府对PEQ项目再次进行了改革。这次“14日变法”虽然最终以失败告终，但影响深远。这一系列调整究竟带来了哪些变化？

首先，PEQ的申请条件大幅提高，包括申请者需具备学士学位，法语水平门槛更高，对许多非法语区的申请者来说挑战巨大。尽管工作经验要求有所缩短，但申请者必须在魁北克找到相关工作，这对于初来乍到的人来说并不容易。总体来看，2019年的PEQ改革无疑让魁北克移民的难度再次提升。

魁北克政府的移民政策为何会出现这样的转变？背后的原因其实是希望引进更多高素质、高技能的移民，以推动本地经济发展。与过去相比，魁北克政府如今更加重视移民的学历、技能和法语水平，以确保新移民能够顺利融入魁北克社会。

展望未来，魁北克政府的移民政策是否会进一步调整？虽然改革步伐可能会继续，但魁北克依然因其优质的生活条件和福利体系吸引着来自世界各地的移民。对于想要移民魁北克的朋友们来说，紧跟政策动态、不断提升自我能力，或许才是实现移民之梦的最佳路径。
"""

model = get_llm_client()

translated_content = translator(model, text_content, "English")

print(translated_content)

keywords = get_keywords(model, translated_content)

print(keywords)