 
 ------公共参数表，用于一些比较独立的参数，参数少独立建表浪费而存放的公共数据表
 local SystemConfig = {
	["buildbase"] = { x=250, y=610000, small=0.55 , mine=1, silver=1, gold =4, }, --资源消耗转魔晶
	["soldiers_time"] = { a=14, b=0.7,}, --士兵训练时间转魔晶(包括治疗、傀儡制造和修复)
	["technology_time"] = { a=14, b=0.7,}, --科技研究时间转魔晶
	["bulid_time"] = { a=14, b=0.7,}, --建筑升级/拆除时间转魔晶
	["herorank_time"] = { a=14, b=0.7,}, --英雄升品质时间转魔晶
	["herostar_time"] = { a=14, b=0.7,}, --英雄升品阶（军阶）时间转魔晶
	["treasure_time"] = { a=14, b=0.7,}, --锻造装备时间转魔晶
	["wall_time"] = { a=14, b=0.7,}, --修复城墙时间转魔晶
	["material_time"] = { a=14, b=0.7,}, --材料生产时间转魔晶
	["vipbox_time"] = { a=14, b=0.7,}, --VIP宝箱时间转魔晶
	["unionquest_time"] = { a=14, b=0.7,}, --联盟任务时间转魔晶
	["interquest_time"] = { a=14, b=0.7,}, --内政任务时间转魔晶
	["demolish_shop"] = { item_id=11000600, }, --建筑拆除道具
	["time_free"] = {  free=0,}, --基础免费时间
	["get_once_limit"] = { limit= 9999, storage_max=999999999 }, --单个物品单次获取上限,物品最大容量
	["sell_limit"] = { limit_num= 100 }, --出售的最大数量
	["compose_limit"] = { limit= 8888 }, --合成分解单次最大值
	["march_cancel"] = { normal_cancel = 14000700, aggregation_cancel = 14000800,}, --行军召回、集结召回道具
	["maxhp"] = { power = {24,0,0}, agile = {16,0,0}, intelligence ={16,0,0},} , --最大生命值转化三个类型英雄的力敏智，下同
	["phy"] = { power = {0.8,0.4,0}, agile = {0,1.4,0}, intelligence ={0,0.4,0},} , --物理攻击
	["magic"] = { power = {0,0,0.4}, agile = {0,0,0.4}, intelligence ={0,0,1.4},} , --魔法强度
	["phyShield"] = { power = {0.15,0.05,0}, agile = {0.1,0.05,0}, intelligence ={0.1,0.05,0},} , --物理护甲
	["magicDefense"] = { power = {0,0.05,0.1}, agile = {0,0.05,0.1}, intelligence ={0,0.05,0.1},} , --魔法抗性等级
	["crit"] = { power = {0,0,0}, agile = {0,0.1,0}, intelligence ={0,0,0},} , --物理暴击等级
	["penShield"] = { power = {0,0,0}, agile = {0,0,0}, intelligence ={0,0,0},} ,--物理穿透
	["magicDefenseIgnored"] = { power = {0,0,0}, agile = {0,0,0}, intelligence ={0,0,0.03},} ,--魔法穿透
	["phyCritDamage"] = 2,--物理暴击伤害倍率
	["magicCritDamage"] = 2,--魔法暴击伤害倍率
	["healCritDamage"] = 2,--治疗暴击伤害倍率
	["critValue"] = { a = 11, b=1.005 ,} , --暴击等级转化属性
	["dodge"] = { a = 5, b=1.005 ,} , --闪避等级转化属性
	["bloodTransferLv"] = { a = 4, b=1.01 ,} , --吸血等级转化属性
	["hit"]={a=5,b=1.005,},--命中等级转换属性系数
	["partPerMillion"]={"receiveHeal","healingSkilImprovement","powerExpendReduce","phyRelief","magicRelief","relief","phyDamage","magicDamage","damageIncrease","energyCoefficient","atkEnergyCoefficient"},--万分比属性
	["checkpoint"]={10716,10717,10718,20718},-----暂不开放的关卡id
	["movecityitem"] = { stochastic = 14000101, high = 14000104, new = 14000100, alliance = 14000103, cross = 14000105, } , --迁城道具:随机、高级、新手、联盟、跨服
	["heroexpitem"] = {{id=11004002,num=1500}, {id=11004001,num=300}, {id=11004000,num=60}, }, --英雄经验道具
	["burning_wall"] = {burning_time=1200, defValue_time=0.25, item_id=11004200, palace_smoke=300, palace_fire=300,  } , ---燃烧时间上限（秒），1秒恢复耐久点，灭火沙道具ID ,王宫冒烟时间，王宫冒火时间 
	["vip"] = {everyday_exp=0, max_day=30, continued_exp=20, up_day=0 } , ---每日登入基础经验，最大天数，连续登入每日经验，升级赋予激活时间（秒）
	["hide_soldier"] = { time1=3600, time2=14400, time3=28800, time4=43200 } ,---藏兵洞1小时，4小时，8小时，12小时  （单位都为秒）
	["Treasure_box"] = { first_box=12, limit_box=200 } , ---最初宝物格，宝物格上限
	["Treasure_quity"] = { quity_max=5 } , ---宝物最高品质
	["gam_special"] = { 23300100 , } , ---特殊宝石：只有一个合成按钮
	["decoration_box"] = { 1,17,30 } ,---铁匠铺1级开放1个饰品格；铁匠铺17级开放2个饰品格；铁匠铺30级开放3个饰品格；
	["lordskill_reset"] = {thingcfgid = 11000900 } ,---领主技能重置道具
	["lordskill_record"] = {thingcfgid = 11005800 } ,---领主技能记录道具
	["lord_info"] = { name_id=11000300, cost_name=100, image_id=11000400, cost_image=400,cd_time=1296000,lv=6, } , ---领主改名、领主改名花费魔晶、更换形象、更换形象花费魔晶,自定义头象上传冷却时间,自定义头像解锁需要的主城等级
	["alm_dungeons"] = { initial_num=0, } , ---精英副本初始挑战次数
	["strength"] = { id = 11003400, limit_storage=1000, everyday_num=0, initial=80, } , ---体力道具ID，存储上限，每日使用体力道具默认次数,体力初始值
	["action"] = { limit_action = 1500, max_action = 15000, initial=1000,  } , ---行动力初始恢复上限，行动力存储上限,行动力初始值
	["lord_skill"] = {id = 101 , lv = 10 , piece = 200 , vipLv=7 } , --城堡等级解锁领主天赋树，切换天赋树价格，vip等级限制
	["civilization"] = {rock_areaid=4,switch_id=11002500, switch_crystal=3000, switch_cd=3600, clear_cost=8000, rank_max=25, week_day=3, week_max=6000, buff_effect=3000,army_begin=4 } , ---文明系统解锁空地战役、切换文明道具ID、切换文明冷却时间（秒）、清除冷却时间花费魔晶、文明等级上限、行为声望重置日期、行为声望上限、未选择文明特效生效万分比、送兵开始等级中立+3
	["civ_item"] = {speed=6, acceleration=3, ues_max=24,} , --初速度、匀加速使用声望道具加速度、一秒钟使用道具数量上限值
	["civ_talk"] = {duration=5, interval=10,} , --弹框出现5S后自动消失，10S间隔出现；
	["civ_reward"] = {time_cd=259200, reward_item= {11002500,1,12000603,1,11002401,1,12000506,1}, } , ---创号等待倒计时、奖励物品；
	["civ_kill"] = {condition=100, value=1, } , ---杀敌战力条件，获得声望值；
	["treasure_order"] = { 1,2,3,4,5,6,6,6 } , ---武器、头盔、上装、下装、副手、饰品1、饰品2、饰品3
	["gem_broke"] = { id =11003505 } , ---宝石粉碎锤：使用后移除并丢弃宝石，且无法还原
	["initial_buff"] = {10030, 259200,70001,432000} ,--新手BUFF（初始保护罩ID,时间、精灵王庇护BUFFid，时间5天） 
	["initial_hero"] = {{cfgid = 101, slot = 62}, {cfgid = 301, slot = 0}, {cfgid = 501, slot = 0}} , --初始英雄：阿里巴巴 阿拉丁 辛巴达
	["shield_hero"] = {1,7,9} , --分享屏蔽英雄：阿里巴巴、杜娅扎德、麦尔加娜
	["lv_hero"] = {limit_hero_lv = 25},--英雄等级初始限制
	["initial_bag"] = {11000300,1,14000100,2,15000300,1,13000102,24,11002402,1,11002401,2,11001000,3,51101300,1,51100100,1,11001299,1,12000600,1,14000103,2} , --初始道具 改名卡*1,新手迁城*2,新手宝箱*1,通用加速5分钟*24,声望道具500*1,声望道具100*2,领主经验100*3,英雄经验60*1,邪眼护眼石白色*1,雪花石白色*1,VIP10点道具*1，精灵经验道具100*1，精灵技能点道具100*1，文明结晶100*1，联盟迁城*2
	["initial_currencyinfo"] = {1000,200,1006,50000,1007,50000,1008,50000,1009,50000,1010,10000,1100,200} , --魔晶200,粮食50000,木头50000,铁50000,银50000,金币10000,文明结晶200
	["initial_soldier"] = {20101,1500,20201,1500,20301,1500} ,--初始士兵：1500个步兵,1500个骑兵,1500个弓兵
	["genius"] = { collpoint = 20000, goldpoint = 5000, collexp = 1000, goldexp = 250, killpoint = 1000, killexp= 100 } , ---采集获得防御点数、采集金币获得防御点数、采集获得精灵经验、采集金币获得精灵经验、杀敌获得攻击点数、杀敌获得精灵经验
	["genius_limit"] = { exp_max = 5000000000, point_max = 300000000, Soul_max = 100000000 } , ---精灵经验上限、精灵攻击/防御点数上限、魂魄数量上限
	["Soul_first"] = { genType = 3, Soul_num = 100 } , ---对应精灵类型，初始赠送魂魄数量
    ["lock_genius"] = { cd= 31536000,}, -- 精灵解封时间（秒）
	["genskill"] = { one_reset = {11001800,1}, full_reset = {11001700,1}, one_star = {11002100,1}, full_star ={11002000,1} } , ---神兽单技能重置、神兽全技能重置、神兽技能升星单个重置、神兽技能升星全部重置
	["genius_max"] = { rank_max = 70, skill_max = 15, satr_max = 9, } , ---精灵的最大等级，精灵技能的最大等级，精灵技能的最大星级
	["genius_min"] = { rank_min = 1, skill_min = 1, satr_min = 0, } , ---精灵的初始等级，精灵技能的初始等级，精灵技能的初始星级
	["genius_run_cd"] = { max = 900, min = 60, } , ---飞翔间隔最大值s、飞翔间隔最小值s
	["mystery_shop"] = { resource_chance = {1001,15,1002,25,1003,25,1004,25,1005,10}, prop_star = {2,80,0.8,3,20,0.7} , refresh_time =10, probability=10000} , ---神秘商店价格类型随机，资源ID，概率、---道具档次随机,档次，概率，折扣,重置时间（秒），是否获得礼包资格（1-10000的随机值,1则为不随机,10%）
	["material_position"] = { position_number = 8 , initial_number = 2 , money_number = 6 , speed_number = 20, money_open = {100,300,1000,1500,2000,3000} } ,--材料工坊位置总数  初始开启位置数量， 魔晶开启位置数量，每次加速次上限 魔晶开启价格（第一个几个，第二个价格，第三个价格....）
    ["horn"] = { id = 11001100 } , --传声号角（喇叭）道具
	["rank"] = { group = 5, activity_time = 15, exploit_limit = 50000, } , --每组活动国家，---每次活动周期（天）---每个周期周获得的最大军功
	["alliance_flag"] = { max_BG = 10, max_face = 10, max_effect = 10, }, --联盟旗帜的底数量上限，面数量上限，特效数量上限
	["collection"] = {max = 100,num=30,} ,--收藏夹数量上限,收藏夹字符数限制
	["action_reset_time"] = { HH = 20, MM = 00, }, --行动力重置时间，阿拉伯当地晚上8点，即UTC17点
	["system_timezone"] = 0,--时区（uct）
	["arena"] = {max = 5,video_number = 20,vidio_time=1209600,scene = 10000,attack = {159,167,173,187,197} ,defense = {38,30,24,11,21},num = 100,max_rank_num=5000,opponent_num=3,pow_ratio=0.6,max_defendhero_num=5,refresh_reward_time=21600,reset_times_limit=20} ,--竞技场每日挑战次数,录像最大保存量，录像最大保存时间，场景ID，我方位置，敌方位置,排行榜最大显示数量，机器人数量，对手数量，次幂系数，防守阵容英雄数量，魔晶领取倒计时，每日魔晶购买挑战次数上限	
	["randomchest"] = {time = 300, num = 8 , refresh_time = 3600 ,cooling_time = 3600 ,chat_cd=15,chat_exist=5, } , --随机宝箱存在时间,最大刷新数,刷新时间,冷却时间,气泡框间隔的出现时间，气泡框存在时间
	["alliance_chat"] = {invite = "des_1211",accession = "des_2179",creat = "des_2180",kick = "des_2181",out = "des_2182",up_rank = "des_2183",down_rank = "des_2184",transfer = "des_2185",join = "des_2186", } ,--联盟邀请公告，入盟邀请，创建联盟，踢出联盟，退出联盟，成员升阶，成员降阶，转让盟主，加入联盟
	["hunting_speed"] = {num = 3300 ,} , --猎杀魔物行军速度
	["scoutprice_speed"] = {num = 10000 ,} , --侦查行军速度   个人出征所需时间(秒)=S*10000/(Y*100)    Y=(1800+S)/1100
	["reshelp_speed"] = {num = 1500 ,} , --资源援助行军速度	
    ["quest_number"] = {interior = 3 , union = 3, } , --内政任务初始数量、联盟任务初始数量
	["quest_draw"] = { Interval ={5000,9000}, drawcontrol={350,351,352,353,354}, } , --内政/联盟任务宝石/材料保底个数；白绿蓝紫橙对应奖池控制ID
	["quest_reset"] = {union_id = 11003200, reset_time = 21600 } , --联盟重置任务id、重置倒计时s
	["vip_quest"] = {wait_time = 3600 } , --领取等待时间s
	["allreward"] = {box_index = 301, deadline_time = 86400 } , -- 联盟活跃宝箱序列、过期时间s
	["alliancegift"] = {limit = 300 , init_level = 1 } , -- 联盟礼物列表上限、初始联盟礼物等级
    ["wish"] = {id = 11000500 , num = 200, limit_price = 200 , a = 5 ,b = 10 , c = 10, d = 20,}, --许愿石道具每日使用次数上限,每种资源每日前2次必出暴击5倍、10倍，每种资源必出5倍暴击次数，每种资源必出10倍暴击次数
	["buff_battle"] = {buff={129,500},fanaticismbuff = 20001, guardiansbuff = 10029, new_guardiansbuff = 10030},--战争狂热加成ID和加成值，战争狂热buffID,战争守护buffID
	["buff_food"] = {buffid = 10019, bufftime = 86400, price = 3, itemid = 12000900,bufftype = 19,capacityAttr=214,bid=201,addid = 203,reduceid = 232,buildcostred = 239,techcostreduce = 247, }, --农田建筑强化buffID（buff表ID），时间，基础价格,强化道具ID,BUFF表类型,容量加成ID，添加建筑ID，产量加成ID,产量降低BUFF,建造粮食消耗加成ID，科研粮食消耗加成ID
	["buff_wood"] = {buffid = 10017, bufftime = 86400, price = 3, itemid = 12000800,bufftype = 18,capacityAttr=215,bid=202,addid = 204,reduceid = 233,buildcostred = 240,techcostreduce = 248}, --伐木场建筑强化buffID（buff表ID），时间，基础价格,强化道具ID,BUFF表类型,容量加成ID，添加建筑ID，产量加成ID,产量降低BUFF,建造木材消耗加成ID，科研木材消耗加成ID
	["buff_iron"] = {buffid = 10021, bufftime = 86400, price = 3, itemid = 12001000, bufftype = 20,capacityAttr=216,bid=203,addid = 205,reduceid = 234,buildcostred = 241,techcostreduce = 249}, --铁矿场建筑强化buffID（buff表ID），时间，基础价格,强化道具ID,BUFF表类型,容量加成ID，添加建筑ID，产量加成ID,产量降低BUFF，建造铁消耗加成ID，科研铁消耗加成ID
	["buff_silver"] = {buffid = 10023, bufftime = 86400, price = 3, itemid = 12001100,bufftype = 21,capacityAttr=217,bid=204,addid = 206,reduceid = 235,buildcostred = 242,techcostreduce = 250}, --白银建筑强化buffID（buff表ID），时间，基础价格,强化道具ID,BUFF表类型,容量加成ID，添加建筑ID，产量加成ID,产量降低BUFF，建造白银消耗加成ID，科研白银消耗加成ID
	["buff_gold"] = {buffid = 10025, bufftime = 86400, price = 6, itemid = 12001200,bufftype = 22,capacityAttr=218,bid=207,addid = 207,reduceid = 236,techcostreduce = 251}, --金矿建筑强化buffID（buff表ID），时间，基础价格,强化道具ID,BUFF表类型,容量加成ID，添加建筑ID，产量加成ID,产量降低BUFF，科研金币消耗加成ID
	["buff_resource"] = {buff_food = 19, buff_wood = 18, buff_iron = 20, buff_silver = 21,buff_gold = 22,},--农田提升、伐木场提升、铁矿提升、银矿提升、金矿提升的typeid
	["scoutprice_time"] = {lately_time = 300,} ,--最近侦查时间报告（秒）
    ["masstime"] = {30,600,1800,3600,},--集结时间
	["prison"] = { army_loss = {5000,10000,} , castle_away=20, castle_custody=22, max_reward=2000000000, min_reward=10000, max_ransom=2000000000, min_ransom=10000, grape=11005000, revive=11005100, kill=11005200,grape_time=43200,ransom_rate = 3000,kill_time=86400,},-- 士兵损失比例=每个比例俘虏一个（50%，100%）已无效，俘虏逃脱城堡等级，俘虏监禁城堡等级，赏金最大值，赏金最下值，赎金最大值，赎金最小值，葡萄汁道具ID，复活道具ID，立即献祭道具ID,魔法药水/监禁缩短至时间,赎赏金税率,立即献祭加成时间
	["allian_teambattle"] = {rank = 4 , task_cd = 2, members = 2, lv = 2, allian_num = 2, quest_number = 14, stage = 1, uplv = 5, downlv = 5,uplv_max = 2, downlv_max = 2 , purchases = 1,cost = 1000,random_icon="icon_wenhao_02",rank_stage = 8,rank_lv =1,}, --编辑任务的最低联盟阶级要求=R4，任务刷新时间,参与需要的成员人数,参与城堡等级限制,每个分组联盟个数,投放任务数量,晋级需要的积分阶级，至史诗联赛晋级需要的排名，至史诗联赛降级需要的排名,史诗联赛晋级需要的排名，传奇联赛降级需要的排名，可购买次数，购买次数单次花费魔晶数，随机任务初始图标,排名奖励需要阶级，排名奖励需要名次
	["online_award"] = {{count=5,prob=10,multiple=5},{count=10,prob=30,multiple=5},{count=20,prob=60,multiple=5},},--在线奖励5次数，概率，倍数 --10次数，概率，倍数 --20次数，概率，倍数 
	["puppet_conversion"] = {num = 0, die = 2000,},--死亡傀儡转化受伤傀儡初始值(万分比),傀儡死亡系数
	["openground"] = { proportion = 0.5,}, --玩家战力/空地战力大于此比例，则弹框
	["SLG_battle_wall"] = {morale = 400,time = 15,damage=150,battle_time=40,},--SLG战斗城墙未倒塌扣的士气值，限制时间,城墙伤害计算参数，战斗总时间
	["integral"] = {lv = {1,7,10,14,18,22,26,30,},rank ={1,2,3,10,30,50,100},},--积分活动城堡等级区间（最小）,名次区间（最大）
	["strongestlord"] = {rank={1,2,3,4,5,6,7,8,9,10,19,29,39,49,59,69,79,89,100,},num =2000,},--最强领主名次区间,最大总排名
	["slg_lord_exp"] = {a=100,b=1.5,},--SLG战斗领主经验  =  对方损失战力/100（战斗胜利方*1.5）（向上取整）
	["slg_hero_exp"] = {a=1500,b=1.5,},	--SLG战斗英雄经验  =  对方损失战力/1500（战斗胜利方*1.5）（向上取整）
	["slg_spirit_exp"] = {a=700,b=1.5,},	--SLG战斗精灵经验  =  对方损失战力/700（战斗胜利方*1.5）（向上取整）
	["aggregate"] = {number=30,} ,  --集结（士兵援助）人数上限，不包含队长，算上队长31人
	["dress_star"] = {lv=20 ,} , --城堡等级≥20，才可强化装扮
	["king_war"] = {war_time=3715200 , war_interval= 691200, } , --第一次国王战开服倒数（秒）43天，正常国王战倒数8天（秒）
	["facelook"] = { id =11005700, num =1, cost =1500} , --- 表情图章，每次使用数量1，花费魔晶
	["offer"] = {offer = "des_2335" , offer2 = "des_2336",},---监狱世界公告文本 献祭者公告文本，被献祭者公告文本
	["head_gm"] = { head = "head_w_001" } , --- 聊天系统中，系统默认头像	
	["rinseking"]={box=15004500,heroID = 23,name="des_2419",num = 80,heroreward={43300230,10},time=604800,rewardtime=259200,preciew_num=1},--新王崛起宝箱，赠送的英雄ID，赠送的英雄宝箱名字，赠送英雄需要达成的任务数量，新王崛起赠送的英雄碎片及数量,任务可完成时间，结算阶段时间（只能领奖不能完成任务）,可提前预览的未解锁任务个数
	["multinationa"] = {military_lv = 1  , military_number= 0 ,} , ----跨国时降低的军衔等级  和军衔点 
	["king_dress"] = {1041,2061,3071,4061,5061,},----国王装扮
	["marshal_dress"] = {5071,},----元帅装扮
	["game_base_num"] = {Training_number = 0 },--- 士兵初始训练数量
	["invite_binding_reward"]={1000,100,13000106,3,14001101,1,},--邀请码绑定奖励
	["invite"]={cd=1296000,lv=16,box_lv=6},-- 更换邀请码CD时间,可被邀请的最高城堡等级,完成进度宝箱需要的城堡等级
	["binding_reward"]={1000,100,11001004,1,11001300,1,13000107,1,},--绑定账号奖励
	["online_limit"] ={ castlelv=5, number=5,advert_time=10,Icebreaking=604800,packType={8},},--驿站在线奖励城堡等级限制，限制等级内每轮次数，广告间隔5分钟时间(秒),破冰展示7天（秒）,在线奖励广告默认播放礼包类型对应RECHARGEBASE表packType类型
	["recharge"]={build=902,},--购买该礼包成功，则永久开启第二建筑队列
	["recharge_buide"]={recharge_id=901, buff_id=253, buff_num=1800,buff_city=24,},--购买该礼包成功，则获得加成，加成数值,城市增益客户端用BUFF_CITY表id
	["day_pack"]={30},--每日礼包城堡等级：1-30
	["recharge_ice"]={show_time=604800,countdown=172800},--破冰礼包主界面展示,若玩家未购买,7天后主动撤销主界面展示；虚假倒计时48h
	["freeca"]={ID=106,time_num=2,reimburse={1000,500,13000111,1,12000510,1,12000112,1,12000212,1,12000312,1,12000412,1}},--新月卡id，时间倍数，补偿物品
	["recharge_lucky"]={specially_time=60,},--特效冷却时间1分钟
	["world_boss"]={refresh="des_2519",kill="des_2520",alliance_rank=5,personal_rank=30,free_move = 1,move_diamonds = 500,},--世界BOSS刷新跑马灯，被击杀跑马灯,联盟排行榜显示数目，个人排行榜显示数目，免费迁城次数，魔晶迁城价格
	["friend_limit"]={ number = 200,},--关注好友数量上限
	["blank_limit"]={ number = 200,},--黑名单数量上限	
	["donate_res"] = {1001, 1, 1002, 1, 1003, 1, 1004, 1, 1005,1,} , --联盟捐献所需资源出现的城堡等级
	["maintain"] = {buffinfo = {10029, 7200,}, wartime = 1200, }, ---维护保护罩buffid,时间 ，  王宫要塞冻结争夺最少时长
	["treasure_item"]={11005900,1},--宝物保存道具ID
	["invite_move"]={cd_time = 900},--邀请迁城CD时间
	["elite_soldier_cfg"]={{10101, 10102},{10201, 10202},{10301, 10302}},---文明切换对应兵种
	["control_period"]=60,--王国管制时间，即迁入保护期 60天
	["animation"]={darkmonster=2,rebelarmy=6,castle=6,camp=6,garrison=6,palaca=6,resource=0,},--动画时长：魔物2s,slg小怪6s,城堡6s,查希里叶营地6s,驻军6s，皇宫6s,资源田0s
	["Civilization_preview"]={[201]= 5, [202] = 5, [203] = 6, [204] = 6, [205] = 6, [206] = 6, [207] = 6,},---5块农田、5块伐木场、6块铁矿、6块白银、6块行军帐篷、6块医疗帐篷、6块金矿
	["mail_pvp"]={1020,1040,1070},--PVP战报：领主经验,精灵经验,文明声望
	["mail_rebelarmy"]={1020,},--叛军战报:领主经验
	["mail_camp"]={1020,},--营地战报：领主经验
	["mail_darkmonster"]={1020,},--魔物战报：领主经验
	["hero_guide"]={43300190,43300190,43300160,43300160,43300240,43300240,43300230,43300230,43300250,43300250,43300260,43300260,43300270,43300270,43300280,43300280,43300290,43300290,43300300,43300300,43300330,43300330,43300370,43300370,43300380,43300380,43300310,43300310},--伊布利梓,佘姆赛,扎特·达瓦希,赛阿丹·奥勒,鲁扬医师,努尔胡达,姜杉王子,萨利姆,泰沃杜德,朱海莱,阿吉布,贝斯蒂,荷鲁斯,泽卜莱康
	["civilization_pack"]={ID=403,sand=1,sky=3,sea=5,},---文明切换礼包ID,礼包沙之国对应,礼包空之国对应,礼包海之国对应
	["daily_pack"]={Stamina=401,Endurance=402,Material=404,Emoji=405,rebelArmy=406},---行动力固定礼包、体力固定礼包、材料宝箱固定礼包、表情图章固定礼包、平叛令礼包
	["arabcountry"]={"LB","EG","DZ","IQ","YE","JO","MA","AE","OM","BH","QA","KW","SA"},-- 中东国家默认选择沙文明
	["alliance_jion_reward"] = {1000,400,},--初次入盟奖励
	["initial_warden_soldier"] = {20101,50,20201,50,20301,50} ,--初始伤兵：50个步兵,50个骑兵,50个弓兵
	["friend_beapply_limit"]={ number = 100,},--被申请数量上限
	["alliance_tech"]={cd = 900,time = 0,lock_time=21600,lv=1,},--科技捐献CD；入盟可捐献时间;捐献锁定时间;可捐献城堡等级
	["alliance_help"]={num = 0 ,time = 0},--联盟帮助基础次数，帮助减少的时间（万分比）
	["alliance_edit_cost"]={name=200,shortname=200,flag=200,invite_notice=300,change_kingdom=1000,newbie_create=200},--修改联盟名称消耗魔晶，修改联盟简称消耗魔晶，修改联盟旗帜消耗魔晶，发送联盟公告邀请消耗魔晶，更换国家消耗魔晶，创建联盟消耗魔晶
	["fbreward"]={1000,200},--FB粉丝好礼奖励：200魔晶
	["url"]={test="http://sfaction.onemt.co/invite?name=XXXXX&inviteCode=XXXXX&source=XXXX",formal="http://sfaction.onemt.co/invite?name=XXXXX&inviteCode=XXXXX&source=XXXX",},--邀请送豪礼H5测试地址，正式地址
	["hospital"]={basics=100000 ,multiple=3,},--王国医院基础容量，普通医院当前容量*倍数
	["select"]={60},--快速搜索范围
	["rebelarmy"]={range = 400,limit = 6 , initial_num = 3 , reply = 3600,},--叛军可攻打范围，平叛令回复上限，初始平叛令，回复1点平叛令需要的时间
	["alliance_language"] = 1,--默认的联盟语言
	["Kingdom_task"] = {Notice_time = 86400,opentime = 43200,},--王国任务预告时间1天、任务持续时间12小时
	["injured"]={[3]=100,[5]=100,},--平叛伤兵比例、攻打查希里叶营地伤兵比例（万分比向上取整）
	["loginreward"] = {lv=5,loginhero_lv=4,},--首次领取每日登陆奖励的城堡等级触发点，首次弹出累计登陆送英雄的城堡等级触发点
	["rebelarmy_num"]={lv_base=10,lv_up=1,num_up=200},--开始递增的基础怪物等级，递增等级，递增数量（从10级开始，每增加1级，总刷新数增加200个）
	["SlgBattleFps"] = {SLGHERO=0,ARMY=0,WALL=0,GENIUS=15,PUPPET=30,BARTIZAN=20,Catapult=45},--根据登录界面平均FPS，决定在XX帧以下则SLG战斗不显示该种类资源，SLGHERO=英雄、ARMY=军队、PUPPET=傀儡、BARTIZAN=箭塔、WALL=城墙、GENIUS=精灵、Catapult=投石车
	["rebelarmy_time"]={10},--叛军每日挑战次数
	["move_list"]={5,20,5,20,},--王国频道迁入的联盟实力排行，王国频道迁入的领主实力排行，王国频道迁出的联盟实力排行，王国频道迁出的领主实力排行
	["chatroom"] = {create = "des_3205",invite = "des_3206",kick = "des_3219",out = "des_3207",}, --聊天创建群聊、邀请加入群聊、移除群聊、离开群聊
	["daily_config"]={2,},--日常任务的随机任务刷新数量
	["kingroad_open"]=9,--王者之路开启等级
	["county_palace"]={1,1,2,2,3,3},--文明对应PALACE表ID，对应宫殿索引,A文明ID,B对应模型表ID
	["spirit"]={lock=12,},--精灵解锁的神灯修复任务ID
	["frame_rate"]=45,--登陆界面帧率，高于该帧率则开启高帧率设置，否则开启低帧率
	["zoom_castle"]={5,3,6.5,2.5,7,4},--主城镜头：默认，回弹后最小，回弹后最大，操作时最小，操作时最大，主城镜头回弹速度
	["zoom_outside"]={2.6,1.8,3.2,1.6,3.3,2},--大地图镜头：默认，回弹后最小，回弹后最大，操作时最小，大地图镜头回弹速度
	["initial_Shield"]=7,---城堡7级升级8级时解除新手护盾判断
	["warstar"]={mutually=30003,lv=1,rank_stage=8,rank_list=100,notice_show=5,notice_time=86400,open_time=172800,lv_list = {1,7,9,11,14,18,22,26,30,},rank ={1,2,3,10,30,50,100},},--备战之星：互斥的活动ID，参与城堡等级限制,排名奖励需要的阶级，可获得排名奖励的名次,预告出现时间(上个国王战结束后第N个0点），预告持续时间，活动开启时间(上个国王战结束后第N个0点），活动持续时间,城堡等级区间（最小）,名次区间（最大)
	["moment"]={notice_show=79200,notice_time=14400,open_time=72000,collect_multiple=5,collect_change=7200,title="des_3356",new_server=5184000,lv=9,},--时刻活动预告开启时间（以0点为基准），预告持续时间，活动持续时间，丰收时刻资源田轮换时间，丰收时刻积分倍数，任务标题，新服时间(单位：秒),低堡的城堡等级（小于等于）
    ["plot_quest"]={castle6=3,castle14=5,queue=10,},--城堡1-6级3s，城堡6-14级5S,建筑队列弹框10s
	["hero_commend"]={actual=150,total=500,},--实际排名节点，总排名节点
	["limit_login"] = {opentime = { {39600, 50400}, {68400, 79200} }, starttime = 21600, showtime = 39600,},--限时登陆预告开启时间（以0点为基准），预告持续时间，激活时间段（以0点为基准），激活后持续时间，预告显示的活动时间
	["cumu_recharge"] = {name="des_3425"},--累计充值任务名称
	["cumu_consum"] = {name="des_3496"},--累计消费任务名称
	["ranking"]={lv=6},--排行榜解锁等级配置
	["palacec_warabuff"]={125,6000,126,6000,128,6000,},--军团攻击下降BUFFid,值，军团防御下降BUFFid,值，军团生命下降BUFFid,值
	["camp_guide"]={distance=150,},--触发引导需要的查希里叶营地离玩家城堡的距离（单位公里）
	["chaser"]={time = {10,600000,},condition= {1,1,},},--n＜服务器开服天数＜m、x个城堡等级达到y级；
	["sea_reward"] = {open_day=7,recharge_day=5,free_reward={13000106,2,12000105,1,12000205,1,12000305,1,12000405,1,},continue_reward={43300300,20,11004002,10,15002302,10,},quest=3,},--海之馈赠活动持续天数，需要的充值天数，免费宝箱奖励，累计充值奖励，每日需要充值的金额（美金）
	["loyalty_reward"] = {open_day=7,recharge_day=5,free_reward={13000106,2,12000105,1,12000205,1,12000305,1,12000405,1,},continue_reward={43300310,20,11004002,10,15002302,10,},quest=3,},--忠义之恩活动持续天数，需要的充值天数，免费宝箱奖励，累计充值奖励，每日需要充值的金额（美金）
	["pack_store"] = {cycle_time=259200,},--全服循环时间
	["lucky_turntable"]= {Last_day=2,itemMax_num=15,oneTime_shopItemId=11048,tenTimes_shopItemId=11049,item_id=11006300,obtain_id=11006300,daily_pack={407,408,409},},--奖池持续天数、幸运币每日魔晶最大购买个数、幸运币1次商品Id、幸运币10次商品Id、幸运币道具id、引导跳转id
	["palacewar_title"] = {end_time=3600,},--王国称号结算时间
	["max_lord_defence_soldier_num"] = {30000000},--防守方添加参战士兵数量上限
	["item_id_range"] = { camp_box_start_id=15002600,camp_box_end_id=15002629,},--最低级查希里叶宝箱ID，最高级查希里叶宝箱ID
	["SLG_DefenseDamageFactor"] = { hero=750000,genius=3000000,},--英雄SLG技能、精灵SLG技能最大攻击士兵数量
	["Crystal_tree"]={reply_time=21600,max_num=10,total_num=9999,item=11000501,},--转化次数回复时间（秒），转化次数上限，每日可转化总次数,转化代币的道具ID
	["Growth_Fund"]={castleLevel=5,newgoto_01=132,newgoto_02=129,name="title_112",des="des_3583",icon="icon_jijing_01",},--成长基金开启等级、引导1特效、引导2剧情对话、名称、描述、图标
	["Wheel_of_Fortune"]={castleLevel=11,newgoto_01=133,newgoto_02=130,name="title_203",des="des_3584",icon="icon_xyzp_01",},--幸运大转盘开启等级、引导1特效、引导2剧情对话、名称、描述、图标
	["discount"] = {time = 86400,activity_time= 604800,open_time=1,newgoto_01=134,newgoto_02=131,name="title_133",des="des_3585",icon="icon_legou_01"},--折扣券提示时间：86400秒、活动持续时间7d、新账号15天后开启活动、引导1特效、引导2剧情对话、名称、描述、图标
	["Workshop"] = {position = 2,name ="des_3605",gift_ID = 107 },--初始栏位，黑魂元素名称,至尊卡礼包ID
	["darkmonster_limit"] = {build_ID=113,build_Lv=1,},--猎杀妖魔前置建筑ID，前置建筑等级
	["Outstanding"] = {show_num = 30,record_num=999,open_time = 864000,refresh_time = 10800,delay_time = 86400},--傲视群雄排行榜显示人数，记录的上榜人数,活动持续时间，排行榜刷新时间,排名奖励结算延迟时间
	["pack_crit"]={num=3,multiple=2,show_multiple=5,show_des= "des_3638"},--功能开启后，前3次购买随机出一次2倍暴击,需要走马灯&王国公告的倍数,走马灯&王国公告多语言
    ["camp"] = {limit_Lv = 7,element_ID = 1103,element_des = "des_3644"},--参与攻营的城堡等级限制,黑魂元素ID,黑魂元素描述
	["pack_plus"] = {open_time=432000,plus_time=86400,},--创号5天后开启加码,加码倒计时；
	["share_information"] = { power = {1000000,99999999,999999999,1000000000}, str = {{"des_3639","des_3640"},{"des_3641","des_3642"},{"des_3758","des_3759"},{"des_3760","des_3761"}},},--分享的属性者战力，战力说明(多语言数量不能删除，条数只能多不能少，若不想要可用相同多语言替代)
	["treasury"] = { castlelv = 12, smoke=300, fire=300, notice_time = 86400 , open_time = 86400, show_level = { 4,5 } , refresh_time =10800 , free_move = 1,move_diamonds = 500,refresh_msg_key ="des_3710"  ,}, --宝藏功能开放等级， 冒烟时间， 着火时间 预告持续时间 活动持续时间 活动中显示的坐标的宝藏等级 宝藏刷新间隔时间，免费迁城次数  迁城魔晶数
	["integral_normal"] = {open_time = 691200 ,strongestlord_before_time = 86400,strongestlord_later_time = 86400,king_war_before_time = 259200,king_war_later_time = 86400,},--普通挑战开服第8天开放，最强领主活动开启前1天不开放，最强领主活动结束后1天不开放，国王战开启前3天不开放，国王战结束后1天不开放
	["Bullet_time"] = {time_scale = 0.5,duration=2},--播放时间倍率,子弹时间持续时长（秒）；

};return SystemConfig

