from context.Context import VideoParameter
from llm.llm_client import get_llm_client
from service.main_process import generate_video

text ="""
现代的早期，东南亚本来大有机会迎接一个经济扩张及制度改变的新时代，但欧洲海军及商业力量的扩散却活生生将之截断。就在荷兰东印度公司进行扩张的同时，另一种迥然不同的贸易则在非洲如火如荼地进行，那就是奴隶贸易。
在美国，一说到南方的奴隶制度，往往都说是“特殊制度”。但从历史的角度观察，诚如大古典学家芬雷所言，奴隶制度绝非特例，几乎在每个社会都曾出现过。本书早先也曾指出，这在古罗马及非洲都是地方性的传统，或者长期以来更是欧洲的奴隶来源，只不过并非唯一来源。
古罗马时期，奴隶都是斯拉夫人（Slavic people），来自黑海四周、中东，也有来自北欧。但到1400年代，欧洲人不再奴役自己人。至于非 洲，如本书第六章所言，并未像中世纪欧洲那样从奴隶制度转变成农奴制度。现代时期来临之前，东非奴隶贸易活络，有大量奴隶越过撒哈拉运往阿拉伯半岛。此外，西非大国马里、加纳及桑海，中世纪时就已经在政府、军队及农业上大量使用奴隶，它们和北非穆斯林国家从事奴隶贸易，同时也采用它们的组织形态。
17世纪初期，加勒比海地区殖民地的糖业种植不仅导致国际间的奴隶贸易量剧增，同时也使奴隶在非洲内部受到前所未有的重视。16世纪时，大西洋的奴隶贸易为数约三十万名，多数来自中非洲，与刚果及葡萄牙人有着密切的关系，后者的根据地在偏南方的卢安达，先今安哥拉的首都。此一时期，横越撒哈拉的奴隶贸易量仍然庞大，北上为奴的非洲人为数约五十五万。到了17世纪，整个情况反转过来。在大西洋贸易中，出售为奴的非洲人多达一百三十五万，绝大多数都是用船送往美洲。至于撒哈拉的交易数量，大体上没有什么改变。18世纪又有另一波的暴 增，乘船横渡大西洋的奴隶多达六百万，横越撒哈拉的奴隶则在七十万之上。如果把各个时期及非洲各地加总起来，从非洲大陆运送出去的奴隶，数量起码超过一千万。
用今天的国界标示，粗略估计 1400年至1900年间的累积人数，及其在1400年人口数中所占百分比。深暗色部分表示奴隶的密度较高，例如安哥拉、贝宁、加纳及多哥，累积输出的奴隶数量超过该国1400年总人口数。
欧洲人突然出现在西非海岸及中非，迫不及待地收购奴隶，对非洲的改变自有其重大影响。大部分要用船运到美国的奴隶都是战俘，且立刻就送往海岸。枪支弹药的大量进口刺激了战争的增加，欧洲人便是拿这些东西来交换奴隶。1730年代，沿着西非海岸，每年进口枪支约十八万，到了1750年及19世纪初年间，单单英国，一年所卖的枪支就在二十八万三千至三十九万四千之间。1750年至1807年间，英国另外还卖了二万二千吨的火药，平均每年约三十八万四千公斤，外加每年九万一千公斤的铅。更往南边去，交易也同样火热。在刚果北部的卢安果沿海，欧洲人一年卖出五万枝枪。
所有这些战争不仅造成生命的丧失及人生的苦难，同时也推动非洲在制度发展上走出一条另类的道路。现代时期萌发之前，相较于欧洲及亚 洲，非洲社会在政治上极少中央集权，大部分政体都是小格局，由部落酋长或所谓的国王控制土地及资源。许多地方，如本书提到过的索马里，政治上根本没有层级分明的权力结构。在政治上，奴隶买卖启动了两种有害的进程。其一，许多原本就比较专制的政权，奴役别人并将之
卖给欧洲的奴隶主变成了国家的唯一目标。其二是因此产生的结果，但却很矛盾：为对抗第一种进程，到头来，战争与奴役却彻底摧毁了下撒哈拉非洲国家的秩序与法治权威。战争之外，奴隶也有绑架得来的，甚至连法律都变成了取得奴隶的工具。无论是犯的是什么罪，刑罚都可以将之打为奴隶。1730年代，在非洲西岸的塞内甘比亚，英国商人摩尔就注意到了这种情形：“自从奴隶买卖派上用场，所有的处罚就都变成了奴隶制度的一环；这种刑罚有个好处，他们打击犯罪从此不遗余力，因为罪犯可以卖为奴 隶，有利可图，而且不只是杀人、盗窃、通奸会被处以卖为奴隶之罪，连小案子也照样处以同罪。”为了抓捕并贩卖奴隶，甚至连宗教制度都遭到扭曲。尼日利亚东部的埃罗恰夸神谕就是一例。当地三个主要族群，伊乔族、伊毕比欧族和伊格波族都相信，神谕是一位普受敬仰的地方神祗的发言，请神谕的目的则是要排难解纷。前往埃罗恰夸请神谕的人，必须从镇里下到克罗斯河的一个峡谷，进入一个高大的洞穴，神谕就放在里面，洞穴前则排列着人的骷髅。分配神谕的祭师和埃罗恰夸的奴隶主及商人勾结，这中间大有文章，经常发生有人被神谕给“吞掉”的事，说穿了，其实是请神谕的人穿过洞穴之后，就被带到克罗斯河，而欧洲人的船早已等在那儿。整件事情里面，法律和风俗都遭到滥用及破坏，成了抓捕奴隶的帮凶，这样的事情对于政治集权化具有致命的效应，虽然在某些地方确实促成了强势政府的兴起，但其存在的目的竟然就只是掠夺与奴役。刚果王国是第一个质变为奴隶国家的非洲国家，后来终因内战而覆亡。其他奴隶国家主要集中在西非，包括今天尼日利亚境内的奥约、贝宁境内的达荷美，以及后来加纳境内的艾森地。
举例来说，17世纪中叶奥约国的扩张，就和沿海奴隶输出的增加有着直接关系。至于国力的强盛则是军事改革的结果，其中包括从北方输入马匹，组成强大骑兵，能够彻底歼灭反对势力。奥约向南方海岸扩张之 际，遭到其他政治体的干预，奥约一一予以击败，并将其人民出售为奴。1690年至1740年这段期间，奥约一手垄断了号称奴隶海岸的贸易。据估计，在此一海岸卖出去的奴隶，征战所俘者占约八至九成。战争与奴隶供应之间存在着显著的关系，另外一个例子则发生在东非（似应为西北非），亦即现今加纳境内的黄金海岸。1700年之后，艾森地从内陆向外扩张，其模式与之前的奥约如出一辙。18世纪前半叶，扩张引发了史称的艾肯战争，艾森地各个击破，并于1747年征服最后一个国家伽 门。1700年至1750年间从黄金海岸出售的奴隶约三十五万七千人，其中多数是战俘。
这种大规模的人口抽离，影响最大的可能就属人口统计。现代时期之 前，非洲人口到底有多少，根本无从知道，倒是奴隶贸易对人口的冲击，不少学者所做的估计却相当值得参考。历史学家曼宁估计，18世纪初，供应奴隶输出的非洲西部及中西部，人口数约在二千二百万至二千五百万之间。但按照保守的假设，18世纪与19世纪初期这段期间，如果没有奴隶贸易的话，以这些地区人口成长一年约为0.5%计，曼宁估计，到1850年，这一区域的人口数至少应为四千六百万至五千三百万。但事实上，却只有一半的数目。
为何会出现这样巨大的差异，1700年至1850年之间，从此一区域输出的奴隶多达八百万人固然是原因之一，但为了抓捕奴隶，征战连年，死亡数以百万计也难辞其咎。此外，奴隶制度与奴隶贸易进一步破坏了家庭与婚姻，或许也降低了生育率。
18世纪末叶，废止奴隶贸易的运动兴起，并在领袖魅力十足的威伯佛斯领导下，开始在英国获得动力。经过多次失败，1807年，废止派终于说服国会，通过法案，将奴隶贸易列为非法。次年，美国继踵其后。但英国政府推行得更彻底，为积极推动此一禁令，在大西洋上部署海军舰 队，企图彻底扫除奴隶贸易。所有这些措施真正见到效果却花了相当长的时间，直到1834年，奴隶身份才在大英帝国境内绝迹，当时奴隶贸易的最大一部分——大西洋奴隶贸易——总算走到了日暮穷途。
1807年后，奴隶贸易告终虽然减少了外界对非洲奴隶的需求，但这并不表示奴隶制度对非洲社会及制度的影响也就此跟着消失。许多国家的组成都是以奴隶为中心，就算英国终结了这方面的交易，但却没改变此一现实。尤其重要的是，奴隶制度在非洲已经根深蒂固。所有这些因素加起来，也就形成了非洲发展的道路，1807年之前如此，其后亦然。
奴隶制度之后，取而代之的是一个新词：“合法生意”，指的是一切从非洲出口但无关于奴隶贸易的新商品。所有这些新货品包括棕榈油、果 仁、花生、象牙、橡胶及阿拉伯树胶。欧洲人及北美洲人的收入因工业革命的推动而成长，对于这类热带产品的需求也随之急剧升高。非洲人一如当年卯足了劲利用奴隶贸易带来的商机，对于这些合法生意，他们也一头栽入。但他们利用这波新商机的方式有一个特殊的背景：奴隶的存在早已司空见惯，但外界对奴隶的需求却突然消失。奴隶既然不能再卖给欧洲人，他们又能做什么呢？答案很简单：可以强制他们在非洲工作，生产合法生意的新产品，利润好得很。
有记录可稽的最佳例子之一在艾森地，亦即今天的加纳。1807年之前，艾森地帝国大搞抓奴卖奴的勾当，将人带到海岸，卖给设在凯普海岸及艾尔米纳的奴隶堡。1807年之后，这行业眼看没了搞头，艾森地的政治菁英阶层在经济上便另起炉灶。但不管怎么说，奴役与奴隶制度根本没有结束。相反的，奴隶全都给圈进了大型农庄，刚开始只在首都库玛西周围，后来又扩张到整个帝国，受雇生产出口用的黄金及可乐果，但也种植大量的粮食，并从事密集的搬运工作，因为艾森地根本不使用轮子运输。同样的变通也发生在更往东的地方。举例来说，达荷美国王在怀达及波多诺伏的港岸地区拥有大片棕榈园，用的就全是奴工。
因此，奴隶贸易的废止并没有使奴隶制度在非洲销声匿迹，充其量只是把奴隶换了个地方使用，以前是用在美洲，如今则是用在非洲境内。尤其重要的是，过去两个世纪为因应奴隶贸易所形成的政治制度并没有改变，因此其行为模式依然。举例来说，在尼日利亚，1820至30年代一度强大的奥约王国之所以崩溃，除了内战的关系，还因为南边的约鲁巴人的城邦兴起，诸如伊洛林及伊巴丹，这些都是直接涉入奴隶贸易的国 家。1830年代，奥约饱受劫掠，之后，约鲁巴诸城又与达荷美角逐该地区的支配权，整个19世纪的前半叶，战火连绵，制造了无数奴隶。除此之外，日常生活中，绑架有之，神谕的诅咒有之，小规模的打家劫舍也照样发生。在尼日利亚某些地方，绑架严重到父母不准孩子到外面游戏，唯恐子女就此沦落成为奴隶。
其结果是，整个19世纪，在非洲大肆扩张的并不是商业合同而是奴隶制度。精确的数字尽管不易取得，根据当时许多旅行者及商人现存的记 述，西非的艾森地王国及达荷美王国，以及约巴鲁诸城邦，奴隶人数都超过人口的半数。比较精确的资料则存在于早期法国殖民地的记录中，其中包括西苏丹，以及西非一大片带状地带，从塞内加尔经马里、吉布纳法索到尼日尔及乍得。到1900年，在这一区域，奴隶仍占全部人口的 30%。
对于消灭非洲的奴隶制度，合法生意的出现固然无能为力，同样的，列强瓜分非洲之后的殖民统治照样无济于事。欧洲人入主非洲，尽管正气凛然，摆出一副对抗并废止奴隶制度的架势，但现实情况却非如此。殖民统治下的非洲，绝大部分地方，直至20世纪奴隶制度依然延续不绝。举例来说，塞拉利昂的奴隶就是直到1928年才完全根绝，尽管首都自由城在18世纪末叶建立之初，还被视为是美洲遣返奴隶的天堂，并成为英国反奴舰队的重要基地，也是奴隶被英国海军从奴隶船上解救下来，重获自由后的新家。尽管具有这样的象征意义，奴隶制度在塞拉利昂还是延续长达一百三十年之久。1840年代，就在塞拉利昂的南边，同样也是为美洲重获自由的奴隶而成立的赖比瑞亚，情况亦复如此。甚至到了20世纪，奴隶制度仍然阴魂不散，迟至1960年代，据估计，劳动人口中仍有四分之一是强制性的，生活上与工作上的条件都无异于奴隶。由于经济与政治制度的建立都是以奴隶贸易为基础，是榨取式的，因此工业化也没有扩及到下撒哈拉非洲；相较于世界其他部分的经济正在转型，这一地区的经济不仅停滞不前甚至是倒退的。


"""

params = VideoParameter(content=text,
                        # qr_url="https://north-path.it-t.xyz",
                        # icon_path="resources/icon/android-chrome-192x192.png"
                        background_music="resources/background_music/Drone in D.mp3"
                        )

generate_video(params)

