
from functools import partial
from collections import Counter

from aiogram.types import (
    BotCommand,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

from rc.const import (
    START_COMMAND,
    HELP_COMMAND,
    EDIT_PROFILE_COMMAND,
    EDIT_NAME_COMMAND,
    EDIT_CITY_COMMAND,
    EDIT_LINKS_COMMAND,
    EDIT_ABOUT_COMMAND,
    MATCH_CITY_COMMAND,
    MATCH_WORLDWIDE_COMMAND,
    CANCEL_COMMAND,
    EMPTY_COMMAND,
    PARTICIPATE_COMMAND,
    PAUSE_WEEK_COMMAND,
    PAUSE_MONTH_COMMAND,
    SHOW_CONTACT_COMMAND,
    CONFIRM_CONTACT_COMMAND,
    FAIL_CONTACT_COMMAND,
    CONTACT_FEEDBACK_COMMAND,

    EDIT_NAME_STATE,
    EDIT_CITY_STATE,
    EDIT_LINKS_STATE,
    EDIT_ABOUT_STATE,
    CONTACT_FEEDBACK_STATE,

    CITY_MODE,
    WORLDWIDE_MODE,

    CONFIRM_STATE,
    FAIL_STATE,

    WEEK_PERIOD,
    MONTH_PERIOD,
)
from rc.text import (
    day_month,
    user_url,
    user_mention,
    intro_text,
    EMPTY_SYMBOL
)
from rc.obj import User


######
#
#  TEXT
#
########


########
#   COMMAND
#######


COMMAND_DESCRIPTIONS = {
    START_COMMAND: 'с чего начать',
    HELP_COMMAND: 'справка',

    EDIT_PROFILE_COMMAND: 'настроить профиль',
    EDIT_NAME_COMMAND: 'изменить имя',
    EDIT_CITY_COMMAND: 'изменить город',
    EDIT_LINKS_COMMAND: 'изменить ссылки',
    EDIT_ABOUT_COMMAND: 'изменить "о себе"',

    MATCH_CITY_COMMAND: 'хочу собеседника из моего города',
    MATCH_WORLDWIDE_COMMAND: 'хочу собеседника из любого города',

    PARTICIPATE_COMMAND: 'участвовать во встречах',
    PAUSE_WEEK_COMMAND: 'пауза на неделю',
    PAUSE_MONTH_COMMAND: 'пауза на месяц',

    SHOW_CONTACT_COMMAND: 'контакт, анкета собеседника',
    CONFIRM_CONTACT_COMMAND: 'договорились о встрече',
    FAIL_CONTACT_COMMAND: 'не договорились/не отвечает',
    CONTACT_FEEDBACK_COMMAND: 'как прошла встреча',

    CANCEL_COMMAND: 'отменить',
    EMPTY_COMMAND: 'оставить пустым',
}


######
#  START
######


def start_text(schedule):
    return f'''Бот @shad_alumni_rc_bot организует random coffee для выпускников ШАДа.

С чего начать?
- Дай согласия на участие во встречах /{PARTICIPATE_COMMAND}. В понедельник {day_month(schedule.next_week_monday())} бот подберёт собеседника, пришлёт анкету и контакт.
- Заполни короткую анкету /{EDIT_PROFILE_COMMAND}. Собеседник поймёт, чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.
- В анкете есть поле "город", нажми /{MATCH_CITY_COMMAND}, чтобы бот подобрал собеседника из твоего города.

/{PARTICIPATE_COMMAND} - участвовать во встречах
/{EDIT_PROFILE_COMMAND} - заполнить анкету
/{MATCH_CITY_COMMAND} - хочу собеседника из моего города
/{HELP_COMMAND} - как работает бот, как договориться о встрече, список команд'''


######
#   HELP
######


HELP_TEXT = f'''Бот @shad_alumni_rc_bot организует random coffee для выпускников ШАДа.

<b>Как это работает?</>
- Участник чата "ШАД 15+" запускает бота, заполняет анкету. Бот случайно объединяет участников в пары.
- Раз в неделю бот присылает каждому участнику контакт собеседника и его анкету. Люди договариваются о времени, созваниваются или встречаются вживую.
- В конце недели бот спрашивает "Как прошла встреча? Будешь участвовать на следующей неделе?".

<b>Расписание</>
- Понедельник - бот присылает контакт и анкету собеседника
- Среда - спрашивает "получилось договориться о встрече?"
- Четверг - присылает новый контакт и анкету тем кто ответ "нет" в среду
- Суббота - спрашивает "участвуешь на следующей неделе?"
- Воскресенье - спрашивает "как прошла встреча?"

<b>Как договориться о встрече</b>
Собеседник согласился участвовать во встречах, получил анкету. Твоя задача договориться про время и место. Примеры первых сообщений:
- Привет, бот random coffee дал твой контакт. Когда удобно встретиться/созвониться на этой неделе? Могу в будни после 17.
- Хай, я из шадовского rc ) Ты в Сбере на Кутузовской? Можно там. Когда удобно? Могу в среду, четверг после 18.

По статистике 15-30% участников не могут договориться о встрече. Если собеседник не отвечает, отказывается или переносит, нажми /{FAIL_CONTACT_COMMAND}, в четверг бот пришлёт контакт нового собеседника.

<b>Команды</b>
/{START_COMMAND} - с чего начать
/{HELP_COMMAND} - справка

/{EDIT_PROFILE_COMMAND} - настроить профиль
/{EDIT_NAME_COMMAND} - изменить имя
/{EDIT_CITY_COMMAND} - изменить город
/{EDIT_LINKS_COMMAND} - изменить ссылки
/{EDIT_ABOUT_COMMAND} - изменить "о себе"

/{MATCH_CITY_COMMAND} - хочу собеседника из моего города
/{MATCH_WORLDWIDE_COMMAND} - хочу собеседника из любого города

/{PARTICIPATE_COMMAND} - участвовать во встречах
/{PAUSE_WEEK_COMMAND} - пауза на неделю
/{PAUSE_MONTH_COMMAND} - пауза на месяц

/{SHOW_CONTACT_COMMAND} - контакт, анкета собеседника
/{CONFIRM_CONTACT_COMMAND} - договорились о встрече
/{FAIL_CONTACT_COMMAND} - не договорились/не отвечает
/{CONTACT_FEEDBACK_COMMAND} - как прошла встреча

<b>Авторы</b>
Код - @alexkuk
Аватарка - https://instagram.com/loullllett
Первая версия бота - @riazanovskiy'''


######
#  PROFILE
######


def edit_profile_text(user):
    return f'''{intro_text(user)}

/{EDIT_NAME_COMMAND} - изменить имя
/{EDIT_CITY_COMMAND} - изменить город
/{EDIT_LINKS_COMMAND} - изменить ссылки
/{EDIT_ABOUT_COMMAND} - изменить "о себе"
'''


EDIT_NAME_TEXT = f'''Напиши своё настоящее имя. Собеседник поймёт, как к тебе обращаться.

/{CANCEL_COMMAND} - отменить
/{EMPTY_COMMAND} - оставить пустым'''

EDIT_CITY_TEXT = f'''Напиши город, в котором живёшь. Или выбери из топа популярных. Собеседник поймет предлагать офлайн встречу или нет.

/{CANCEL_COMMAND} - отменить
/{EMPTY_COMMAND} - оставить пустым'''

EDIT_LINKS_TEXT = f'''Накидай ссылок про себя: инста, твиттер, фейсбук, канал, подкаст. Собеседник поймёт чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.

Примеры
- http://lab.alexkuk.ru, https://github.com/kuk, https://habr.com/ru/users/alexanderkuk/
- https://www.linkedin.com/in/alexkuk/, https://vk.com/alexkuk
- http://val.maly.hk

/{CANCEL_COMMAND} - отменить
/{EMPTY_COMMAND} - оставить пустым'''

EDIT_ABOUT_TEXT = f'''Напиши о себе. Собеседник поймёт чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.

Что писать?
- Где учился?
- Где успел поработать? Чем занимался, самое важное/удивительное?
- Где успел пожить?
- Личное, чем занимаешься кроме работы? Спорт, игры.

Пример
"Закончил ШАД в 2011. Работал в Яндексе в Поиске. Сделал библиотеку Nile, чтобы удобно ворочать логи на Мап Редьюсе https://habr.com/ru/company/yandex/blog/332688/.

Автор проекта Наташа https://github.com/natasha - библиотека для русскоязычного NLP. Работаю в своей Лабе https://lab.alexkuk.ru, адаптирую Наташу под задачи клиентов. Присматриваю за чатиком @natural_language_processing - самое крупное сообщество про NLP на русском.

Живу в Москве в Крылатском. У нас тут мекка велоспорта. Умею сидеть на колесе и сдавать смену. Бегаю, пробежал 10 км за 39 минут. Вожу экскурсии для друзей, рассказываю про сталинский генплан, импрессионистов и супрематистов."

/{CANCEL_COMMAND} - отменить
/{EMPTY_COMMAND} - оставить пустым'''

TOP_CITIES = [
    'Москва',
    'Санкт-Петербург',
    'Екатеринбург',
    'Амстердам',
    'Мюнхен',
    'Париж',
]


######
#  MATCH MODE
######


MATCH_WORLDWIDE_TEXT = f'''Бот выберет случайного собеседника среди всех участников.

/{MATCH_CITY_COMMAND} - хочу собеседника из моего города
'''

ASK_EDIT_CITY_TEXT = f'Заполни, пожалуйста, поле "город" в анкете /{EDIT_CITY_COMMAND}. Потом снова нажми /{MATCH_CITY_COMMAND}.'


def match_city_text(city, cities):
    counts = Counter(_ for _ in cities if _)
    count = counts[city]
    if count <= 1:
        # Informative list from the start
        counts.update(TOP_CITIES)

        return f'''Пометил, что хочешь собеседника из города "{city}". Ты пока единственный участник из этого города.

Проверь, что написал название города, как остальные участники. Например, "Санкт-Петербург" вместо "Питер", "Париж" вместо "Paris".

Города из анкет участников: {', '.join(sorted(counts))}.

/{MATCH_WORLDWIDE_COMMAND} - хочу собеседника из любого города'''

    else:
        return f'''Пометил, что хочешь собеседника из города "{city}". Участников с таким городом в анкете - {count}.

/{MATCH_WORLDWIDE_COMMAND} - хочу собеседника из любого города'''


#####
#  CONTACT
#####


def lines_text(lines):
    return '\n'.join(lines)


def participate_lines(user, schedule):
    yield f'Пометил, что участвуешь во встречах. В понедельник {day_month(schedule.next_week_monday())} бот пришлёт анкету и контакт собеседника.'

    if not user.links and not user.about:
        yield f'''
Заполни, пожалуйста, ссылки /{EDIT_LINKS_COMMAND} или "о себе" /{EDIT_ABOUT_COMMAND}. Собеседник поймёт чем ты занимаешься, о чём интересно спросить. Снимает неловкость в начале разговора.'''

    if not user.city:
        yield f'''
Чтобы бот подобрал собеседника из твоего города, заполни поле "город" в анкете /{EDIT_CITY_COMMAND} и нажми /{MATCH_CITY_COMMAND}'''


NO_CONTACT_TEXT = 'Бот не назначил тебе собеседника.'
PAUSE_TEXT = 'Поставил встречи на паузу. Бот не будет присылать контакты собеседников и напоминания.'


def show_contact_text(user, contact):
    return f'''Контакт собеседника в Телеграме: <a href="{user_url(user.user_id)}">{user_mention(user)}</a>

{intro_text(user)}

/{CONFIRM_CONTACT_COMMAND} - договорились о встрече
/{FAIL_CONTACT_COMMAND} - не договорились/не отвечает
/{CONTACT_FEEDBACK_COMMAND} - оставить фидбек'''


CONFIRM_CONTACT_TEXT = f'''Пометил, что вы договорились о встрече. Бот не потревожит рассылкой с напоминанием списаться.

/{CONTACT_FEEDBACK_COMMAND} - оставить фидбек о встрече'''


def fail_contact_text(schedule):
    if schedule.now() < schedule.current_week_thursday():
        return f'''Пометил, что не получилось договориться. Бот подберет нового собеседника в четверг {day_month(schedule.current_week_thursday())}.

/{CONFIRM_CONTACT_COMMAND} - всё-таки получилось договориться, не надо подбирать нового'''

    else:
        return f'''Жалко, что встреча не состоялась.

Участвуешь на следующей неделе? Если дашь согласие, в понедельник {day_month(schedule.next_week_monday())} бот пришлёт анкету и контакт собеседника.

/{PARTICIPATE_COMMAND} - участвовать
/{PAUSE_WEEK_COMMAND} - пауза на неделю
/{PAUSE_MONTH_COMMAND} - пауза на месяц'''


def contact_feedback_text(user):
    return f'''Напиши фидбек своими словами или оставь оценку от 1 до 5, где 1 - очень плохо, 5 - очень хорошо. Собеседник на этой неделе - <a href="{user_url(user.user_id)}">{user_mention(user)}</a>.

/{CANCEL_COMMAND} - отменить
/{EMPTY_COMMAND} - оставить пустым'''


CONTACT_FEEDBACK_OPTIONS = '12345'


def contact_feedback_state_text(user, contact, schedule):
    return f'''Фидбек - "{contact.feedback or EMPTY_SYMBOL}", собеседник - <a href="{user_url(user.user_id)}">{user_mention(user)}</a>.

Участвуешь во встречах на следующей неделе? Если дашь согласие, в понедельник {day_month(schedule.next_week_monday())} бот пришлёт анкету и контакт собеседника.

/{PARTICIPATE_COMMAND} - участвовать
/{PAUSE_WEEK_COMMAND} - пауза на неделю
/{PAUSE_MONTH_COMMAND} - пауза на месяц'''


#######
#
#   HANDLERS
#
######


######
#  START
######


async def handle_start(context, message):
    user = await context.db.get_user(message.from_user.id)
    if not user:
        user = User(
            user_id=message.from_user.id,
            username=message.from_user.username,
            created=context.schedule.now(),
            name=message.from_user.full_name,
        )
        await context.db.put_user(user)

    await context.bot.set_my_commands(commands=[
        BotCommand(command, description)
        for command, description
        in COMMAND_DESCRIPTIONS.items()
    ])

    text = start_text(context.schedule)
    await message.answer(text=text)


#####
#  PROFILE
######


async def handle_edit_profile(context, message):
    user = await context.db.get_user(message.from_user.id)
    text = edit_profile_text(user)
    await message.answer(text=text)


async def handle_edit_name(context, message):
    user = await context.db.get_user(message.from_user.id)

    markup = None
    if not user.name and message.from_user.full_name:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(message.from_user.full_name)

    await message.answer(
        text=EDIT_NAME_TEXT,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_NAME_STATE
    )


async def handle_edit_city(context, message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for city in TOP_CITIES:
        markup.insert(city)

    await message.answer(
        text=EDIT_CITY_TEXT,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_CITY_STATE
    )


async def handle_edit_links(context, message):
    await message.answer(text=EDIT_LINKS_TEXT)
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_LINKS_STATE
    )


async def handle_edit_about(context, message):
    await message.answer(text=EDIT_ABOUT_TEXT)
    await context.db.set_chat_state(
        message.chat.id,
        EDIT_ABOUT_STATE
    )


def parse_command(text):
    if text.startswith('/'):
        return text.lstrip('/')


async def handle_edit_profile_states(context, message):
    state = await context.db.get_chat_state(message.chat.id)
    user = await context.db.get_user(message.from_user.id)

    command = parse_command(message.text)
    if command != CANCEL_COMMAND:
        if command != EMPTY_COMMAND:
            value = message.text
        else:
            value = None

        if state == EDIT_NAME_STATE:
            user.name = value
        elif state == EDIT_CITY_STATE:
            user.city = value
        elif state == EDIT_LINKS_STATE:
            user.links = value
        elif state == EDIT_ABOUT_STATE:
            user.about = value

        user.updated_profile = context.schedule.now()
        await context.db.put_user(user)

    text = edit_profile_text(user)
    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )
    await context.db.set_chat_state(
        message.chat.id,
        state=None
    )


