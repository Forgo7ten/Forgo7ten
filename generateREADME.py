# coding=utf-8
# @File    : generateREADME.py
# @Desc    : 爬取CSDN和Hexo博客；更新主页README显示
# @Author  : Forgo7ten
# @Time    : 2021/11/22

import re
import time
import requests

my_headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}


def log(msg):
    with open("log.txt", "a+", encoding="utf-8") as logf:
        logf.write(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + msg +
            "\n")


def add_info(f):
    info_txt = """<p align="center" ><img src="https://media.giphy.com/media/l15xvlS8trI0vLQIWb/giphy.gif" width="32px" /><span style="font-size:32px;font-weight:bold">Hi there</span></p>

<p align="center"> <a href="https://github.com/Forgo7ten" target="_blank"> <img src="https://github-readme-stats.vercel.app/api?username=Forgo7ten&show_icons=true&theme=aura&count_private=true" /></a></p>


"""
    f.write(info_txt)


def add_star_info(f):
    f.write("\n### 我的精选文章\n")
    txt = """- [010Editor注册license算法分析](https://forgo7ten.github.io/2021112101/)

- [由2021ByteCTF引出的intent重定向浅析](https://forgo7ten.github.io/2021101701/)

- [vx逆向分析随笔](https://forgo7ten.github.io/2021081401/)

- [Example(0) 今日水印相机自定义水印](https://forgo7ten.github.io/2021081001/)

- ...

"""
    f.write(txt)


def add_other_info(f):
    info_txt = """
## 精选仓库

<a href="https://github.com/Forgo7ten/AndroidReversePractice"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Forgo7ten&repo=AndroidReversePractice&show_owner=true&&theme=aura" /></a><a href="https://github.com/Forgo7ten/GistShow"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Forgo7ten&repo=GistShow&show_owner=true&&theme=aura" /></a>
<a href="https://github.com/Forgo7ten/CTFtools"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Forgo7ten&repo=CTFtools&show_owner=true&&theme=aura" /></a><a href="https://github.com/Forgo7ten/Forgo7ten.github.io"><img src="https://github-readme-stats.vercel.app/api/pin/?username=Forgo7ten&repo=Forgo7ten.github.io&show_owner=true&&theme=aura" /></a>

## 联系我

<p align="center">
<a href="https://forgo7ten.github.io/"><img alt="Website" src="https://img.shields.io/badge/Website-Forgo7ten.github.io-blue?style=flat-square&logo=google-chrome"></a>
<a href="mailto:Forgo7ten2020@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-Forgo7ten2020@gmail.com-blue?style=flat-square&logo=gmail"></a>
</p>
"""
    f.write(info_txt)


def add_csdn_info(f):
    f.write("\n### 我的csdn博客\n")
    csdn_blog_url = "https://blog.csdn.net/Palmer9"
    titles_partten = re.compile(
        r'<div class="blog-list-box-top".*?> *?<h4.*?>(.*?)</h4></div>')
    urls_partten = re.compile(
        r'<article class="blog-list-box" .*?><a href="(.*?)" target=')

    r = requests.get(csdn_blog_url, headers=my_headers)
    if 200 == r.status_code:
        html_text = r.text.replace("\n", " ")
        titles = titles_partten.findall(html_text)
        urls = urls_partten.findall(html_text)
        for i in range(5):
            f.write(f"- [{titles[i]}]({urls[i]})\n")
        log("爬取csdn博客成功！")
    else:
        f.write("Failed!\n")
        log("爬取csdn博客失败！")
    f.write("- ...\n")
    f.write(f"- [查看更多]({csdn_blog_url})\n")


def add_hexo_info(f):
    f.write("\n### 我的hexo博客\n")
    hexo_blog_url = "https://forgo7ten.github.io/atom.xml"
    partten = re.compile(
        r'<entry> *?<title>(.*?)</title> *?<link href="(.*?)"/>')
    r = requests.get(hexo_blog_url, headers=my_headers)
    if 200 == r.status_code:
        html_text = r.text.replace("\n", " ")
        blogs = partten.findall(html_text)
        for i in range(5):
            f.write(f"- [{blogs[i][0]}]({blogs[i][1]})\n")
        log("爬取hexo博客成功！")
    else:
        f.write("Failed!\n")
        log("爬取hexo博客失败！")
    f.write("- ...\n")
    f.write(f"- [查看更多]({hexo_blog_url[:27]})\n")


def main():
    f = open("README.md", "w+", encoding="utf-8")
    add_info(f)
    f.write('<table align="center"><tr>\n')
    f.write('<td valign="top" width="33%">\n')
    add_csdn_info(f)
    f.write('\n</td>\n')
    f.write('<td valign="top" width="33%">\n')
    add_hexo_info(f)
    f.write('\n</td>\n')
    f.write('<td valign="top" width="33%">\n')
    add_star_info(f)
    f.write('\n</td>\n')
    f.write('</tr></table>\n')
    add_other_info(f)
    log("执行完毕！")
    f.close


if __name__ == '__main__':
    main()
