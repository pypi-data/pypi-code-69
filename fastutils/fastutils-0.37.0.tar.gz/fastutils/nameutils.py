import random








last_names = [
('黄', 165),
('赵', 165),
('王', 164),
('钱', 164),
('张', 163),
('孙', 162),
('陈', 162),
('郑', 161),
('李', 160),
('周', 159),
('吴', 158),
('蒋', 91),
('冯', 89),
('杨', 66),
('沈', 51),
('万', 10),
('东', 10),
('仇', 10),
('余', 10),
('佟', 10),
('冷', 10),
('凌', 10),
('卢', 10),
('可', 10),
('司', 10),
('向', 10),
('商', 10),
('堵', 10),
('姚', 10),
('宣', 10),
('居', 10),
('席', 10),
('强', 10),
('房', 10),
('支', 10),
('文', 10),
('晁', 10),
('曹', 10),
('权', 10),
('查', 10),
('柴', 10),
('栗', 10),
('欧', 10),
('殳', 10),
('池', 10),
('汪', 10),
('沃', 10),
('海', 10),
('爱', 10),
('由', 10),
('皇甫', 10),
('相', 10),
('福', 10),
('窦', 10),
('童', 10),
('索', 10),
('翁', 10),
('胡', 10),
('艾', 10),
('蓟', 10),
('诸葛', 10),
('谢', 10),
('贝', 10),
('金', 10),
('钭', 10),
('阙', 10),
('陆', 10),
('雷', 10),
('乔', 9),
('井', 9),
('付', 9),
('代', 9),
('仲', 9),
('仲孙', 9),
('佘', 9),
('侯', 9),
('候', 9),
('元', 9),
('公', 9),
('凤', 9),
('剡', 9),
('单于', 9),
('厉', 9),
('古', 9),
('同', 9),
('和', 9),
('唐', 9),
('墨', 9),
('孔', 9),
('宰父', 9),
('尉迟', 9),
('尚', 9),
('归', 9),
('惠', 9),
('扈', 9),
('操', 9),
('施', 9),
('梁丘', 9),
('毕', 9),
('滕', 9),
('牛', 9),
('狄', 9),
('秦', 9),
('竺', 9),
('糜', 9),
('经', 9),
('苑', 9),
('苟', 9),
('荆', 9),
('蔚', 9),
('褚', 9),
('诸', 9),
('谷', 9),
('轩辕', 9),
('边', 9),
('迟', 9),
('逄', 9),
('隆', 9),
('黎', 9),
('龚', 9),
('伊', 8),
('位', 8),
('储', 8),
('公冶', 8),
('养', 8),
('利', 8),
('别', 8),
('单', 8),
('危', 8),
('卿', 8),
('司空', 8),
('咸', 8),
('喻', 8),
('国', 8),
('夏', 8),
('宇', 8),
('宗', 8),
('屠', 8),
('左', 8),
('康', 8),
('慎', 8),
('成', 8),
('戚', 8),
('晋', 8),
('晏', 8),
('景', 8),
('杭', 8),
('松', 8),
('柯', 8),
('栾', 8),
('桓', 8),
('步', 8),
('母', 8),
('汝', 8),
('涂', 8),
('焦', 8),
('牧', 8),
('班', 8),
('甘', 8),
('申', 8),
('空', 8),
('简', 8),
('终', 8),
('胥', 8),
('芮', 8),
('茅', 8),
('荣', 8),
('贡', 8),
('辛', 8),
('通', 8),
('逯', 8),
('邓', 8),
('邰', 8),
('邴', 8),
('郎', 8),
('都', 8),
('鄢', 8),
('钟', 8),
('钦', 8),
('闫', 8),
('闾丘', 8),
('阴', 8),
('靳', 8),
('颛孙', 8),
('颜', 8),
('万俟', 7),
('严', 7),
('亓', 7),
('伯', 7),
('倪', 7),
('充', 7),
('冀', 7),
('南门', 7),
('占', 7),
('哈', 7),
('宋', 7),
('宰', 7),
('寿', 7),
('屈', 7),
('巢', 7),
('巴', 7),
('师', 7),
('年', 7),
('庞', 7),
('弓', 7),
('彭', 7),
('徐', 7),
('微', 7),
('敖', 7),
('时', 7),
('朴', 7),
('楼', 7),
('段', 7),
('毛', 7),
('漆', 7),
('熊', 7),
('燕', 7),
('甄', 7),
('盖', 7),
('秋', 7),
('端木', 7),
('第五', 7),
('籍', 7),
('米', 7),
('羿', 7),
('苏', 7),
('茹', 7),
('董', 7),
('蓝', 7),
('虞', 7),
('衡', 7),
('言', 7),
('计', 7),
('费', 7),
('赫连', 7),
('越', 7),
('郝', 7),
('门', 7),
('闵', 7),
('阎', 7),
('阮', 7),
('陶', 7),
('鞠', 7),
('项', 7),
('须', 7),
('鬱', 7),
('丰', 6),
('云', 6),
('傅', 6),
('公羊', 6),
('厍', 6),
('吉', 6),
('壤驷', 6),
('子车', 6),
('尤', 6),
('德', 6),
('怀', 6),
('戈', 6),
('扶', 6),
('方', 6),
('昌', 6),
('明', 6),
('束', 6),
('梅', 6),
('沙', 6),
('温', 6),
('湛', 6),
('滑', 6),
('满', 6),
('瞿', 6),
('禄', 6),
('章', 6),
('耿', 6),
('聂', 6),
('芦', 6),
('裘', 6),
('裴', 6),
('詹', 6),
('谯', 6),
('贲', 6),
('贺', 6),
('轩', 6),
('连', 6),
('邬', 6),
('郗', 6),
('郭', 6),
('长孙', 6),
('闻人', 6),
('饶', 6),
('鲁', 6),
('乐正', 5),
('乜', 5),
('习', 5),
('于', 5),
('亓官', 5),
('任', 5),
('伍', 5),
('党', 5),
('公良', 5),
('冉', 5),
('刁', 5),
('劳', 5),
('包', 5),
('双', 5),
('司徒', 5),
('奚', 5),
('姜', 5),
('姬', 5),
('宇文', 5),
('宗政', 5),
('崔', 5),
('常', 5),
('庄', 5),
('庹', 5),
('廉', 5),
('廖', 5),
('易', 5),
('昝', 5),
('暨', 5),
('梁', 5),
('武', 5),
('段干', 5),
('水', 5),
('汲', 5),
('游', 5),
('申屠', 5),
('祖', 5),
('程', 5),
('练', 5),
('花', 5),
('苗', 5),
('莘', 5),
('蒙', 5),
('薛', 5),
('袁', 5),
('西门', 5),
('解', 5),
('赖', 5),
('车', 5),
('郁', 5),
('雍', 5),
('霍', 5),
('韶', 5),
('骆', 5),
('高', 5),
('鱼', 5),
('齐', 5),
('龙', 5),
('丁', 4),
('东方', 4),
('乌', 4),
('令狐', 4),
('仰', 4),
('公孙', 4),
('卓', 4),
('印', 4),
('司寇', 4),
('季', 4),
('宦', 4),
('宫', 4),
('容', 4),
('宿', 4),
('寇', 4),
('岑', 4),
('干', 4),
('应', 4),
('庾', 4),
('弘', 4),
('於', 4),
('暴', 4),
('曾', 4),
('杜', 4),
('柏', 4),
('桂', 4),
('殷', 4),
('法', 4),
('洪', 4),
('潘', 4),
('琴', 4),
('穆', 4),
('符', 4),
('笪', 4),
('红', 4),
('缪', 4),
('能', 4),
('萧', 4),
('蒯', 4),
('路', 4),
('那', 4),
('郦', 4),
('酆', 4),
('阚', 4),
('隗', 4),
('东门', 3),
('仉督', 3),
('从', 3),
('伏', 3),
('俞', 3),
('全', 3),
('况', 3),
('勾', 3),
('华', 3),
('卫', 3),
('史', 3),
('叶', 3),
('吕', 3),
('呼延', 3),
('夔', 3),
('太叔', 3),
('孟', 3),
('宁', 3),
('家', 3),
('富', 3),
('尹', 3),
('山', 3),
('岳', 3),
('左丘', 3),
('巩', 3),
('巫马', 3),
('平', 3),
('广', 3),
('慕', 3),
('揭', 3),
('智', 3),
('柳', 3),
('桑', 3),
('江', 3),
('浦', 3),
('浮', 3),
('牟', 3),
('祁', 3),
('祝', 3),
('禹', 3),
('羊', 3),
('臧', 3),
('范', 3),
('葛', 3),
('蔡', 3),
('蔺', 3),
('覃', 3),
('訾', 3),
('许', 3),
('赏', 3),
('邱', 3),
('邵', 3),
('郏', 3),
('韩', 3),
('顾', 3),
('魏', 3),
('麻', 3),
('仝', 2),
('佴', 2),
('冶', 2),
('匡', 2),
('卜', 2),
('卞', 2),
('后', 2),
('娄', 2),
('封', 2),
('巫', 2),
('戎', 2),
('戴', 2),
('有', 2),
('生', 2),
('白', 2),
('益', 2),
('盛', 2),
('石', 2),
('纪', 2),
('罗', 2),
('翟', 2),
('舒', 2),
('苍', 2),
('英', 2),
('莫', 2),
('薄', 2),
('融', 2),
('谈', 2),
('谭', 2),
('贾', 2),
('邢', 2),
('邹', 2),
('郜', 2),
('鄂', 2),
('闻', 2),
('阳', 2),
('韦', 2),
('马', 2),
('乐', 1),
('亢', 1),
('何', 1),
('侍', 1),
('关', 1),
('农', 1),
('刘', 1),
('南', 1),
('司马', 1),
('安', 1),
('宓', 1),
('尧', 1),
('嵇', 1),
('帅', 1),
('幸', 1),
('慕容', 1),
('曲', 1),
('朱', 1),
('林', 1),
('楚', 1),
('榖梁', 1),
('樊', 1),
('欧阳', 1),
('汤', 1),
('淳于', 1),
('濮', 1),
('璩', 1),
('田', 1),
('皮', 1),
('管', 1),
('缑', 1),
('肖', 1),
('荀', 1),
('蒲', 1),
('蓬', 1),
('郤', 1),
('钮', 1),
('鲍', 1),
('东郭', 1),
('南宫', 1),
('夹谷', 1),
('百里', 1),
('澹台', 1),
('拓跋', 1),
('上官', 1),
('公西', 1),
('鲜于', 1),
('钟离', 1),
('漆雕', 1),
('濮阳', 1),
('羊舌', 1),
('夏侯', 1),
]



