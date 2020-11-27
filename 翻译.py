# coding: gbk
def en_zh(self):
    en = {
        "apple":"ƻ��",
        "apple tree":"ƻ����",
        "milk":"ţ��",
        "egg":"����",
        "colour":"��ɫ",
        "come":"��",
        "hat":"ñ��",
        "one":"һ",
        "two":"��",
        "three":"��",
        "four":"��",
        "five":"��",
        "six":"��",
        "seven":"��",
        "eight":"��",
        "nine":"��",
        "ten":"ʮ",
        "please":"��",
        "sorry":"�Բ���",
        "umbrella":"��ɡ",
        "ticket":"Ʊ",
        "son":"����",
        "daughter":"Ů��",
        "teacher":"��ʦ",
        "upstairs":"��¥��",
        "Chinese":"�й���",
        "good":"�õ�",
        "meet":"����",
        "Mr":"����",
        "your":"��",
        "pen":"�ֱ�",
        "This is an apple.":"����һ��ƻ����",
        "These is apples":"��Щ��ƻ����",
        "a":"һ��",
        "She has an apple and a pear":"����һ��ƻ������",
        "Where is the cinema":"��ӰԺ����",
        "It is next to the bookstore":"����������",
        "Where is the museum shop":"����ݵ��̵����Ķ���",
        "Hello":"���",
        "You are a dog" :"���ǹ�",
        "He finished his homework":"���������ҵ",
        "He is going to take a trip" :"����Ҫȥ����",
        "Before having dinner, he finished all his homework":"���緹֮ǰ������������м�ͥ��ҵ",
        "She is singing":"�����ڳ���",
        "Who is she":"����˭",
        "Hi":"��",
        "What is the matter with them":"������ô��",
        "What is the time":"������",
        "Is that all?":"����Щ��",
        }
    try:
        print(en[self])

    except:
        import http.client
        import hashlib
        import urllib
        import random
        import json

        appid = '20200918000568429' # ��д���appid
        secretKey = 's1L79LVZN7db_nKrzOTT'  # ��д�����Կ

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'en'   #ԭ������
        toLang = 'zh'   #��������
        salt = random.randint(32768, 65536)
        q= self
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response��HTTPResponse����
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
    for i in '.!?������':
        self = self.replace(i,"")
    zh = {
        "ƻ��":"apple",
        "ƻ����":"apple tree",
        "��":"come",
        "ñ��":"hat",
        "����":"egg",
        "һ":"one",
        "��":"two",
        "��":"three",
        "��":"four",
        "��":"five",
        "��":"six",
        "��":"seven",
        "��":"eight",
        "��":"nine",
        "ʮ":"ten",
        "��":"please",
        "�й���":"Chinese",
        "�Բ���":"sorry",
        "�õ�":"good",
        "����":"meet",
        "����":"Mr",
        "��ɡ":"umbrella",
        "����":"son",
        "Ů��":"daughter",
        "Ʊ":"ticket",
        "�ֱ�":"pen",
        "ţ��":"milk",
        "��ɫ":"colour",
        "����һ��ƻ����":"This is an apple.",
        "��Щ��ƻ����":"These is apples",
        "һ��":"a",
        "������":"I missed you",
        "����һ��ƻ������":"She has an apple and a pear",
        "��ӰԺ����":"Where is the cinema?",
        "����������":"It is next to the bookstore",
        '����ݵ��̵����Ķ���':"Where is the museum shop?",
        "���":"Hello",
        "���ǹ�":"You are a dog",
        "���������ҵ":"He finished his homework",
        "���緹֮ǰ������������м�ͥ��ҵ":"Before having dinner, he finished all his homework.",
        "����Ҫȥ����":"He is going to take a trip.",
        "�����ڳ���":"She is singing",
        "���ʲô����":"What is your name?",
        "����˭":"Who is she?",
        "��":"Hi",
        "������ô��":"What is the matter with them",
        "������":"What is the time",
        "����Щ��":"Is that all?",
        "�����ڸ�ʲô":"What are you doing",
        "�㽫Ҫ��ʲô":"What are you going to do",
        "����Ҫ��ʲô":"What do you want to do",
        "�㽫Ҫ��ʲô":"What are you going to buy",
        "��һ����������ϲ��":"Which season do you like best",
        
        }
    try:
        print(zh[self])

    except:
        import http.client
        import hashlib
        import urllib
        import random
        import json

        appid = '20200918000568429' # ��д���appid
        secretKey = 's1L79LVZN7db_nKrzOTT'  # ��д�����Կ

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'zh'   #ԭ������
        toLang = 'en'   #��������
        salt = random.randint(32768, 65536)
        q= self
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response��HTTPResponse����
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            print (result)
            

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()


print('����v1.0')
print('��ѡ������Ӣ��Ӣ����')
take = input()
if take=='����Ӣ':
    print('������Ҫ��������')
    self = input()
    zh_en(self)

if take=='Ӣ����':
    print('������Ҫ��������')
    self = input()
    en_zh(self)


