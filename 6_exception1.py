def hello_user():

    print('Привет! Введите сообщение: ')

    while True:
        try:
            inp: str = input().strip().lower()
            if inp == 'пока':
                get_answer()
                break
            elif inp != 'хорошо':
                print('Как дела?')
            else:
                print('Рад за Вас! (но не от всей души, конечно)\n\nВведите сообщение: ')
                continue
        except KeyboardInterrupt:
            print('\nПока!')
            break


def get_answer():
    print('Пока!')


if __name__ == "__main__":
    hello_user()
