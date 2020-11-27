# coding: gbk
def en_zh(self):
    en = {
        "apple":"苹果",
        "apple tree":"苹果树",
        "milk":"牛奶",
        "egg":"鸡蛋",
        "colour":"颜色",
        "come":"来",
        "hat":"帽子",
        "one":"一",
        "two":"二",
        "three":"三",
        "four":"四",
        "five":"五",
        "six":"六",
        "seven":"七",
        "eight":"八",
        "nine":"九",
        "ten":"十",
        "please":"请",
        "sorry":"对不起",
        "umbrella":"雨伞",
        "ticket":"票",
        "son":"儿子",
        "daughter":"女儿",
        "teacher":"老师",
        "upstairs":"在楼上",
        "Chinese":"中国人",
        "good":"好的",
        "meet":"遇见",
        "Mr":"先生",
        "your":"你",
        "pen":"钢笔",
        "This is an apple.":"这是一个苹果。",
        "These is apples":"这些是苹果。",
        "a":"一个",
        "She has an apple and a pear":"她有一个苹果和梨",
        "Where is the cinema":"电影院在哪",
        "It is next to the bookstore":"它在书店隔壁",
        "Where is the museum shop":"博物馆的商店在哪儿？",
        "Hello":"你好",
        "You are a dog" :"你是狗",
        "He finished his homework":"他完成了作业",
        "He is going to take a trip" :"他将要去旅行",
        "Before having dinner, he finished all his homework":"吃午饭之前，他完成了所有家庭作业",
        "She is singing":"她正在唱歌",
        "Who is she":"她是谁",
        "Hi":"嗨",
        "What is the matter with them":"他们怎么啦",
        "What is the time":"几点钟",
        "Is that all?":"就这些吗",
        }
    try:
        print(en[self])

    except:
        import http.client
        import hashlib
        import urllib
        import random
        import json

        appid = '20200918000568429' # 填写你的appid
        secretKey = 's1L79LVZN7db_nKrzOTT'  # 填写你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'en'   #原文语种
        toLang = 'zh'   #译文语种
        salt = random.randint(32768, 65536)
        q= self
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            print (result)

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()



# coding: gbk
def zh_en(self):
    for i in '.!?。？！':
        self = self.replace(i,"")
    zh = {
        "苹果":"apple",
        "苹果树":"apple tree",
        "来":"come",
        "帽子":"hat",
        "鸡蛋":"egg",
        "一":"one",
        "二":"two",
        "三":"three",
        "四":"four",
        "五":"five",
        "六":"six",
        "七":"seven",
        "八":"eight",
        "九":"nine",
        "十":"ten",
        "请":"please",
        "中国人":"Chinese",
        "对不起":"sorry",
        "好的":"good",
        "遇见":"meet",
        "先生":"Mr",
        "雨伞":"umbrella",
        "儿子":"son",
        "女儿":"daughter",
        "票":"ticket",
        "钢笔":"pen",
        "牛奶":"milk",
        "颜色":"colour",
        "这是一个苹果。":"This is an apple.",
        "这些是苹果。":"These is apples",
        "一个":"a",
        "我想你":"I missed you",
        "她有一个苹果和梨":"She has an apple and a pear",
        "电影院在哪":"Where is the cinema?",
        "它在书店隔壁":"It is next to the bookstore",
        '博物馆的商店在哪儿？':"Where is the museum shop?",
        "你好":"Hello",
        "你是狗":"You are a dog",
        "他完成了作业":"He finished his homework",
        "吃午饭之前，他完成了所有家庭作业":"Before having dinner, he finished all his homework.",
        "他将要去旅行":"He is going to take a trip.",
        "她正在唱歌":"She is singing",
        "你叫什么名字":"What is your name?",
        "她是谁":"Who is she?",
        "嗨":"Hi",
        "他们怎么啦":"What is the matter with them",
        "几点钟":"What is the time",
        "就这些吗":"Is that all?",
        "你正在干什么":"What are you doing",
        "你将要干什么":"What are you going to do",
        "你想要干什么":"What do you want to do",
        "你将要买什么":"What are you going to buy",
        "那一个季节你最喜欢":"Which season do you like best",
        
        }
    try:
        print(zh[self])

    except:
        import http.client
        import hashlib
        import urllib
        import random
        import json

        appid = '20200918000568429' # 填写你的appid
        secretKey = 's1L79LVZN7db_nKrzOTT'  # 填写你的密钥

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'zh'   #原文语种
        toLang = 'en'   #译文语种
        salt = random.randint(32768, 65536)
        q= self
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            print (result)
            

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()


print('翻译v1.0')
print('请选择中译英或英译中')
take = input()
if take=='中译英':
    print('请输入要翻译的语句')
    self = input()
    zh_en(self)

if take=='英译中':
    print('请输入要翻译的语句')
    self = input()
    en_zh(self)


