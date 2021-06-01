from datetime import datetime
from math import sqrt
import service1 as sv
from visual import visual_representation, wrap
from main_class import Num
run = True
based = []

while run:
    num = input('Вводите натуральное число чтобы узнать об его свойствах: ')
    try:
        if num == 'quit':
            run = False
            break
        num = int(num)
        if num <= 1:
            raise ValueError
        cl = Num(num)
        numData = [cl.dividers(), cl.issimple(), cl.rectangleness(), cl.unusual(), cl.smooth(), cl.isexcess(),
                   cl.issufficient(), cl.repr_pow2(), cl.repr_sqrt2(), sv.romanize(num), sv.bitize(num)]

        based += sv.check_savings("__cache__.txt", ["dict:", "[", "]"])
        if num in based:
            print("\nВы уже ранее вводили это число\n".center(150, '-'))
            continue
        sv.print_all(numData, num)
        try:
            with open('__cache__.txt', 'a+') as nD:
                if num not in based:
                    print(datetime.now(), file=nD)
                    print(sv.formData(numData, cl, num), file=nD)
            based.append(num)
            based = list(set(based))
        except FileNotFoundError:
            print(
                'Нужный файл не получилось найти, без этого вы не сможете получить доступ к числовой базе данных и '
                'ввести вклад в неё')
        visual_representation(numData, sv.rct, sv.unus, sv.isEx, sv.suf, sv.isS, cl.factorization, num,
                              cl.smooth, cl.repr_sqrt2, cl.repr_pow2, sv.roman, str(bin(num))[2:])
    except ValueError:
        print('Вы ввели не натуральное число')

input('Нажмите Enter чтобы выйти...  ')
with open('__cache__.txt', 'a+') as nD:
    print(f'dict: {based}', file=nD)
exit()