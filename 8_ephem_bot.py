import logging
import string
import ephem
import settings
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime, date


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


# PROXY = {
#     'proxy_url': settings.PROXY_URL',
#     'urllib3_proxy_kwargs': {
#     'username': settings.PROXY_USERNAME,
#     'password': settings.PROXY_PASSWORD
#     }
# }


def greet_user(update, context):
    update.message.reply_text('Вызван /start')


def talk_to_me(update, context):
    update.message.reply_text(update.message.text)


def constel(update, context):

    planet_key: str = update.message.text.lower().split()[-1]

    planets: dict = {
            'mercury': ephem.Mercury,
            'venus': ephem.Venus,
            'moon': ephem.Moon,
            'sun': ephem.Sun,
            'mars': ephem.Mars,
            'jupiter': ephem.Jupiter,
            'saturn': ephem.Saturn,
            'uranus': ephem.Uranus,
            'neptune': ephem.Neptune,
            'pluto': ephem.Pluto,
            'меркурий': ephem.Mercury,
            'венера': ephem.Venus,
            'луна': ephem.Moon,
            'солнце': ephem.Sun,
            'марс': ephem.Mars,
            'юпитер': ephem.Jupiter,
            'сатурн': ephem.Saturn,
            'уран': ephem.Uranus,
            'нептун': ephem.Neptune,
            'плутон': ephem.Pluto,
        }

    position = planets[planet_key](datetime.today().strftime('%Y/%m/%d'))
    const = ephem.constellation(position)[1]
    update.message.reply_text(f'{planet_key.title()} is in {const} today.')


def word_counter(update, context):

    res: str = ''

    for i in update.message.text:
        if i in string.punctuation:
            res += ' '
        else:
            res += i

    message_length: int = len(res.split()) - 1

    if message_length < 1:
        update.message.reply_text("Недостаточно слов для подсчета, введите текст: ")
    else:
        if message_length in range(11, 21) or str(message_length)[-1] in '056789':
            update.message.reply_text(f"{message_length} слов")
        elif str(message_length)[-1] == '1':
            update.message.reply_text(f"{message_length} слово")
        else:
            update.message.reply_text(f"{message_length} слова")


def next_full_moon(update, context):
    user_text: str = ' '.join(update.message.text.strip().split()[1:])
    if user_text == '':
        nfm = ephem.next_full_moon(datetime.today())
        update.message.reply_text(f"Ближайшее полнолуние {nfm}")
    else:
        try:
            date_moon: datetime.date = date.fromisoformat(user_text)
            nfm: ephem.Date = ephem.next_full_moon(date_moon)
            answer: str = f"Ближайшее полнолуние от даты {date_moon} - {nfm}"

        except ValueError as ve:
            print(ve)
            answer: str = f"Введите дату в формате ГГГГ-ММ-ДД"
        return update.message.reply_text(answer)


