# TMDB w/ Justwatch Telegram Bot via Python

我的第一个 Python 项目，学习&了解 Python 中～
如果觉得麻烦可以使用现成项目：[https://t.me/dyjw_bot](https://t.me/dyjw_bot)

Python 版本需求 >= 3.10 因为用到了match函数

## 如何使用

```
git clone https://github.com/Mayomi/Python-Telegram-Bot.git
cd Python-Telegram-Bot
pip install -r requirements.txt
nano bot.py
# 编辑 line 10 及 line 12 为对应的Token&Key
python3 bot.py
```

## 申请 Telegram Bot Token

1. 私聊 [https://t.me/BotFather](https://https://t.me/BotFather)
2. 输入 `/newbot`，并为你的bot起一个**响亮**的名字
3. 接着为你的bot设置一个username，但是一定要以bot结尾，例如：`dyjw_bot`
4. 最后你就能得到bot的token了，看起来应该像这样：`5043403136:AAHcEXY0Hu-qplH5my5nrfHg5nQU-p8zH6w`

## 申请 TheMovieDB APIKey

1. 前往：[https://developers.themoviedb.org/3/getting-started/introduction](https://developers.themoviedb.org/3/getting-started/introduction)，并注册一个账号
2. 然后根据指引完成APIKey的注册

## 感谢非常棒的开源项目让我学习

[python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
[dawoudt/JustWatchAPI](https://github.com/dawoudt/JustWatchAPI)
[celiao/tmdbsimple](https://github.com/celiao/tmdbsimple/)
