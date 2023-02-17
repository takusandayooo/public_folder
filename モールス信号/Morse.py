import json,requests
def inverse_lookup(d, x):
    for k,v in d.items():
        for item in v:
            #print(item)
            if(item==x):
                return k
json_open=open('モールス一覧.json','r')
json_load = json.load(json_open)
collect=int(input("(1,モールス信号→文字:2,文字→モールス信号)"))
sentence=input("文章もしくはモールス信号を入力してください。:")
display=list()
if(collect==1):
    json_loads=json_load['Morse']
    json_load1=json_load["elseMorse1"]
    json_load2=json_load["elseMorse2"]
    lists=sentence.split(" ")
    count=0
    while(len(lists)>count):
        if(len(lists)>count+1):
            if(lists[count+1]==".."or lists[count+1]=="..--."):
                if(lists[count+1]==".."):
                    print(json_load1[lists[count]],end="")
                    count+=2
                else:
                    print(json_load2[lists[count]],end="")
                    count+=2
            else:
                print(json_loads[lists[count]],end="")
                count+=1
        else:
            #print(json_load)
            print(json_loads[lists[count]],end="")
            count+=1
elif(collect==2):
    json_opens=open('モールス一覧2.json','r')
    json_loadss = json.load(json_opens)
    #print(json_loadss)
    json_loads=json_loadss['Morse']
    json_load1=json_loadss["Morseelse"]
    url="https://labs.goo.ne.jp/api/hiragana"
    params={"app_id":"APIのKEY","sentence":sentence,"output_type":"hiragana"}#"https://labs.goo.ne.jp/api/jp/hiragana-translation/"←こちらのAPIを使用した。
    res=requests.post(url,params)
    print(res.json()["converted"])
    lists=res.json()["converted"]
    count=0
    while(len(lists)>count):
        if(inverse_lookup(json_load1, lists[count])!=None):
            print(inverse_lookup(json_load1, lists[count]),end=" ")
            count+=1
        else:
            print(inverse_lookup(json_loads, lists[count]),end=" ")
            count+=1
print("\n")