def city_game(update, context):
    user_text: str = update.message.text[8:].strip().lower()
    game_lst: list = [
        'абаза', 'абакан', 'абдулино', 'абинск', 'агидель', 'агрыз', 'адыгейск', 'азнакаево', 'азов', 'ак-довурак', 'аксай', 'алагир', 'алапаевск', 'алатырь', 'алдан', 'алейск', 'александров', 'александровск', 'александровск-сахалинский', 'алексеевка', 'алексин', 'алзамай', 'алупка', 'алушта', 'альметьевск', 'амурск', 'анадырь', 'анапа', 'ангарск', 'андреаполь', 'анжеро-судженск', 'анива', 'апатиты', 'апрелевка', 'апшеронск', 'арамиль', 'аргун', 'ардатов', 'ардон', 'арзамас', 'аркадак', 'армавир', 'армянск', 'арсеньев', 'арск', 'артём', 'артёмовск', 'артёмовский', 'архангельск', 'асбест', 'асино', 'астрахань', 'аткарск', 'ахтубинск', 'ачинск', 'аша',
        'бабаево', 'бабушкин', 'бавлы', 'багратионовск', 'байкальск', 'баймак', 'бакал', 'баксан', 'балабаново', 'балаково', 'балахна', 'балашиха', 'балашов', 'балей', 'балтийск', 'барабинск', 'барнаул', 'барыш', 'батайск', 'бахчисарай', 'бежецк', 'белая калитва', 'белая холуница', 'белгород', 'белебей', 'белинский', 'белово', 'белогорск', 'белозерск', 'белокуриха', 'беломорск', 'белорецк', 'белореченск', 'белоусово', 'белоярский', 'белый', 'белёв', 'бердск', 'березники', 'берёзовский', 'беслан', 'бийск', 'бикин', 'билибино', 'биробиджан', 'бирск', 'бирюсинск', 'бирюч', 'благовещенск', 'благодарный', 'бобров', 'богданович', 'богородицк', 'богородск', 'боготол', 'богучар', 'бодайбо', 'бокситогорск', 'болгар', 'бологое', 'болотное', 'болохово', 'болхов', 'большой камень', 'бор', 'борзя', 'борисоглебск', 'боровичи', 'боровск', 'бородино', 'братск', 'бронницы', 'брянск', 'бугульма', 'бугуруслан', 'будённовск', 'бузулук', 'буинск', 'буй', 'буйнакск', 'бутурлиновка',
        'валдай', 'валуйки', 'велиж', 'великие луки', 'великий новгород', 'великий устюг', 'вельск', 'венёв', 'верещагино', 'верея', 'верхнеуральск', 'верхний тагил', 'верхний уфалей', 'верхняя пышма', 'верхняя салда', 'верхняя тура', 'верхотурье', 'верхоянск', 'весьегонск', 'ветлуга', 'видное', 'вилюйск', 'вилючинск', 'вихоревка', 'вичуга', 'владивосток', 'владикавказ', 'владимир', 'волгоград', 'волгодонск', 'волгореченск', 'волжск', 'волжский', 'вологда', 'володарск', 'волоколамск', 'волосово', 'волхов', 'волчанск', 'вольск', 'воркута', 'воронеж', 'ворсма', 'воскресенск', 'воткинск', 'всеволожск', 'вуктыл', 'выборг', 'выкса', 'высоковск', 'высоцк', 'вытегра', 'вышний волочёк', 'вяземский', 'вязники', 'вязьма', 'вятские поляны',
        'гаврилов посад', 'гаврилов-ям', 'гагарин', 'гаджиево', 'гай', 'галич', 'гатчина', 'гвардейск', 'гдов', 'геленджик', 'георгиевск', 'глазов', 'голицыно', 'горбатов', 'горно-алтайск', 'горнозаводск', 'горняк', 'городец', 'городище', 'городовиковск', 'гороховец', 'горячий ключ', 'грайворон', 'гремячинск', 'грозный', 'грязи', 'грязовец', 'губаха', 'губкин', 'губкинский', 'гудермес', 'гуково', 'гулькевичи', 'гурьевск', 'гусев', 'гусиноозёрск', 'гусь-хрустальный',
        'давлеканово', 'дагестанские огни', 'далматово', 'дальнегорск', 'дальнереченск', 'данилов', 'данков', 'дегтярск', 'дедовск', 'демидов', 'дербент', 'десногорск', 'джанкой', 'дзержинск', 'дзержинский', 'дивногорск', 'дигора', 'димитровград', 'дмитриев', 'дмитров', 'дмитровск', 'дно', 'добрянка', 'долгопрудный', 'долинск', 'домодедово', 'донецк', 'донской', 'дорогобуж', 'дрезна', 'дубна', 'дубовка', 'дудинка', 'духовщина', 'дюртюли', 'дятьково',
        'евпатория', 'егорьевск', 'ейск', 'екатеринбург', 'елабуга', 'елец', 'елизово', 'ельня', 'еманжелинск', 'емва', 'енисейск', 'ермолино', 'ершов', 'ессентуки', 'ефремов',
        'железноводск', 'железногорск', 'железногорск-илимский', 'жердевка', 'жигулёвск', 'жиздра', 'жирновск', 'жуков', 'жуковка', 'жуковский',
        'завитинск', 'заводоуковск', 'заволжск', 'заволжье', 'задонск', 'заинск', 'закаменск', 'заозёрный', 'заозёрск', 'западная двина', 'заполярный', 'зарайск', 'заречный', 'заринск', 'звенигово', 'звенигород', 'зверево', 'зеленогорск', 'зеленоградск', 'зеленодольск', 'зеленокумск', 'зерноград', 'зея', 'зима', 'златоуст', 'злынка', 'змеиногорск', 'знаменск', 'зубцов', 'зуевка',
        'ивангород', 'иваново', 'ивантеевка', 'ивдель', 'игарка', 'ижевск', 'избербаш', 'изобильный', 'иланский', 'инза', 'инкерман', 'иннополис', 'инсар', 'инта', 'ипатово', 'ирбит', 'иркутск', 'исилькуль', 'искитим', 'истра', 'ишим', 'ишимбай',
        'йошкар-ола',
        'кадников', 'казань', 'калач', 'калач-на-дону', 'калачинск', 'калининград', 'калининск', 'калтан', 'калуга', 'калязин', 'камбарка', 'каменка', 'каменногорск', 'каменск-уральский', 'каменск-шахтинский', 'камень-на-оби', 'камешково', 'камызяк', 'камышин', 'камышлов', 'канаш', 'кандалакша', 'канск', 'карабаново', 'карабаш', 'карабулак', 'карасук', 'карачаевск', 'карачев', 'каргат', 'каргополь', 'карпинск', 'карталы', 'касимов', 'касли', 'каспийск', 'катав-ивановск', 'катайск', 'качканар', 'кашин', 'кашира', 'кедровый', 'кемерово', 'кемь', 'керчь', 'кизел', 'кизилюрт', 'кизляр', 'кимовск', 'кимры', 'кингисепп', 'кинель', 'кинешма', 'киреевск', 'киренск', 'киржач', 'кириллов', 'кириши', 'киров', 'кировград', 'кирово-чепецк', 'кировск', 'кирс', 'кирсанов', 'киселёвск', 'кисловодск', 'клин', 'клинцы', 'княгинино', 'ковдор', 'ковров', 'ковылкино', 'когалым', 'кодинск', 'козельск', 'козловка', 'козьмодемьянск', 'кола', 'кологрив', 'коломна', 'колпашево', 'кольчугино', 'коммунар', 'комсомольск', 'комсомольск-на-амуре', 'конаково', 'кондопога', 'кондрово', 'константиновск', 'копейск', 'кораблино', 'кореновск', 'коркино', 'королёв', 'короча', 'корсаков', 'коряжма', 'костерёво', 'костомукша', 'кострома', 'котельники', 'котельниково', 'котельнич', 'котлас', 'котово', 'котовск', 'кохма', 'красавино', 'красноармейск', 'красновишерск', 'красногорск', 'краснодар', 'краснозаводск', 'краснознаменск', 'краснокаменск', 'краснокамск', 'красноперекопск', 'краснослободск', 'краснотурьинск', 'красноуральск', 'красноуфимск', 'красноярск', 'красный кут', 'красный сулин', 'красный холм', 'кремёнки', 'кропоткин', 'крымск', 'кстово', 'кубинка', 'кувандык', 'кувшиново', 'кудымкар', 'кузнецк', 'куйбышев', 'кулебаки', 'кумертау', 'кунгур', 'купино', 'курган', 'курганинск', 'курильск', 'курлово', 'куровское', 'курск', 'куртамыш', 'курчатов', 'куса', 'кушва', 'кызыл', 'кыштым', 'кяхта',
        'лабинск', 'лабытнанги', 'лагань', 'ладушкин', 'лаишево', 'лакинск', 'лангепас', 'лахденпохья', 'лебедянь', 'лениногорск', 'ленинск', 'ленинск-кузнецкий', 'ленск', 'лермонтов', 'лесной', 'лесозаводск', 'лесосибирск', 'ливны', 'ликино-дулёво', 'липецк', 'липки', 'лиски', 'лихославль', 'лобня', 'лодейное поле', 'лосино-петровский', 'луга', 'луза', 'лукоянов',
        'магадан', 'магас', 'магнитогорск', 'майкоп', 'майский', 'макаров', 'макарьев', 'макушино', 'малая вишера', 'малгобек', 'малмыж', 'малоархангельск', 'малоярославец', 'мамадыш', 'мамоново', 'мантурово', 'мариинск', 'мариинский посад', 'маркс', 'махачкала', 'мглин', 'мегион', 'медвежьегорск', 'медногорск', 'медынь', 'межгорье', 'междуреченск', 'мезень', 'меленки', 'мелеуз', 'менделеевск', 'мензелинск', 'мещовск', 'миасс', 'микунь', 'миллерово', 'минеральные воды', 'минусинск', 'миньяр', 'мирный', 'михайлов', 'михайловка', 'михайловск', 'мичуринск', 'могоча', 'можайск', 'можга', 'моздок', 'мончегорск', 'морозовск', 'моршанск', 'мосальск', 'москва', 'муравленко', 'мураши', 'мурманск', 'муром', 'мценск', 'мыски', 'мытищи', 'мышкин',
        'набережные челны', 'навашино', 'наволоки', 'надым', 'назарово', 'назрань', 'называевск', 'нальчик', 'нариманов', 'наро-фоминск', 'нарткала', 'нарьян-мар', 'находка', 'невель', 'невельск', 'невинномысск', 'невьянск', 'нелидово', 'неман', 'нерехта', 'нерчинск', 'нерюнгри', 'нестеров', 'нефтегорск', 'нефтекамск', 'нефтекумск', 'нефтеюганск', 'нея', 'нижневартовск', 'нижнекамск', 'нижнеудинск', 'нижние серги', 'нижний ломов', 'нижний новгород', 'нижний тагил', 'нижняя салда', 'нижняя тура', 'николаевск', 'николаевск-на-амуре', 'никольск', 'никольское', 'новая ладога', 'новая ляля', 'новоалександровск', 'новоалтайск', 'новоаннинский', 'нововоронеж', 'новодвинск', 'новозыбков', 'новокубанск', 'новокузнецк', 'новокуйбышевск', 'новомичуринск', 'новомосковск', 'новопавловск', 'новоржев', 'новороссийск', 'новосибирск', 'новосиль', 'новосокольники', 'новотроицк', 'новоузенск', 'новоульяновск', 'новоуральск', 'новохопёрск', 'новочебоксарск', 'новочеркасск', 'новошахтинск', 'новый оскол', 'новый уренгой', 'ногинск', 'нолинск', 'норильск', 'ноябрьск', 'нурлат', 'нытва', 'нюрба', 'нягань', 'нязепетровск', 'няндома',
        'облучье', 'обнинск', 'обоянь', 'обь', 'одинцово', 'озёрск', 'озёры', 'октябрьск', 'октябрьский', 'окуловка', 'оленегорск', 'олонец', 'олёкминск', 'омск', 'омутнинск', 'онега', 'опочка', 'оренбург', 'орехово-зуево', 'орлов', 'орск', 'орёл', 'оса', 'осинники', 'осташков', 'остров', 'островной', 'острогожск', 'отрадное', 'отрадный', 'оха', 'оханск', 'очёр',
        'павлово', 'павловск', 'павловский посад', 'палласовка', 'партизанск', 'певек', 'пенза', 'первомайск', 'первоуральск', 'перевоз', 'пересвет', 'переславль-залесский', 'пермь', 'пестово', 'петров вал', 'петровск', 'петровск-забайкальский', 'петрозаводск', 'петропавловск-камчатский', 'петухово', 'петушки', 'печора', 'печоры', 'пикалёво', 'пионерский', 'питкяранта', 'плавск', 'пласт', 'плёс', 'поворино', 'подольск', 'подпорожье', 'покачи', 'покров', 'покровск', 'полевской', 'полесск', 'полысаево', 'полярные зори', 'полярный', 'поронайск', 'порхов', 'похвистнево', 'почеп', 'починок', 'пошехонье', 'правдинск', 'приволжск', 'приморск', 'приморско-ахтарск', 'приозерск', 'прокопьевск', 'пролетарск', 'протвино', 'прохладный', 'псков', 'пугачёв', 'пудож', 'пустошка', 'пучеж', 'пушкино', 'пущино', 'пыталово', 'пыть-ях', 'пятигорск',
        'радужный', 'райчихинск', 'раменское', 'рассказово', 'ревда', 'реж', 'реутов', 'ржев', 'родники', 'рославль', 'россошь', 'ростов', 'ростов-на-дону', 'рошаль', 'ртищево', 'рубцовск', 'рудня', 'руза', 'рузаевка', 'рыбинск', 'рыбное', 'рыльск', 'ряжск', 'рязань',
        'саки', 'салават', 'салаир', 'салехард', 'сальск', 'самара', 'санкт-петербург', 'саранск', 'сарапул', 'саратов', 'саров', 'сасово', 'сатка', 'сафоново', 'саяногорск', 'саянск', 'светлогорск', 'светлоград', 'светлый', 'светогорск', 'свирск', 'свободный', 'себеж', 'севастополь', 'северо-курильск', 'северобайкальск', 'северодвинск', 'североморск', 'североуральск', 'северск', 'севск', 'сегежа', 'сельцо', 'семикаракорск', 'семилуки', 'семёнов', 'сенгилей', 'серафимович', 'сергач', 'сергиев посад', 'сердобск', 'серов', 'серпухов', 'сертолово', 'сибай', 'сим', 'симферополь', 'сковородино', 'скопин', 'славгород', 'славск', 'славянск-на-кубани', 'сланцы', 'слободской', 'слюдянка', 'смоленск', 'снежинск', 'снежногорск', 'собинка', 'советск', 'советская гавань', 'советский', 'сокол', 'солигалич', 'соликамск', 'солнечногорск', 'соль-илецк', 'сольвычегодск', 'сольцы', 'сорочинск', 'сорск', 'сортавала', 'сосенский', 'сосновка', 'сосновоборск', 'сосновый бор', 'сосногорск', 'сочи', 'спас-деменск', 'спас-клепики', 'спасск', 'спасск-дальний', 'спасск-рязанский', 'среднеколымск', 'среднеуральск', 'сретенск', 'ставрополь', 'старая купавна', 'старая русса', 'старица', 'стародуб', 'старый крым', 'старый оскол', 'стерлитамак', 'стрежевой', 'строитель', 'струнино', 'ступино', 'суворов', 'судак', 'суджа', 'судогда', 'суздаль', 'суоярви', 'сураж', 'сургут', 'суровикино', 'сурск', 'сусуман', 'сухиничи', 'сухой лог', 'сызрань', 'сыктывкар', 'сысерть', 'сычёвка', 'сясьстрой',
        'тавда', 'таганрог', 'тайга', 'тайшет', 'талдом', 'тамбов', 'тара', 'тарко-сале', 'таруса', 'татарск', 'таштагол', 'тверь', 'теберда', 'тейково', 'темников', 'темрюк', 'терек', 'тетюши', 'тимашёвск', 'тихвин', 'тихорецк', 'тобольск', 'тогучин', 'тольятти', 'томари', 'томмот', 'томск', 'топки', 'торжок', 'торопец', 'тосно', 'тотьма', 'троицк', 'трубчевск', 'трёхгорный', 'туапсе', 'туймазы', 'тула', 'тулун', 'туран', 'туринск', 'тутаев', 'тында', 'тырныауз', 'тюкалинск', 'тюмень',
        'уварово', 'углегорск', 'углич', 'удачный', 'удомля', 'ужур', 'узловая', 'улан-удэ', 'ульяновск', 'унеча', 'урай', 'урень', 'уржум', 'урус-мартан', 'урюпинск', 'усинск', 'усмань', 'усолье', 'усолье-сибирское', 'уссурийск', 'усть-джегута', 'усть-илимск', 'усть-катав', 'усть-кут', 'усть-лабинск', 'устюжна', 'уфа', 'ухта', 'учалы', 'уяр',
        'фатеж', 'феодосия', 'фокино', 'фролово', 'фрязино', 'фурманов',
        'хабаровск', 'хадыженск', 'ханты-мансийск', 'харабали', 'харовск', 'хасавюрт', 'хвалынск', 'хилок', 'химки', 'холм', 'холмск', 'хотьково',
        'цивильск', 'цимлянск', 'циолковский',
        'чадан', 'чайковский', 'чапаевск', 'чаплыгин', 'чебаркуль', 'чебоксары', 'чегем', 'чекалин', 'челябинск', 'чердынь', 'черемхово', 'черепаново', 'череповец', 'черкесск', 'черноголовка', 'черногорск', 'чернушка', 'черняховск', 'чехов', 'чистополь', 'чита', 'чкаловск', 'чудово', 'чулым', 'чусовой', 'чухлома', 'чёрмоз',
        'шагонар', 'шадринск', 'шали', 'шарыпово', 'шарья', 'шатура', 'шахты', 'шахтёрск', 'шахунья', 'шацк', 'шебекино', 'шелехов', 'шенкурск', 'шилка', 'шимановск', 'шиханы', 'шлиссельбург', 'шумерля', 'шумиха', 'шуя',
        'щигры', 'щучье', 'щёкино', 'щёлкино', 'щёлково',
        'электрогорск', 'электросталь', 'электроугли', 'элиста', 'энгельс', 'эртиль',
        'югорск', 'южа', 'южно-сахалинск', 'южно-сухокумск', 'южноуральск', 'юрга', 'юрьев-польский', 'юрьевец', 'юрюзань', 'юхнов',
        'ядрин', 'якутск', 'ялта', 'ялуторовск', 'янаул', 'яранск', 'яровое', 'ярославль', 'ярцево', 'ясногорск', 'ясный', 'яхрома'

        ]
    if user_text not in game_lst:
        update.message.reply_text('Нет такого города в нашем списке!')
    else:
        next_turn_letter: str = user_text[-1]
        answer: list = [i for i in game_lst if i.startswith(next_turn_letter) and i != user_text]
        if not answer:
            next_turn_letter: str = user_text[-2]
            answer: list = [i for i in game_lst if i.startswith(next_turn_letter) and i != user_text]
        chosen_city: str = random.choice(answer).title()
        game_lst.remove(user_text)
        update.message.reply_text(f'{next_turn_letter}, {chosen_city}, Ваш ход')
        game_lst.remove(chosen_city)


