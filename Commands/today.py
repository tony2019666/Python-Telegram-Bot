import bot
import mapping
import json
import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def onTrending(datatype):
    match datatype:
        case 'today':
            key = bot.tmdb_apikey
            language = 'zh-CN'
            url = f'https://api.themoviedb.org/3/trending/all/day?api_key={key}&language={language}'
            response = json.loads(requests.get(url).text)
            text = f'👇为你送上本日特别推荐：👇'
            keyboard = []
            results = response['results']
            for i in range(10):
                recommend = results[i]
                id = recommend['id']
                object_type = 'movie'
                title = 'title'
                if recommend['media_type'] == 'tv':
                    object_type = 'tv'
                    title = 'name'
                query = recommend[title]
                object_switch = mapping.onType(object_type)
                content = f'#{i+1} -《{query}》{object_switch}'
                button = InlineKeyboardButton(
                    content, callback_data=f'info_{object_type}_{id}_{query}')
                keyboard.append([button])
            reply_markup = InlineKeyboardMarkup(keyboard)
            return text, reply_markup