#####
#  MATCH
#######


async def handle_match_city(context, message):
    user = await context.db.get_user(message.from_user.id)

    if not user.city:
        await message.answer(text=ASK_EDIT_CITY_TEXT)
        return

    user.match_mode = CITY_MODE

    await context.db.put_user(user)

    cities = await context.db.read_user_cities()
    text = match_city_text(user.city, cities)
    await message.answer(text)


async def handle_match_worldwide(context, message):
    user = await context.db.get_user(message.from_user.id)

    user.match_mode = WORLDWIDE_MODE

    await context.db.put_user(user)

    await message.answer(text=MATCH_WORLDWIDE_TEXT)


######
#  PARTICIPATE/PAUSE
#######


async def handle_participate(context, message):
    user = await context.db.get_user(message.from_user.id)

    user.agreed_participate = context.schedule.now()
    user.paused = None
    user.pause_period = None

    await context.db.put_user(user)

    text = lines_text(participate_lines(user, context.schedule))
    await message.answer(text=text)


async def handle_pause(context, message):
    user = await context.db.get_user(message.from_user.id)

    user.agreed_participate = None
    user.paused = context.schedule.now()

    command = parse_command(message.text)
    if command == PAUSE_WEEK_COMMAND:
        user.pause_period = WEEK_PERIOD
    elif command == PAUSE_MONTH_COMMAND:
        user.pause_period = MONTH_PERIOD

    await context.db.put_user(user)
    await message.answer(text=PAUSE_TEXT)


