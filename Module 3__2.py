from pkgutil import extend_path


def parametrs(a,b,c):
    print(a, b ,c)

def function(a, b=3, c=None):
    if c is None:
        c = []
        c.append(a + b)
    print(c)
   # elif c > 0:


      #  print(c)




function(4)
function(5,b=6)

function(6,4,44)
function(9,34,33)




def mail_sander(sender = 'university.help@gmail.com', message = 'Вы все хорошие', *, recipient):
    #message = 'если раскомментировать, то получится принимающий аргумент в функции и все message по умолчанию будут
    # этим текстом
    if sender == recipient:
        print(f'Невозможно отправить самому себе')
        return


    if '@' not in sender or not (sender.endswith('.com') or sender.endswith('.ru') or sender.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса1 {sender} на адрес {recipient}. Сообщение: {message}')
        print('ОШИБКА! У отправителя пропущены символы "@", ".ru", ".net", ".com"')
    elif '@' not in recipient or not (recipient.endswith('.com') or recipient.endswith('.ru') or recipient.endswith('.net')):
        print(f'Невозможно отправить письмо с адреса2 {sender} на адрес {recipient}. Сообщение: {message}')
        print('ОШИБКА! У получателя пропущены символы "@", ".ru", ".net", ".com"')
    else:
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}. Сообщение: {message}')
        else:
            print(f'ВНИМАНИЕ: НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
                  f' Сообщение: {message}')

mail_sander(message='Urban uchit coditb, как же horosho', recipient='killdozerbur@yandex.com')
mail_sander(recipient='chillyband@gavmail.net')
mail_sander(sender='university.help@gmail.cococo', recipient='killdozerbur@yande.ru')
mail_sander(recipient='trevorgmail.ru')
mail_sander(sender='chillybandonfire@gavmail.ru', message='Письмо от кавер группы Чилли', recipient='merries@mail.net')
mail_sander(recipient='university.help@gmail.com')

#Крч надеюсь все правильно, было много затыков со знаками препинания и НИ в ОДНОМ УРОКЕ НЕТ ОБЬЯСНЕНИЯ о способе вывода
# принт через print(f''). в модуле номер два, преподаватель пользуется этим способом на вебинаре и очень вскользь упоминает
mail_sander(sender=input(),recipient=input())
