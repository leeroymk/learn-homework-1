"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    try:
        age: str = input('Please, enter your age: ').strip()
        age_processed: int = int(age)
    except ValueError:
        return print('Please, enter a number. Next time...')
    else:
        have_to_do(age_processed)


def have_to_do(age):
    if age > 0:
        print(f'So, your age is {age}.')
        if age in range(1, 7):
            print("Why aren't you in kindergarten?")
        elif age in range(7, 18):
            print("Why aren't you in school?")
        elif age in range(18, 24):
            print("Why aren't you in college?")
        else:
            print("Why aren't you at work?")
    else:
        print('Enter the correct age. Next time...')


if __name__ == "__main__":
    main()