######
#  CONTACT
#########


async def handle_contact(context, message):
    user = await context.db.get_user(message.from_user.id)

    if not user.partner_user_id:
        await message.answer(text=NO_CONTACT_TEXT)
        return

    key = (
        context.schedule.current_week_index(),
        user.user_id,
        user.partner_user_id
    )
    contact = await context.db.get_contact(key)
    if not contact:
        await message.answer(text=NO_CONTACT_TEXT)
        return

    return contact


async def handle_show_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    partner_user = await context.db.get_user(contact.partner_user_id)
    text = show_contact_text(partner_user, contact)
    await message.answer(text=text)


async def handle_confirm_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    contact.state = CONFIRM_STATE
    await context.db.put_contact(contact)

    await message.answer(text=CONFIRM_CONTACT_TEXT)


async def handle_fail_contact(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    contact.state = FAIL_STATE
    await context.db.put_contact(contact)

    text = fail_contact_text(context.schedule)
    await message.answer(text=text)


async def handle_contact_feedback(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        row_width=len(CONTACT_FEEDBACK_OPTIONS)
    )
    for option in CONTACT_FEEDBACK_OPTIONS:
        markup.insert(option)

    partner_user = await context.db.get_user(contact.partner_user_id)
    text = contact_feedback_text(partner_user)
    await message.answer(
        text=text,
        reply_markup=markup
    )
    await context.db.set_chat_state(
        message.chat.id,
        CONTACT_FEEDBACK_STATE
    )


async def handle_contact_feedback_state(context, message):
    contact = await handle_contact(context, message)
    if not contact:
        return

    command = parse_command(message.text)
    if command != CANCEL_COMMAND:
        if command != EMPTY_COMMAND:
            contact.feedback = message.text
        else:
            contact.feedback = None
        await context.db.put_contact(contact)

    partner_user = await context.db.get_user(contact.partner_user_id)
    text = contact_feedback_state_text(partner_user, contact, context.schedule)

    await message.answer(
        text=text,
        reply_markup=ReplyKeyboardRemove()
    )
    await context.db.set_chat_state(
        message.chat.id,
        state=None
    )


######
#  HELP/OTHER
########


async def handle_help(context, message):
    await message.answer(text=HELP_TEXT)


async def handle_other(context, message):
    await message.answer(text=HELP_TEXT)


#######
#   SETUP
######


def setup_handlers(context):
    context.dispatcher.register_message_handler(
        partial(handle_start, context),
        commands=START_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_edit_profile, context),
        commands=EDIT_PROFILE_COMMAND
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_name, context),
        commands=EDIT_NAME_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_city, context),
        commands=EDIT_CITY_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_links, context),
        commands=EDIT_LINKS_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_edit_about, context),
        commands=EDIT_ABOUT_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_match_city, context),
        commands=MATCH_CITY_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_match_worldwide, context),
        commands=MATCH_WORLDWIDE_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_participate, context),
        commands=PARTICIPATE_COMMAND
    )
    context.dispatcher.register_message_handler(
        partial(handle_pause, context),
        commands=[
            PAUSE_WEEK_COMMAND,
            PAUSE_MONTH_COMMAND,
        ]
    )

    context.dispatcher.register_message_handler(
        partial(handle_show_contact, context),
        commands=SHOW_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_confirm_contact, context),
        commands=CONFIRM_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_fail_contact, context),
        commands=FAIL_CONTACT_COMMAND,
    )
    context.dispatcher.register_message_handler(
        partial(handle_contact_feedback, context),
        commands=CONTACT_FEEDBACK_COMMAND,
    )

    context.dispatcher.register_message_handler(
        partial(handle_help, context),
        commands=HELP_COMMAND,
    )

    # Every call to chat_states filter = db query. Place handlers
    # last. TODO Implement aiogram storage adapter for DynamoDB,
    # natively handle FSM

    context.dispatcher.register_message_handler(
        partial(handle_edit_profile_states, context),
        chat_states=[
            EDIT_NAME_STATE,
            EDIT_CITY_STATE,
            EDIT_LINKS_STATE,
            EDIT_ABOUT_STATE,
        ]
    )
    context.dispatcher.register_message_handler(
        partial(handle_contact_feedback_state, context),
        chat_states=CONTACT_FEEDBACK_STATE,
    )

    context.dispatcher.register_message_handler(
        partial(handle_other, context)
    )