def calc(update, context):
    user_text: str = update.message.text[6:].strip()
    var1, var2 = '', ''

    for i in user_text:
        if not i.isdigit():
            break
        else:
            var1 += i

    for i in user_text[::-1]:
        if not i.isdigit():
            break
        else:
            var2 += i

    res: list = list(map(int, [var1, (var2)[::-1]]))
    oper: str = ''.join(set(user_text) - set(var1+var2))

    if len(res) != 2:
        return 'Работаю пока только с двумя элементами'
    else:
        try:
            oper_dct: dict = {
                '+': sum(res),
                '-': res[0] - res[1],
                '/': res[0] / res[1],
                '*': res[0] * res[1]
                }

            answer: str = oper_dct.get(oper, 'Данная операция не поддерживается')
        except ZeroDivisionError:
            answer: str = 'Делить на ноль НЕЛЬЗЯ!'
        return update.message.reply_text(answer)


def main():
    mybot = Updater(
        settings.API_KEY,
        # request_kwargs=PROXY,
        use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", constel))
    dp.add_handler(CommandHandler("wordcount", word_counter))
    dp.add_handler(CommandHandler("nfm", next_full_moon))
    dp.add_handler(CommandHandler("cities", city_game))
    dp.add_handler(CommandHandler("calc", calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот запущен')
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    print('Бот запущен!')
    main()