first_names = [
('江', 65),
('晓', 63),
('伟', 54),
('鹏', 51),
('杰', 48),
('俊', 42),
('涛', 41),
('佳', 40),
('超', 40),
('婷', 40),
('志', 37),
('飞', 34),
('斌', 34),
('丽', 32),
('军', 31),
('辉', 30),
('建', 29),
('小', 28),
('敏', 28),
('亚', 28),
('静', 27),
('春', 26),
('磊', 26),
('勇', 26),
('慧', 24),
('玉', 24),
('梦', 24),
('凯', 24),
('波', 23),
('天', 23),
('芳', 23),
('艳', 23),
('浩', 23),
('思', 23),
('馨', 22),
('鑫', 22),
('亮', 22),
('一', 22),
('雪', 21),
('峰', 21),
('丹', 21),
('娟', 20),
('晨', 20),
('琳', 19),
('雨', 19),
('威', 19),
('祥', 18),
('洋', 18),
('旭', 18),
('良', 18),
('嘉', 18),
('柳', 18),
('光', 18),
('锋', 17),
('振', 17),
('栋', 17),
('君', 16),
('瑞', 16),
('剑', 16),
('霞', 16),
('琦', 15),
('智', 15),
('兴', 15),
('青', 15),
('颖', 15),
('玲', 15),
('璐', 15),
('瑶', 14),
('欣', 14),
('新', 14),
('永', 14),
('子', 14),
('艺', 14),
('倩', 14),
('娜', 14),
('琪', 13),
('晶', 13),
('健', 13),
('博', 13),
('川', 12),
('可', 12),
('雅', 12),
('立', 12),
('莹', 12),
('彬', 12),
('翔', 12),
('冬', 12),
('然', 12),
('航', 11),
('姗', 11),
('庆', 11),
('维', 11),
('豪', 11),
('少', 11),
('珊', 11),
('楠', 10),
('清', 10),
('中', 10),
('宏', 9),
('刚', 9),
('恒', 9),
('珍', 9),
('炜', 9),
('泽', 9),
('雯', 9),
('雄', 9),
('冰', 9),
('正', 9),
('贤', 9),
('聪', 9),
('蕾', 9),
('朋', 9),
('旺', 8),
('虎', 8),
('群', 8),
('昊', 8),
('秀', 8),
('凡', 8),
('达', 8),
('政', 8),
('星', 8),
('靖', 8),
('恺', 8),
('世', 8),
('坤', 8),
('欢', 8),
('洁', 7),
('萍', 7),
('婉', 7),
('忠', 7),
('兵', 7),
('宝', 7),
('萌', 7),
('远', 7),
('瑜', 7),
('茂', 7),
('攀', 7),
('耀', 7),
('岩', 7),
('男', 7),
('根', 7),
('琛', 7),
('妮', 7),
('圆', 7),
('大', 7),
('甜', 7),
('莎', 7),
('璇', 6),
('学', 6),
('邦', 6),
('月', 6),
('力', 6),
('彪', 6),
('书', 6),
('灵', 6),
('兰', 6),
('姣', 6),
('治', 6),
('帆', 6),
('胜', 6),
('铭', 6),
('霖', 6),
('骏', 6),
('莉', 6),
('民', 6),
('煜', 6),
('壮', 6),
('诗', 6),
('乾', 6),
('巍', 6),
('震', 6),
('会', 6),
('露', 6),
('盼', 6),
('儒', 6),
('灿', 5),
('竹', 5),
('汉', 5),
('莲', 5),
('圣', 5),
('毅', 5),
('茜', 5),
('薇', 5),
('挺', 5),
('启', 5),
('香', 5),
('贵', 5),
('迪', 5),
('普', 5),
('晗', 5),
('悦', 5),
('发', 5),
('蓉', 5),
('为', 5),
('素', 5),
('鸣', 5),
('进', 5),
('长', 5),
('玮', 5),
('彦', 5),
('义', 5),
('炎', 5),
('琼', 5),
('硕', 5),
('赛', 5),
('源', 5),
('传', 4),
('继', 4),
('增', 4),
('爽', 4),
('啸', 4),
('烨', 4),
('希', 4),
('如', 4),
('珺', 4),
('菲', 4),
('美', 4),
('赟', 4),
('承', 4),
('保', 4),
('睿', 4),
('照', 4),
('昕', 4),
('昭', 4),
('均', 4),
('洲', 4),
('园', 4),
('自', 4),
('曦', 4),
('笑', 4),
('潇', 4),
('礼', 4),
('扬', 4),
('妍', 4),
('冠', 4),
('淑', 4),
('运', 4),
('兆', 4),
('芬', 4),
('培', 4),
('伦', 4),
('涵', 4),
('芝', 4),
('锦', 4),
('焕', 4),
('昆', 4),
('树', 4),
('瑾', 4),
('敬', 4),
('怡', 3),
('纯', 3),
('轲', 3),
('轶', 3),
('翠', 3),
('峥', 3),
('宜', 3),
('雁', 3),
('奕', 3),
('昱', 3),
('娴', 3),
('定', 3),
('愉', 3),
('甫', 3),
('哲', 3),
('孝', 3),
('锐', 3),
('朝', 3),
('标', 3),
('裕', 3),
('梓', 3),
('银', 3),
('加', 3),
('皓', 3),
('崇', 3),
('桂', 3),
('铎', 3),
('钰', 3),
('铃', 3),
('奇', 3),
('宾', 3),
('驰', 3),
('真', 3),
('寒', 3),
('晟', 3),
('润', 3),
('娇', 3),
('妙', 3),
('菁', 3),
('跃', 3),
('沁', 3),
('行', 3),
('冲', 3),
('暄', 3),
('绍', 3),
('心', 3),
('想', 3),
('婧', 3),
('宽', 3),
('婕', 3),
('起', 3),
('先', 3),
('阔', 3),
('迎', 3),
('城', 3),
('科', 3),
('京', 3),
('植', 2),
('晴', 2),
('芸', 2),
('其', 2),
('羲', 2),
('念', 2),
('汇', 2),
('璨', 2),
('夫', 2),
('辰', 2),
('望', 2),
('战', 2),
('奎', 2),
('依', 2),
('显', 2),
('原', 2),
('皇', 2),
('联', 2),
('祎', 2),
('森', 2),
('渊', 2),
('淳', 2),
('寅', 2),
('泉', 2),
('鸿', 2),
('滨', 2),
('分', 2),
('晔', 2),
('祺', 2),
('含', 2),
('妹', 2),
('旻', 2),
('谊', 2),
('胤', 2),
('喜', 2),
('舟', 2),
('野', 2),
('令', 2),
('营', 2),
('猛', 2),
('征', 2),
('映', 2),
('翰', 2),
('媛', 2),
('桐', 2),
('愿', 2),
('镇', 2),
('研', 2),
('炳', 2),
('善', 2),
('晖', 2),
('佑', 2),
('逢', 2),
('珮', 2),
('守', 2),
('友', 2),
('见', 2),
('懿', 2),
('锜', 2),
('钢', 2),
('逸', 2),
('召', 2),
('宸', 2),
('来', 2),
('垚', 2),
('玺', 2),
('昂', 2),
('豆', 2),
('翀', 2),
('四', 2),
('萱', 2),
('之', 2),
('畅', 2),
('旋', 2),
('苹', 2),
('彤', 2),
('弯', 2),
('桥', 2),
('道', 2),
('翼', 2),
('熙', 2),
('士', 2),
('鼎', 2),
('芃', 2),
('娅', 2),
('荟', 2),
('淙', 2),
('造', 2),
('创', 2),
('才', 2),
('训', 2),
('湖', 2),
('仕', 2),
('湘', 2),
('俏', 2),
('影', 2),
('添', 2),
('招', 2),
('展', 2),
('枫', 2),
('萃', 2),
('苜', 1),
('葵', 1),
('笔', 1),
('岚', 1),
('阅', 1),
('殿', 1),
('苈', 1),
('概', 1),
('镭', 1),
('舰', 1),
('丘', 1),
('尔', 1),
('蛟', 1),
('拓', 1),
('笠', 1),
('弦', 1),
('升', 1),
('曼', 1),
('歆', 1),
('棋', 1),
('珏', 1),
('俭', 1),
('延', 1),
('峯', 1),
('援', 1),
('统', 1),
('互', 1),
('亭', 1),
('钏', 1),
('泓', 1),
('劲', 1),
('岫', 1),
('闽', 1),
('韵', 1),
('捷', 1),
('载', 1),
('忆', 1),
('伶', 1),
('滔', 1),
('涣', 1),
('亿', 1),
('芙', 1),
('直', 1),
('塔', 1),
('带', 1),
('淞', 1),
('恩', 1),
('也', 1),
('述', 1),
('蕊', 1),
('沄', 1),
('鹤', 1),
('瑗', 1),
('桤', 1),
('千', 1),
('惟', 1),
('湃', 1),
('日', 1),
('迺', 1),
('骥', 1),
('早', 1),
('拴', 1),
('岗', 1),
('姿', 1),
('妃', 1),
('得', 1),
('淮', 1),
('斐', 1),
('琰', 1),
('骢', 1),
('抒', 1),
('产', 1),
('品', 1),
('凝', 1),
('绪', 1),
('圳', 1),
('誉', 1),
('盾', 1),
('局', 1),
('玥', 1),
('樱', 1),
('堂', 1),
('工', 1),
('濛', 1),
('巧', 1),
('汶', 1),
('羽', 1),
('恬', 1),
('渝', 1),
('聿', 1),
('楷', 1),
('移', 1),
('谆', 1),
('屹', 1),
('情', 1),
('意', 1),
('信', 1),
('栎', 1),
('婵', 1),
('豫', 1),
('众', 1),
('玖', 1),
('觅', 1),
('霄', 1),
('果', 1),
('赫', 1),
('引', 1),
('风', 1),
('碧', 1),
('沐', 1),
('功', 1),
('紫', 1),
('镜', 1),
('珉', 1),
('委', 1),
('澎', 1),
('旎', 1),
('响', 1),
('炯', 1),
('勒', 1),
('炫', 1),
('螣', 1),
('作', 1),
('险', 1),
('佩', 1),
('宪', 1),
('铁', 1),
('备', 1),
('甲', 1),
('歌', 1),
('潼', 1),
('闯', 1),
('斯', 1),
('聚', 1),
('砚', 1),
('财', 1),
('多', 1),
('甦', 1),
('盈', 1),
('侨', 1),
('警', 1),
('快', 1),
('沥', 1),
('颢', 1),
('合', 1),
('议', 1),
('鸥', 1),
('夜', 1),
('坛', 1),
('锴', 1),
('卉', 1),
('珝', 1),
('检', 1),
('珂', 1),
('昉', 1),
('腾', 1),
('骅', 1),
('重', 1),
('仙', 1),
('喆', 1),
('惊', 1),
('娃', 1),
('祯', 1),
('伸', 1),
('嵘', 1),
('铜', 1),
('唯', 1),
('菊', 1),
('莱', 1),
('以', 1),
('廷', 1),
('骑', 1),
('慈', 1),
('总', 1),
('琚', 1),
('泊', 1),
('侠', 1),
('在', 1),
('塽', 1),
('嵩', 1),
('允', 1),
('麒', 1),
('诣', 1),
('赓', 1),
('隽', 1),
('琮', 1),
('献', 1),
('慰', 1),
('途', 1),
('娆', 1),
('骐', 1),
('魁', 1),
('焱', 1),
('州', 1),
('演', 1),
('矗', 1),
('化', 1),
('娣', 1),
('存', 1),
('稷', 1),
('遥', 1),
('荧', 1),
('顺', 1),
('曜', 1),
('津', 1),
('徽', 1),
('介', 1),
('克', 1),
('导', 1),
('铮', 1),
('犇', 1),
('策', 1),
('深', 1),
('若', 1),
('太', 1),
('毓', 1),
('弢', 1),
('霏', 1),
('昀', 1),
('校', 1),
('函', 1),
('跑', 1),
('随', 1),
('焰', 1),
('韬', 1),
('棒', 1),
('臣', 1),
('钊', 1),
('芹', 1),
('厚', 1),
('帝', 1),
('件', 1),
('里', 1),
('业', 1),
('企', 1),
('仑', 1),
('人', 1),
('姝', 1),
('前', 1),
('好', 1),
('遒', 1),
('典', 1),
('沛', 1),
('燏', 1),
('港', 1),
('嫒', 1),
('著', 1),
('丛', 1),
('玄', 1),
('渤', 1),
('仁', 1),
('珲', 1),
('诺', 1),
('晰', 1),
('铧', 1),
('烈', 1),
('滟', 1),
('敦', 1),
('地', 1),
('滢', 1),
('修', 1),
('牮', 1),
('坚', 1),
('烽', 1),
('杏', 1),
('蠓', 1),
('榕', 1),
('沣', 1),
('枭', 1),
('矾', 1),
('旦', 1),
('峻', 1),
('楹', 1),
('榜', 1),
('谦', 1),
('株', 1),
('河', 1),
('号', 1),
('举', 1),
('箭', 1),
('桦', 1),
('谋', 1),
('罡', 1),
('淼', 1),
('壵', 1),
('非', 1),
('端', 1),
('琨', 1),
('勤', 1),
('赐', 1),
('轻', 1),
('靓', 1),
('骋', 1),
('撼', 1),
]

last_names.sort(key=lambda x: x[1])
last_names_choices = list("".join([name[0] * name[1] for name in last_names]))
random.shuffle(last_names_choices)
random.shuffle(last_names_choices)

first_names_choices = list("".join([name[0] * name[1] for name in first_names]))
first_names_choices = first_names_choices * 10
random.shuffle(first_names_choices)
random.shuffle(first_names_choices)


def get_random_name(last_name=None, first_name_length=(1, 2)):
    last_name = last_name or random.choice(last_names_choices) 
    return last_name + "".join(random.choices(first_names_choices, k=random.randint(*first_name_length)))


def get_last_names():
    return [x[0] for x in last_names]

def get_suggest_first_names():
    return [x[0] for x in first_names]


def guess_surname(fullname):
    sns = []
    for sn, _ in last_names:
        if fullname.startswith(sn):
            sns.append(sn)
    final_sn = ""
    for sn in sns:
        if len(sn) > len(final_sn):
            final_sn = sn
    if final_sn:
        return final_sn
    return fullname.split()[-1]
