from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def create_button(view, data):
    return InlineKeyboardButton(view, callback_data=data)


def create_page_button_list(bef, end, prefix, pre=None):
    if pre == None:
        button_list = []
    else:
        button_list = [pre]
    for x in range(bef, end):
        button_list.append(create_button(x, prefix + str(x)))
    return button_list
