from context.Context import VideoParameter
from service.main_process import generate_video

text = """
本书讨论的主题是世界上的富裕国家如美国、英国和德国，以及贫穷国家如下撒哈拉非洲、中美洲和南亚的国家，在所得和生活水准上的悬殊差距。
在我们写这篇序言时，北非和中东正经历“阿拉伯之春”（Arab Spring）的震撼，这场运动始于2010年12月17日，一名叫博阿齐齐（Mohamed Bouazizi）的街头小贩自焚激起大众的愤怒，进而点燃所谓的茉莉花革命（Jasmine Revolution）。

序言后，巴林、利比亚、叙利亚和也门政权的命途已岌岌不保。
这些国家内部不满的根源在于贫穷。埃及人平均所得水准只有美国人的 12%左右，预期寿命则少十年；20%的埃及人口生活在赤贫中。虽然这些差异很显著，但比起美国和世界上最贫穷的国家如北韩、塞拉利昂和津巴布韦还算小，因为后面这些国家生活在贫困中的人口远超过半数。
为什么埃及比美国贫穷这么多？有哪些限制因素使埃及人无法变富裕？埃及的贫穷是无法改变的呢，或者它的贫穷可以根除？开始思考这个问题有一个顺理成章的方法是，听埃及人自己谈论他们面对的问题，以及为什么他们挺身反对穆巴拉克政权。二十四岁的哈梅德是开罗一家广告代理商的员工，她在开罗的解放广场（Tahrir Square）示威时清楚地表达她的观点：“我们受到贪腐、压迫和劣质教育的荼毒。我们生活在一个必须改变的腐化体系中。”广场另一位示威者、二十岁的夏米是一名药学系学生，他表达相同的看法说：“我希望到今年底时我们能有一个民选政府，公民自由获得保障，而且我们能终结掌控这个国家的贪
渎。”解放广场的抗议者异口同声谴责政府的腐化、无能提供公共服
务，以及国内缺乏机会平等。他们尤其控诉压迫和缺乏政治权利。正如国际原子能总署前署长巴拉迪（Mohamed El Baradei）2011年1月13日在推特（Twitter）上写的：“突尼斯：压迫+缺乏社会正义+封杀和平改革渠道=定时炸弹。”埃及人和突尼斯人都认为他们的经济问题根源是缺乏政治权利。当抗议者开始更有系统地表述他们的要求时，埃及抗议运动领袖之一、软件工程师兼部落客哈利勒（Wael Khalil）张贴了第一份十二项立即要求，全部集中在政治改革上。提高最低薪资之类的议题只出现在中程要求当中，留待稍后实施。
对埃及人来说，导致他们落后的原因包括一个无能且贪腐的政府，一个让他们无法发挥才能、雄心和原创性的社会，以及他们所得到的教育。但是，他们也知道，这些问题的根源是政治。所有他们面对的经济阻 碍，来自于政治权力在埃及由少数菁英行使与垄断的方式。他们了解，这是他们首先要改变的事。
然而，解放广场上的抗议者对这个议题的看法，却与主流思想明显背 离。当辩论为什么埃及这样的国家如此贫穷时，大多数学者与评论家都强调完全不同的因素。有些人强调埃及的贫穷主要由地理条件所决定，因为这个国家大部分是沙漠，且缺乏足够的降雨，土壤和气候不适于高生产力的农业。其他人则指出，埃及人的文化特质不利于经济发展和繁荣富裕。他们说，埃及人缺乏让其他国家繁荣兴盛的工作伦理和文化特

质，而且还接受与经济成功相冲突的伊斯兰信仰。第三种看法在经济学家和政策专家当中是主流意见，这种看法认为埃及统治者根本不知道该做什么来促使他们国家繁荣起来，并且在过去一直采用不正确的政策和策略。这种看法也认为，如果这些统治者能接受正确的顾问提供的正确咨询，富裕兴盛将随之而来。对这些学者专家来说，统治埃及的少数菁英只顾自己利益、牺牲社会福祉的事实，似乎与了解这个国家的经济问题毫不相干。
在本书，我们将论述解放广场上的埃及人的看法才是正确的，而不是大多数学者和评论家的看法。事实上，埃及之所以贫穷就是因为它被一小群菁英统治，他们以图利自己的方式组织社会，牺牲了大多数人的利 益。政治权力集中在少数人手中，用来为掌权者制造庞大的财富，例如前总统穆巴拉克显然累积了七百亿美元财富。输家是埃及人民，而且他们有切身之痛。
我们将阐明，对埃及贫穷的这种诠释（也就是人民的看法），也对“为什么穷国会贫穷”提供了一种普遍的解释。不管是在北韩、塞拉利昂或津巴布韦，我们将说明穷国为什么贫穷的原因就和埃及一样。英国和美国之类的国家变富裕，是因为它们的人民推翻掌控权力的菁英，创造了一个政治权利更广泛分配的社会，在这样的社会中，政府需要回应人民并对人民负责，而且广大民众都能够利用经济机会。我们将说明，要了解今日世界何以有这种不平等，就必须深入过去，研究各个社会的历史演进。我们将发现，英国之所以比埃及富裕，是因为英国（精确地说是英格兰）在1688年发生一场革命，促成了该国的政治转型以及伴随的经济转型。人民争取并赢得更多政治权利，而且利用这些权利来扩大自身的经济机会。其结果是一个完全不同的政治与经济演进轨迹，并在工业革命达到高潮。
工业革命及其解放的科技发展并未扩散到埃及，因为该国当时在鄂图曼帝国（Ottoman Empire）掌控下，受到的待遇和后世穆巴拉克家族的对待相去不远。鄂图曼在埃及的统治于1798年被拿破仑推翻，但该国随后又落入英国殖民主义者的掌控，他们对促进埃及的富裕繁荣和鄂图曼人一样毫无兴趣。虽然埃及人终于摆脱鄂图曼帝国和大英帝国、并在1952年推翻君主政体，但这种改变与1688年英国的革命不同；埃及政治并未从根本上转型，只是把权力交给另一批菁英，而他们对于为埃及人民创造富裕的漠不关心也与鄂图曼和英国如出一辙。结果是，社会的基本结构并未改变，埃及也依然贫穷如故。

本书将探究长期以来这些模式如何自我复制，以及为什么有时候它们会改变，就像1688年英国发生的事件，和1789年的法国大革命。这将协助我们了解今日埃及的情况是否已经改变，以及推翻穆巴拉克的革命会不会带来一套能够带给一般埃及人民富裕的新制度。埃及过去曾发生过未带来改变的革命，因为发动革命的人只是接管被罢黜者的统治，重新建立类似的体系。一般人民确实难以获得真正的政治权利，并改变社会的运作方式。但真正的改变仍然可能发生，而我们看到它在英国、法国和美国，以及日本、博茨瓦纳和巴西等国家如何发生。基本上贫穷的社会想变富裕，需要的就是政治转型。有证据显示埃及可能正在发生这种转型。另一位解放广场的抗议者迈特瓦利说：“现在你看到穆斯林和基督徒站在一起，你也看到老年人和年轻人同心协力，他们都想要相同的东西。”我们将看到社会中这种广泛的运动就是这类政治转型发生的关
键。如果我们了解这类转型发生的时机和原因，我们将更有能力评估哪
些运动就像过去那样将以失败收场，以及哪些运动我们可以期待将获得成功，并改善数百万人的生活。


"""

params = VideoParameter(content=text,
                        # qr_url="https://north-path.it-t.xyz",
                        # icon_path="resources/icon/android-chrome-192x192.png"
                        background_music="resources/background_music/Undercover Vampire.mp3"
                        )

generate_video(params)
