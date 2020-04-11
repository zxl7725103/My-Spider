# ！/usr/bin/env python
# -*-coding:utf-8-*-
"""
@Author  : zhangxiaoliang
@Time    : 2020/04/05 11:50
@Desc : wixin Video downloading
@Project : python_appliction
@FileName: you-get2.py
@Software: PyCharm
@Blog    ：
tkinter的使用，you-get的调用
"""

import re
import sys
import tkinter as tk
import tkinter.messagebox as msgbox
import webbrowser
import requests
import you_get
from tkinter.filedialog import askdirectory

import subprocess as sub
import threading

"""
视频下载类
"""


class DownloadApp:
    # construct
    def __init__(self, width=800, height=200):
        self.w = width
        self.h = height
        self.title = '微信视频下载助手'
        self.root = tk.Tk (className=self.title)
        self.url = tk.StringVar ()
        self.start = tk.IntVar ()
        self.end = tk.IntVar ()
        self.path = tk.StringVar ()
        self.path.set ('D:/DownloadApp')
        self.name=tk.StringVar ()

        # define frame
        frame_1 = tk.Frame (self.root)
        frame_2 = tk.Frame (self.root)
        frame_3 = tk.Frame (self.root)
        frame_4 = tk.Frame (self.root)

        # menu
        menu = tk.Menu (self.root)
        self.root.config (menu=menu)
        menu1 = tk.Menu (menu, tearoff=0)
        menu.add_cascade (label='菜单', menu=menu1)
        #menu1.add_command (label='about me', command=lambda: webbrowser.open ('https://blog.csdn.net/zxl7725103'))
        menu1.add_command (label='退出', command=lambda: self.root.quit ())

        # set frame_1
        label1 = tk.Label (frame_1, text='请输入微信文章链接：')
        entry_url = tk.Entry (frame_1, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        Get_url = tk.Button (frame_1, text='下载链接解析', font=('楷体', 12), fg='green', width=15, height=-1,
                          command=self.video_url)
        CLS = tk.Button (frame_1, text='清除链接', font=('楷体', 12), fg='green', width=8, height=-1,
                             command=self.CLS)

        # set frame_2
        s_lable = tk.Label (frame_2, text='视频解析是否成功：')
        e_lable = tk.Label (frame_2, textvariable=self.name)  #Label名称的可变性
        #e_lable = tk.Label (frame_2, text='结束值：')
        #start = tk.Entry (frame_2, textvariable=self.start, highlightcolor='Fuchsia', highlightthickness=1, width=10)
        #end = tk.Entry (frame_2, textvariable=self.end, highlightcolor='Fuchsia', highlightthickness=1, width=10)

        # set frame_3
        label2 = tk.Label (frame_3, text='请输入视频输出地址：')
        entry_path = tk.Entry (frame_3, textvariable=self.path, highlightcolor='Fuchsia', highlightthickness=1,
                               width=35)

        down_path = tk.Button (frame_3, text='选择保存目录', font=('楷体', 12), fg='green', width=8, height=-1,
                          command=self.down_path)
        #down = tk.Button (frame_3, text='下载', font=('楷体', 12), fg='green', width=3, height=-1,
                          #command=self.video_download)
        down = tk.Button (frame_3, text='下载', font=('楷体', 12), fg='green', width=3, height=-1,
                           command=lambda :thread_it(self.video_download))  #下载采用多线程
        # set frame_4
        label_desc = tk.Label (frame_4, fg='black', font=('楷体', 8),height=3,
                               text='\n注意：支持微信公众号内视频的下载！步骤：1、粘贴含视频的微信公众号地址，点击下载链接解析，2、选择保存目录后，点击下载')
        label_warning = tk.Label (frame_4, fg='blue', font=('楷体', 12), text='\nauthor:MoYing')

        # layout
        frame_1.pack ()
        frame_2.pack ()
        frame_3.pack ()
        frame_4.pack ()

        label1.grid (row=0, column=0)
        entry_url.grid (row=0, column=1)
        Get_url.grid(row=0, column=2)
        CLS.grid (row=0, column=3)

        s_lable.grid (row=1, column=0)
        #start.grid (row=1, column=1)
        e_lable.grid (row=1, column=1)
        #end.grid (row=1, column=3)

        label2.grid (row=2, column=0)
        entry_path.grid (row=2, column=1)
        down_path.grid (row=2, column=2, ipadx=20)
        down.grid (row=2, column=3, ipadx=20)

        label_desc.grid (row=3, column=0)
        label_warning.grid (row=4, column=0)

    """
    视频下载
    """
    def CLS(self):
        self.url.set (" ")
    def down_path(self):
        p=askdirectory()
        print(p)
        self.path.set(p+'/')

    def video_url(self):

        cookies = {
            'rewardsn': '',
            'wxtokenkey': '777',
            'tvfe_boss_uuid': '14bc09a5142c8ace',
            'pgv_pvid': '4700131718',
            'pgv_info': 'ssid=s2087229496',
        }

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36 Edg/79.0.309.68',
            'Sec-Fetch-User': '?1',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-Mode': 'navigate',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'If-Modified-Since': 'Sat, 4 Apr 2020 18:41:31 +0800',
        }

        params = (
            ('__biz', 'MjM5MTQ1MjYxNw=='),
            ('mid', '2649823639'),
            ('idx', '1'),
            ('sn', '576e987c34c5ae91bb748f2aad9a658c'),
            ('chksm', 'beb0e53189c76c27074069681155cf2ce1ac91dfe785bcd54e159ea70aae8ec0b7f13ab91566'),
            ('scene', '21'),
        )
        url = "https://mp.weixin.qq.com/s?__biz=MjM5MTQ1MjYxNw==&mid=2649823639&idx=1&sn=576e987c34c5ae91bb748f2aad9a658c&chksm=beb0e53189c76c27074069681155cf2ce1ac91dfe785bcd54e159ea70aae8ec0b7f13ab91566&scene=21#wechat_redirect"
        # url="https://mp.weixin.qq.com/s?__biz=MjM5MTQ1MjYxNw==&mid=2649822010&idx=2&sn=b483640475dbb54618a12edc292f1da7&chksm=beb0ef9c89c7668af5cea2176a8dedb14efa6a5ce49850cb15e05976dba8cbfc4896fd9f096e&scene=21#wechat_redirect"
        # url="https://mp.weixin.qq.com/s?__biz=MjM5MTQ1MjY理》教学视xNw==&mid=2649822170&idx=2&sn=b9626e6784128d89625ac67ca792f2b0&chksm=beb0ef7c89c7666a86b2c4e83e0cae97294da544bec6c896a19032accdcd41199f18c26baa36&scene=21#wechat_redirect"

        try:
            url = self.url.get ()
            response = requests.get (url, headers=headers)
            #response.text
            #id = re.findall (r'vid=(.*?)"></iframe>', response.text)
            id = re.findall (r'vid=(.{11})', response.text)
            print(id)
            if id==[] :
                id=re.findall(r'source_link : "http://v.qq.com/x/page/(.*?).html',response.text)
            self.Video_url = "https://v.qq.com/x/page/" + id[0] + ".html"
            self.Video_name = (re.findall (r'<meta property="twitter:title" content="(.*?)" />', response.text))[0]
            print (self.Video_name)
            if "|" in self.Video_name:  #字符"|"无法生产文件名
                self.Video_name=(self.Video_name.split("|"))[0]
                print(self.Video_name)
            self.name.set("解析成功,视频名称为："+self.Video_name+"---请选择目录后，进行下载。")
            print(self.Video_name,self.Video_url)
        except:
            self.name.set ("解析失败，无法下载")
            pass
    def video_download(self):
        # 正则表达是判定是否为合法链接
        #url = self.Video_url
        #name=self.Video_name
        path = self.path.get ()
        if re.match (r'^https?:/{2}\w.+$', self.Video_url):
            if path != '':
                msgbox.showwarning (title='警告', message='下载过程中窗口如果出现短暂卡顿说明文件正在下载中！')
                try:
                    #sys.argv = ['you-get', '-o', path, self.Video_url,'-O',self.Video_name]
                    #you_get.main ()
                    cmd = f'you-get -o {path} {self.Video_url} -O {self.Video_name}'  #后台调用cmd
                    p = sub.Popen (cmd, stdout=sub.PIPE, stderr=sub.PIPE)
                    output, errors = p.communicate()
                    output = output.decode ('UTF-8')
                    print (cmd)
                except Exception as e:
                    print (e)
                    msgbox.showerror (title='error', message=e)
                msgbox.showinfo (title='info', message='下载完成！')
            else:
                msgbox.showerror (title='error', message='输出地址错误！')
        else:
            msgbox.showerror (title='error', message='视频地址错误！')

    def center(self):
        ws = self.root.winfo_screenwidth ()
        hs = self.root.winfo_screenheight ()
        x = int ((ws / 2) - (self.w / 2))
        y = int ((hs / 2) - (self.h / 2))
        self.root.geometry ('{}x{}+{}+{}'.format (self.w, self.h, x, y))

    def event(self):
        self.root.resizable (False, False)
        self.center ()
        self.root.mainloop ()


# 为避免在下载时tkinter界面卡死，创建线程函数
def thread_it(func, *args):
    # 创建
    t = threading.Thread (target=func, args=args)
    # 守护 !!!
    t.setDaemon (True)
    # 启动
    t.start ()


if __name__ == '__main__':
    app = DownloadApp ()
    app.event ()