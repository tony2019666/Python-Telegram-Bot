import ButtonChecker


def onType(object_type):
    match object_type:
        case 'movie':
            return '🎬 电影'
        case 'show':
            return '📺 剧集'
        case 'tv':
            return '📺 剧集'


def onCountry(country):
    list = ButtonChecker.getCountry()
    for i in list:
        if country == i[1]:
            return i[0]
    return '未找到'


def onProviders(providers, id):
    for i in providers:
        if id == i['id']:
            return i['clear_name']


def onOfferType(key):
    match key:
        case 'flatrate':
            keytype = '在线观看🖥（付费）'
        case 'free':
            keytype = '在线观看🖥（免费）'
        case 'ads':
            keytype = '在线观看🖥（广告）'
        case 'buy':
            keytype = '购买方式💵（买断）'
        case 'rent':
            keytype = '购买方式💵（租借）'
    return keytype