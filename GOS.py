import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import branca
import folium
import webbrowser
def get_data(url):
    page=pd.read_html(url,encoding='CP1251')
    header=page[6].drop(12).T
    header=header.iloc[1]
    header[0]='Номер УИК'
    data=page[7].drop(12).T
    data.columns=header
    data.reset_index()
    return data
def plot(x,y,label,j):
    plt.figure()
    x = np.array(x)
    y = np.array(y)
    plt.xlim(2090,2200)
    xmin = min(data.iloc[:, 1])
    xmax = max(data.iloc[:, 1])
    plt.scatter(x,y)
    plt.title('Голоса за ' + label)
url221 = 'http://www.st-petersburg.vybory.izbirkom.ru/region/region/' \
       'st-petersburg?action=show&root=178402912&tvd=27820001217447&vrn=27820001217413&region=' \
       '78&global=&sub_region=78&prver=0&pronetvd=null&vibid=27820001217447&type=222'
data=get_data(url221)
data.iloc[:,0]=[int(i.split()[1][1:]) for i in data.iloc[:,0]]
pd.options.display.max_columns = 100
summ=[]
names=data.columns[12:15]
for j in range(12,15):
    list_pro=[data.iloc[k,j].split(" ")[1] for k in range(len(data.iloc[:,j]))]
    data.insert(3+j,"% голосов за "+names[j-12],list_pro)
list_ya=[float("{:.3f}".format(((int(data.iloc[k,3])+(int(data.iloc[k,4])))/int(data.iloc[k,1]))*100)) for k in range(len(data.iloc[:,1]))]
data.insert(18,"% явки",list_ya)
for j in range(77):
    data.iloc[j, 12:15] = [int(i.split(" ")[0]) for i in data.iloc[j, 12:15]]
data.drop([0,75,76], inplace=True)
geo=[[59.850785,30.379915],[59.855453, 30.389396],[59.855455, 30.388398],[59.851787,30.379917],[59.852275, 30.388083],[59.852277, 30.389085],[59.851279, 30.389087],[59.851281, 30.388089],
     [59.850203, 30.371728],[59.852785,30.378915],[59.850203, 30.371728],[59.848965, 30.378021],[59.847965, 30.378021],[59.848965, 30.379021],[59.844968, 30.385201],[59.841304, 30.379066],
     [59.841304, 30.378066],[59.845968, 30.385201],[59.844968, 30.384201],[59.846964, 30.393131],[59.845964, 30.393131],[59.846964, 30.394131],[59.837017, 30.381480],[59.840264, 30.391581],
     [59.840264, 30.392581],[59.841160,30.399055],[59.841160,30.398055],[59.838017, 30.381480],[59.838017, 30.382480],[59.842160,30.399055],[59.848075, 30.411679],[59.849075, 30.412679],
     [59.848075, 30.411679],[59.849075, 30.412679],[59.847840, 30.412510],[59.847840, 30.413510],[59.840964,30.419247],[59.841964,30.419247],[59.840964,30.418247],[59.836844,30.423048],
     [59.835844,30.423048],[59.836844,30.424048],[59.832583,30.426957],[59.833583,30.426957],[59.831237,30.427819],[59.832237,30.427819],[59.838381, 30.401835],[59.837381, 30.401835],
     [59.835650, 30.396630],[59.834650, 30.396630],[59.835650, 30.395630],[59.833349, 30.385677],[59.832210, 30.408234],[59.833210, 30.408234],[59.832210, 30.418234],[59.831384, 30.402511],
     [59.832384, 30.402511],[59.831384, 30.403511],[59.828972, 30.411498],[59.829972, 30.411498],[59.828972, 30.412498],[59.825741, 30.403766],[59.824741, 30.403766],[59.825741, 30.404766],
     [59.843349, 30.385677],[59.842349, 30.385677],[59.831016, 30.389665],[59.832016, 30.389665],[59.831016, 30.388665],[59.826558, 30.394229],[59.827558, 30.394229],[59.830426, 30.426287],
     [59.847840,30.413510],[59.851314,30.416467]]
data.insert(19,"Координаты",list(geo))
data.to_csv('data.csv')
plot(data.iloc[:, 0], data.iloc[:, 12], 'Амосова',1)
plot(data.iloc[:, 0], data.iloc[:, 13], 'Беглова',2)
plot(data.iloc[:, 0], data.iloc[:, 14], 'Тихонову',3)
plot(data.iloc[:, 0], [float(h[:-1]) for h in data.iloc[:, 15]], 'Амосова в %',1)
plot(data.iloc[:, 0], [float(h[:-1]) for h in data.iloc[:, 16]], 'Беглова в %',2)
plot(data.iloc[:, 0], [float(h[:-1]) for h in data.iloc[:, 17]], 'Тихонову в %',3)
fig, ax = plt.subplots()
width=0.7
ax.bar(list(data.iloc[:, 0]), list(data.iloc[:, 18]), width=width)
fig.set_figwidth(19.2)
fig.set_figheight(6.4)
plt.show()
map = folium.Map(location=[59.839396,30.404847], zoom_start = 13.5)
for i in range(74):
    g=data.iloc[i, 18]
    if g<25:
        col="lightgray"
    elif 25<=g<30:
        col="green"
    elif 30<=g<40:
        col="orange"
    elif g>=40:
        col="red"
    folium.Marker(location=list(data.iloc[i, 19]), popup="УИК №{}\n{}%".format(data.iloc[i, 0],data.iloc[i, 18]), icon=folium.Icon(color = col)).add_to(map)
colormap =  branca.colormap.StepColormap(["lightgray","green","orange","red"],[10,25,30,40,80],10,80,'% явки избирателей от их общего количества').add_to(map)
map.save("map.html")
webbrowser.open("map.html")