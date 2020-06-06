# -*- coding: utf-8 -*-
"""
Created on Sun May 31 18:01:13 2020

@author: takashi.shiozawa
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)#等差数列生成

fig = plt.figure()
plt.plot(x,np.sin(x),"-")
plt.plot(x,np.cos(x),"--")

fig.savefig("sin,cos.png")#画像として保存

fig,ax = plt.subplots(2)#subplots(何行、何列、何番目)
ax[0].plot(x,np.sin(x))#0行目に作図
ax[1].plot(x,np.cos(x))#1行目に作図

#作図環境の生成
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x))

#外観の調整⓵
plt.plot(x,np.sin(x-0),color="blue")#名前で指定
plt.plot(x,np.sin(x-1),color="k")#カラーコード(rgbcmyk)で指定
plt.plot(x,np.sin(x-2),color="0b.75")#0から1のグレースケールで指定

#外観の調整⓶
plt.plot(x,x+0,linestyle="solid")#直線
plt.plot(x,x+1,linestyle="dashed")#点線
plt.plot(x,x+2,linestyle="dashdot")#点線と点
plt.plot(x,x+3,linestyle="dotted")#点

plt.plot(x,x+4,linestyle="-")#solid
plt.plot(x,x+5,linestyle="--")#dashed
plt.plot(x,x+6,linestyle="-.")#dashdot
plt.plot(x,x+7,linestyle=":")#dotted

#カラーコードと線のタイプはひとまとめにも可能
plt.plot(x,x+4,"-r")#solid
plt.plot(x,x+5,"--g")#dashed
plt.plot(x,x+6,"-.b")#dashdot
plt.plot(x,x+7,":y")#dotted

#軸の範囲指定
plt.plot(x,np.sin(x))

plt.xlim(-1,11)
plt.ylim(-1.5,1.5)

#引数を逆にすると逆の順序になる
plt.plot(x,np.sin(x))

plt.xlim(11,-1)
plt.ylim(1.5,-1.5)

#plt.axisの利用
plt.plot(x,np.sin(x))
plt.axis([-1,11,-1.5,1.5])

plt.plot(x,np.sin(x))
plt.axis("tight")#周辺の境界を自動で狭くする

plt.plot(x,np.sin(x))
plt.axis("equal")#ｘとｙの比率を固定

#ラベル付け
plt.plot(x,np.sin(x))
plt.title("A sine curve")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.plot(x,np.sin(x),"-g",label="sin(x)")
plt.plot(x,np.cos(x),"--r",label="cos(x)")

plt.legend()

"""plt methodとax methodの互換性
plt.xlabel();ax.set_xlabel()
plt.ylabel();ax.set_ylabel()
plt.xlim();ax.set_xlim()
plt.ylim();ax.set_ylim()
plt.title();ax.set_title()
"""

ax = plt.axes()
ax.plot(x,np.sin(x))
ax.set(xlim=(0,10),ylim=(-2,2),xlabel="x",ylabel="sin(x)",
       title="A Simple Plot")

#散布図
x = np.linspace(0,10,30)#0から10まで30個の等差数列
y = np.sin(x)

plt.plot(x,y,"o",color="red")
plt.plot(x,y,"o",color="r")

rng = np.random.RandomState(0)
for marker in ["o",".",",","x","+","v","^","<",">","s","d"]:
    plt.plot(rng.rand(5),rng.rand(5),marker,
         label="marker='{}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0,1.8)

"""format関数
apple  = 50
orange = 100
total = apple + orange

print('合計：{}円'.format(total))

apple  = 50
orange = 100
total = apple + orange

print('りんご：{0}円 みかん：{1}円 合計：{2}円'.format(apple, orange, total))

apple  = 50
orange = 100
total = apple + orange

list = [apple, orange, total]  #リストの作成

print('りんご：{0[0]}円 みかん：{0[1]}円 合計：{0[2]}円'.format(list))

上記のように変数の文字列の埋め込みの際に用いられる"""


#散布図でマーカーと線と色を一括で決める
plt.plot(x,y,"-ok")#直線の円マーカーの黒

#引数の指定
plt.plot(x,y,"-p",color="gray",#直線の五角形
         markersize=15,linewidth=4,
         markerfacecolor="white",
         markeredgecolor="gray",#マーカーの輪郭の色
         markeredgewidth=2)#マーカーの輪郭のサイズ
plt.ylim(-1.2,1.2)

rng = np.random.RandomState(0)
x = rng.randn(100)#randnは標準正規分布（平均0、標準偏差1）の分布
y = rng.randn(100)
color = rng.rand(100)#randは0~1からランダム
sizes = 1000*rng.rand(100)


plt.scatter(x,y,c=color,s=sizes,alpha=0.3,
            cmap="viridis")
plt.colorbar()
""""plt.plotではcolor,sizeは1つの値しか取れない
一方でplt.scatterは複数の値をとれる"""

#irisデータの読み込み
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0],features[1],alpha=0.2,
            s=100*features[3],c=iris.target,cmap="viridis")
"x軸；がくの長さ、y軸；がくの幅、サイズ；花びらの幅書ける100、色；種類"
"大きなデータセットではplt.scatterよりもplt.plotの方が効率がよい(一括で体裁を整えられるから）"

#誤差の可視化(エラーバーについて)
x = np.linspace(0,10,50)
dy = 0.8
y = np.sin(x)+dy*np.random.randn(50)

plt.errorbar(x, y, yerr=dy,fmt=".k")#yerr；エラーの大きさ、fmt；点の形と色、黒の点
plt.errorbar(x, y, yerr=dy,fmt="or")#yerr；エラーの大きさ、fmt；点の形と色、赤の円
plt.errorbar(x, y, yerr=dy,fmt="pk")#yerr；エラーの大きさ、fmt；点の形と色、黒の五角形

#見た目の調整
plt.errorbar(x, y, yerr=dy,fmt="ok",ecolor="lightgray",
             elinewidth=3,capsize=5)#capsize；末端の線の長さ







































































































