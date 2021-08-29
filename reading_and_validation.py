import sys
from argparse import ArgumentParser
import pandas as pd


class WrongArguments(Exception):
    def __init__(self, accuracy=0.0, lr=0.0, km=100):
        self.accuracy = accuracy
        self.lr = lr
        self.km = km
        if accuracy >= 1.0 or accuracy < 0.0 or lr < 0.0:
            print('accur дожен быть в диапазоне от 0 до 1, lr - больше 0')
            exit()
        if km < 0:
            print('km дожен быть больше 0')
            exit()


def validation(parser):

    namespace, unknown = parser.parse_known_args(sys.argv[1:])
    try:
        acc, learning_rate = float(namespace.accur), float(namespace.lr)
        visual, error = namespace.vis, namespace.error
        WrongArguments(acc, learning_rate)
        return acc, learning_rate, visual, error
    except ValueError as e:
        print('Неверный формат параметров')
        exit()


def get_arguments_train():

    parser = ArgumentParser(prog='train_linear_regression', description='''
    Эта программа позволяет понять, как работает линейная регрессия.
    Проверяющий может поиграться со входными параметрами и посмотреть,
    как их значения влияют на конечный результат''', add_help=False,
                            epilog='''
    (c) October 2020. Автор программы, как всегда, пусечка и лапочка.''')
    group = parser.add_argument_group(title='Параметры')
    group.add_argument('--help', '-h', action='help', help='Справка')
    group.add_argument('--accur', '-accur', default='0.91242',
                       help='Точность предсказания')
    group.add_argument('--lr', '-lr', default='0.02',
                       help='Шаг обучения модели')
    group.add_argument('--vis', '-vis', action='store_const', const=True,
                       help='График исходных значений и предсказаний')
    group.add_argument('--error', '-error', action='store_const', const=True,
                       help='График изменения ошибки')
    group.add_argument('every', nargs='?', metavar='')
    return parser


def validate_data():

    try:
        data = pd.read_csv('data.csv')
    except FileNotFoundError as e:
        print('Источник данных отсутствует')
        exit()
    else:
        x_tr = [i for i in data['km']]
        y = [i for i in data['price']]
        delete = list()
        if not isinstance(y[0], int):
            for i in range(len(y)):
                if not y[i].isdigit():
                    delete.append(i)
        if not isinstance(x_tr[0], int):
            for i in range(len(y)):
                if not x_tr[i].isdigit() and i not in delete:
                    delete.append(i)
        y = [int(y[i]) for i in range(len(y)) if i not in delete]
        x_tr = [int(x_tr[i]) for i in range(len(x_tr)) if i not in delete]
        if len(y) == 0:
            print('Данные пусты')
            exit()
        return x_tr, y


def read_validate_train():
    parser = get_arguments_train()
    accur, learning_rate, vis, error = validation(parser)
    x_tr, y = validate_data()
    return accur, learning_rate, x_tr, y, vis, error


def validate_data_estimate():

    try:
        data = pd.read_csv('results.csv', header=None)
    except FileNotFoundError as e:
        print('''Источник данных отсутствует.
        theta_0 и theta_1 по умолчанию равны 0
        
        Стоимость авто равна 0''')
        exit()
    else:
        try:
            data.fillna(0, inplace=True)
            theta_0 = float(data[0][0])
            theta_1 = float(data[1][0])
        except ValueError as e:
            print('Измените данные в файле')
            exit()
        else:
            return theta_0, theta_1


def validation_estimate(parser):
    namespace, unknown = parser.parse_known_args(sys.argv[1:])
    try:
        km = int(namespace.km)
        WrongArguments(km=km)
        return km
    except ValueError as e:
        print('Неверный формат параметров')
        exit()


def get_arguments_estimate():

    parser = ArgumentParser(prog='train_linear_regression', description='''
    С помощью этой программы можно предсказать стоимость автомобиля,
    в зависимости от его пробега.''', add_help=False, epilog='''
    (c) October 2020. Автор программы, как всегда, пусечка и лапочка.''')
    group = parser.add_argument_group(title='Параметры')
    group.add_argument('--help', '-h', action='help', help='Справка')
    group.add_argument('--km', '-km', default='5000', help='Пробег автомобиля')
    group.add_argument('every', nargs='?', metavar='')
    return parser


def read_validate_estimate():

    parser = get_arguments_estimate()
    km = validation_estimate(parser)
    theta_0, theta_1 = validate_data_estimate()
    return theta_0, theta_1, km
