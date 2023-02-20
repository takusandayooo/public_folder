import tkinter as tk
import tkinter.ttk as ttk
import json,requests,time
from playsound import playsound

def inverse_lookup(d, x):
    for k,v in d.items():
        for item in v:
            #print(item)
            if(item==x):
                return k
def push1():
    json_open=open('モールス一覧.json','r')
    json_load = json.load(json_open)
    sentence = entry2.get()
    prints=list()
    
    json_opens=open('モールス一覧2.json','r')
    json_loadss = json.load(json_opens)
    #print(json_loadss)
    json_loads=json_loadss['Morse']
    json_load1=json_loadss["Morseelse"]
    url="https://labs.goo.ne.jp/api/hiragana"
    params={"app_id":"APIのKEY","sentence":sentence,"output_type":"hiragana"}
    res=requests.post(url,params)
    print(res.json()["converted"])
    lists=res.json()["converted"]
    count=0
    while(len(lists)>count):
        if(inverse_lookup(json_load1, lists[count])!=None):
            a=str(inverse_lookup(json_load1, lists[count]))
            #print(a,end=" ")
            prints.append(a)
            count+=1
        else:
            a=str(inverse_lookup(json_loads, lists[count]))
            #print(a,end=" ")
            prints.append(a)
            count+=1
    result =" ".join(prints)
    print(result,)
    entry3.delete(0, tk.END)
    entry3.insert(0, result)
    for x in prints:
        for t in x:
            if(t=="-"):
                playsound("(-).mp3")
            elif(t=="."):
                playsound("(.).mp3")
            else:
                time.sleep(0.1)    
def push2():
    display=list()
    json_open=open('モールス一覧.json','r')
    json_load = json.load(json_open)
    json_loads=json_load['Morse']
    json_load1=json_load["elseMorse1"]
    json_load2=json_load["elseMorse2"]
    sentence = entry3.get()
    lists=sentence.split(" ")
    count=0
    while(len(lists)>count):
        if(len(lists)>count+1):
            if(lists[count+1]==".."or lists[count+1]=="..--."):
                if(lists[count+1]==".."):
                    print(json_load1[lists[count]],end="")
                    display.append(str(json_load1[lists[count]]))
                    count+=2
                else:
                    print(json_load2[lists[count]],end="")
                    display.append(str(json_load2[lists[count]]))
                    count+=2
            else:
                print(json_loads[lists[count]],end="")
                display.append(str(json_loads[lists[count]]))
                count+=1
        else:
            #print(json_load)
            print(json_loads[lists[count]],end="")
            display.append(json_loads[lists[count]])
            count+=1
    result ="".join(display)
    print(result)
    entry2.delete(0, tk.END)
    entry2.insert(0, result)

root = tk.Tk()
root.title("モールス信号")
root.geometry("1000x500")
frame1 = tk.Frame(root)
frame1.pack(pady=20)
title = tk.Label(frame1, text="モールス信号変換機！！", font=('Times New Roman',20))
title.pack()
border = ttk.Separator(root, orient="horizontal")
border.pack(fill="both", pady=2)
####
frame2 = tk.Frame(root, height=100, width=15)
frame2.pack(padx=40, pady=10, fill=tk.BOTH)
subtitle2 = tk.Label(frame2, text="文章", font=('Times New Roman',20), anchor=tk.SW)
subtitle2.pack(side=tk.LEFT, padx=30)
entry2 = tk.Entry(frame2, width=100)
entry2.pack(anchor=tk.SW, padx=5)
button2 = tk.Button(frame2, height=2, width=10,text="文章→モールス信号",command=push1)
button2.pack(side=tk.RIGHT, padx=5)
#####
frame3 = tk.Frame(root, height=100, width=15)
frame3.pack(padx=40, pady=10, fill=tk.BOTH)
subtitle3 = tk.Label(frame3, text="モールス信号", font=('Times New Roman',20), anchor=tk.SW)
subtitle3.pack(side=tk.LEFT, padx=3)
entry3 = tk.Entry(frame3, width=100)
entry3.pack(anchor=tk.SW, padx=5)
button3 = tk.Button(frame3, height=2, width=10,text="モールス信号→文章",command=push2)
button3.pack(side=tk.RIGHT, padx=5)
root.mainloop()
