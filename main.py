from context.Context import VideoParameter
from llm.llm_client import get_llm_client
from service.main_process import generate_video

text ="""
在美国，广纳式制度源自殖民时期弗吉尼亚、马里兰及卡罗莱纳的抗 争，后来又经美国宪法加强，辅之以制衡及分权。但宪法并不是广纳式制度发展的终点，和英国一样，以良性循环为基础的正面反馈过程，仍然不断在强化广纳式制度。
在美国，到了19世纪中叶，虽然不包括妇女及黑人，全部的白人男性都已经可以投票。经济制度愈来愈广纳，举例来说，1862年通过的公地放领法案就容许拓垦者占有新开辟的疆土，而不是把这些土地分配给政治菁英。但也和英国一样，广纳式制度所遭遇的挑战从来未曾停止过。美国内战结束，北方开启了飞跃的经济成长。随着铁路、工业及商业的扩展，颇有一些人发了大财。挟着经济成果的优势，这些人及他们拥有的公司愈来愈肆无忌惮，“流氓大亨”（Robber Barons）之名不胫而走。因为这些精明务实的生意人目标是巩固垄断局面，不让任何潜在的竞争者进入市场，或站在平等的地位做生意。其中最恶名昭彰的是范德比尔特
（Cornelius Vanderbilt），他就说过一句名言：“我干嘛在乎法律？权力难道不是在我的手里？”
另外一个是洛克菲勒（John D. Rockefeller），1870年成立标准石油公 司，很快就将克利夫兰的竞争对手排除，企图垄断运输、石油零售及石化产品。到1882年，他创造了一个垄断怪兽，用当时的话来说叫做托拉斯（trust）。到1890年，标准石油控制了88%在美国流通的汽油，1916年，洛克菲勒成为世界上第一个身价十亿美元的富翁。同时代的漫画把标准石油公司画成一只章鱼，紧紧抓着的不仅是石油工业，还包括美国的国会山庄。
几乎同样恶名昭彰的还有摩根（John Pierpont Morgan），他是摩根银行集团创始人，经过数十年的并购之后，最后成了摩根大通（J. P. Morgan Chase）。1901年，摩根与卡内基（Andrew Carnegie）成立了美国钢铁公司，是第一个资本价值超过十亿美元的公司，也是当时有史以来世界最大的钢铁公司。1890年代，几乎每个行业都开始出现大托拉斯，当中有许多都控制着该行业70%以上的市场，其中包括好几个家喻户晓的名字，譬如杜邦（Dupont）、柯达（Eastman Kodak）及国际收割机
（International Harvester）。就历史来说，美国，至少是北部及中西部的美国，拥有相对竞争的市场，而且比起该国其他部分，尤其是南部，要平等得多。但在这个时期，竞争让位给了垄断，财富的不平等迅速加大。
对于这种侵犯，美国的多元政治系统已经使社会的一大部分壮大，具备了对抗的能力。饱受流氓大亨垄断行为欺凌，或反对他们肆无忌惮独霸业界的人，开始组织起来，平民派（Populist）于此时出现，然后则是进步运动（Progressive movements）。
平民运动的出现，肇因于1860年代后期即已肆虐中西部的长期耕地危 机。全国农业保护协会，人称“种田佬”（Granger），成立于1867年，展开农民的动员，对抗不公不义的商业行为。1873年及1874年，种田佬控制了中西部十一个州的州议会，随着农村的不满达到高峰，1892年组成人民党，并在当年的总统大选中赢得8.5%的选票。接下来两届选举，平民派支持民主党候选人布莱恩，布莱恩将他们的议题纳入自己的政见，但两次均告失败。这时候，反对托拉斯扩散的草根力量已经组织起来，全力反制洛克菲勒及其他流氓大亨对国家政治的影响力。
渐渐的，这些政治运动发挥了效果，开始对政治态度乃至于立法产生影响，特别是对于政府在规范垄断上应该扮演的角色。1887年，第一项重要的立法州际商业法案通过，州际商业委员会成立，开始执行联邦对产业界的规范。紧接着，1890年通过谢尔曼反托拉斯法案（Sherman Antitrust Act），成为打击流氓大亨托拉斯的根本，至今仍是美国反托拉斯的主力规范。而连续数任总统，包括罗斯福（Theodore Roosevelt，绰号泰迪“Teddy”，1901年至1909年在任）、塔夫脱（William Taft， 1909年至1913年在任）及威尔逊（Woodrow Wilson，1913年至1921年在任），也都承诺改革并遏止流氓大亨坐大，选后都大力展开反托拉斯行动。

反托拉斯背后的关键力量及推动联邦规范业界的动能，主要还是农村的选票。1870年代早期，各州分别对铁路所做的规范就是来自农民团体。事实上，谢尔曼法案实施前，五十九件送进国会有关托拉斯的陈情案，几乎全都来自农业州，推广的工作也都是农民同盟、农民联盟、农民互助协会及牧业保护协会这类团体。农民在反对产业界的垄断中找到了共同的利益。
平民派倾全力支持民主党后，本身实力大幅衰落，残余分子另组进步 派，继续推动许多相关议题的改革。刚开始，进步运动以泰迪•罗斯福为核心。泰迪是麦金利的副总统，并在麦金利遭刺身亡后接任总统，时在1901年。跻身中央之前，罗斯福曾任纽约州长，作风强硬，扫除贪腐与“机器政治”*不遗余力。在首次国会演讲中，他把注意力转移到托拉斯上，强调美国的富裕是立基于市场经济及商人的灵活，但同时，

“期间不乏邪恶之辈……而且美国人民的心中都相信，以托拉斯闻名的大公司，就其特质与倾向来说，皆有害于全民福祉。这并非出自嫉妒或恶意，也不是不以大产业的成就为荣，无视于他们为国家之商业力量领先诸国所付出的努力，更不是因为无知而不晓得有必要以新方法迎合不断变化的贸易形势，也不是明知世界的进步有赖大事业的成就，而故意忽视集结资本乃努力完成大事业之必不可少。所有这一切只是因为深 信，集结与集中不是该予以禁止，而是应该置于理性控制的监督之下，且依我个人的判断，此一信念乃是正确的。”
加下去，他说道：“凡为追求社会更为美好者，都应该消弭商界巧取豪夺之恶，一如整个国家之消弭暴力之恶。”他的结论是：

“为了全民之利益，政府的力量固然不宜介入，但也应该运用监督的力量规范所有从事州际业务的公司，特别是那些在生意上以垄断手段或倾向而致富的公司。”


罗斯福建议国会设立一个联邦机构，赋予其调查大公司业务的权力，必要时不惜通过宪法修正案，借以成立此一单位。1902年，罗斯福动用谢尔曼法案解散北方证券公司，影响到摩根大通的利益，接下来又对杜 邦、美国烟草公司及标准石油公司提出诉讼。1906年，罗斯福以海普伯恩法案增强州际商业法案，以此提升州际商业委员会的权力，特别准许其检查铁路的财务账目，并将其权力扩张到其他领域。继罗斯福出任总统的塔夫脱对托拉斯的整治更不留情，并以1911年解散标准石油公司达到高峰。塔夫脱同时也推动其他重大改革，例如联邦所得税的实施就是 1913年宪法第十六修正案批准的结果。

随着威尔逊在1912年当选，进步运动的改革达到高峰。威尔逊在他1913年出版的《新自由》中写道：“如果垄断继续存在，政府将为垄断所宰制。我可不希望看到垄断依然故我。这个国家里面，如果有人真的大到足以拥有美国政府，他们迟早会将之占为己有。”
1914年，威尔斯促成了克莱顿法案的通过，并成立联邦贸易委员会落实这项法律。此外，在路易斯安那州众议员普乔领导下，普乔委员会
对“金融托拉斯”展开调查，威尔逊乃趁势加强了对金融界的规范，1913年成立联邦储备委员会，负责规范金融业的垄断活动。
如本书第三章所见，19世纪末、20世纪初，流氓大亨及托拉斯之兴起充分说明一项事实：市场本身并不保证会有广纳式制度。市场可以被少数几家公司宰制，索取过高的价格，阻挡更有竞争力的对手及新的技术进入。在他们的摆布之下，市场将不再广纳，只会愈来愈成为经济与政治霸权的囊中之物。广纳式经济制度需要的不只是市场而已，更需要的是能为大多数人创造公平竞争环境及经济机会的广纳式市场。在菁英阶层的政治权力支持下，无孔不入的垄断与此完全背道而驰。但对垄断托拉斯采取的反制也说明了一个现象，那就是，只要政治制度是广纳的，对于偏离广纳式市场的经济行为，政治制度会产生反作用力。这就是良性循环在发挥作用。广纳式经济制度可以为广纳式政治制度的繁荣打下基础，但经济活动偏离广纳式经济制度时，广纳式政治制度又会反过来发挥约束的效果。在美国，托拉斯遭到了遏阻，对照墨西哥的情况，便充分说明了良性循环的作用。在墨西哥，政府体制无能约束电信巨子谢林的垄断，但在美国，谢尔曼及克莱顿法却在上个世纪反复发挥效果，严加管束托拉斯、垄断及卡特尔，确保市场的持续广纳。
20世纪上半叶的美国经验，同时也凸显了自由媒体在壮大社会大众及促进良性循环上所扮演的角色。1906年，罗斯福取材自班扬的《天路历 程》中一个“喜欢揭人丑事”（muckrake）的角色，创造了“扒粪
客”（muckraker）一词，用来形容他口中那种侵略性强的新闻记者。这个词就此流传了下来，同时也象征新闻记者虽然无孔不入但也有效揭发了流氓大亨的过分行径，以及地方与联邦政客的腐败。最有名的扒粪客当推塔贝尔（Ida Tarbell），1904年出版的《标准石油公司史》使他成为舆论反对洛克菲勒及其公司利益的关键角色，最后导致标准石油公司在1911年解体。另一个重要的扒粪客是律师兼作家布兰迪斯（Louis Brandeis），后来被威尔逊总统提名为最高法院大法官。在《银行家怎么用别人的钱》一书中，他铺陈了一系列的金融丑闻，影响普乔委员会至深。此外，报业巨头赫斯特（William Randolph Hearst）扮演的扒粪客角色也相当突出。在他办的《大都会》杂志中，1906年发表了一系列由菲利普（David Graham Phillips）执笔的文章，名为“参议院的背叛”，提升了推动参议院直选的声势，促成1913年美国宪法第十七修正案的通过，是为进步运动另一次重要的改革。
政治人物采取行动反对托拉斯，扒粪客扮演了重要的角色。对流氓大亨而言，扒粪客犹如眼中钉肉中刺，但美国的政治制度却使他们无法将这些人拔除或噤声。广纳式政治制度容许自由的媒体繁荣发展，但回过头来，自由的媒体也比较能够让有害于广纳式制度的威胁曝光并广为人 知，促使社会对之采取抗拒行动。相对地，在榨取式政治制度、专制政权或独裁统治下，这类的自由根本就不可能，因为它们动辄压制反对力量的形成。自由媒体所提供的信息在20世纪上半叶的美国显然关系重大。如果没有这类信息，流氓大亨的肆无忌惮及胡作非为，美国老百姓将无从知道，也就无法动员起来反对托拉斯了。


"""

params = VideoParameter(content=text,
                        # qr_url="https://north-path.it-t.xyz",
                        # icon_path="resources/icon/android-chrome-192x192.png"
                        background_music="resources/background_music/Drone in D.mp3"
                        )

generate_video(params)

