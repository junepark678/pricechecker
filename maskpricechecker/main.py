import requests
from pyquery import PyQuery
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk

urls = [
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=16045202761&cat_id=50000246&frm=NVSHATC&query=iphone+xs&NaPm=ct%3Dk7szvu0o%7Cci%3D357fc13a64cb2a175d2f571843927476d257bd51%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D58e570a307e7a0902b86581497b8ab36f5be5f77",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=16044767575&cat_id=50000246&frm=NVSHBRD&query=iphone+xs&NaPm=ct%3Dk7szy0q0%7Cci%3Ddb7c85586c94255695309db905b7da0ad3a374d4%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D57de513217e267c0d94dbb71f21c75b6c87eb900",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=20858302247&cat_id=50001519&frm=NVSHATC&query=iphone&NaPm=ct%3Dk7t1x0a0%7Cci%3Da756743c335eac417fe305c279bf578ab73fa48f%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dc79c6df911b8517ae4fb317e1051a830d05a829a",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=20858389068&cat_id=50001519&frm=NVSHATC&query=iphone&NaPm=ct%3Dk7t1yrjs%7Cci%3Df23bf974dcae12a1168e37dd92f0ccdf6d379a5a%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Db52dccd2920bdec124c99e7bd1fefc676b166506",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=20858385412&cat_id=50000246&frm=NVSHCAT&query=iPhone+11&NaPm=ct%3Dk7t1zyrc%7Cci%3D22bd9bb6500c098c360a601afabe9eb2f7d48813%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D51e58d5f1a930f479c10b87e764bd0a48a4fd486",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=20858274127&cat_id=50000246&frm=NVSHCAT&query=iPhone+11&NaPm=ct%3Dk7t20mog%7Cci%3Db195db67e59fe7139a8935518013918a3383a721%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D5d6a402f1099b2ea112669e033b7f1df706d729a",
    "https://search.shopping.naver.com/detail/detail.nhn?nv_mid=20858558236&cat_id=50000246&frm=NVSHCAT&query=iPhone+11&NaPm=ct%3Dk7t2apc0%7Cci%3Dd7cf1b84186329a82eeb1ba71bd2f81e63f26466%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D6a315339200f8576c9ffdb9eb3d3e4fbb8975932",

        ]
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15'}

tk = Tk()

tk.title("price tracker")
tree = ttk.Treeview(tk)
tree.pack()
tree['columns'] = ('price')
tree.heading('#0', text="name")
tree.heading('price', text="price")

urlid = 0

for x in urls:
    page = requests.get(x, headers=headers)
    soup = PyQuery(page.content)
    soup2 = BeautifulSoup(page.content, features="lxml")
    title = soup2.select_one("div.h_area").get_text()
    price = soup2.select_one('em.num').get_text()
    sprice = price.strip()+"원"
    stitle = title.strip()
    print(stitle)
    print(sprice)
    tree.insert('', 'end', str(urlid), text=stitle)
    tree.set(str(urlid), 'price', sprice)
    urlid += 1



tk.mainloop()