from numba import njit
from math import sqrt
from itertools import combinations


class Num:
    def __init__(self, number):
        self.num = number

    @staticmethod
    @njit
    def dividers_get(integer):
        div_lst = [i for i in range(1, integer + 1) if integer % i == 0]
        return div_lst

    def factorization(self):
        """Calculates all divisors of a number"""
        div_lst = self.dividers_get(self.num)
        return div_lst

    def dividers(self):
        """ Searching the all dividers of number """
        div_lst = self.factorization()
        return 'Все делители числа: {}'.format(div_lst)

    def issimple(self):
        """ Checking, number is simple? """
        div_lst = self.factorization()
        if len(div_lst) == 2:
            return 'Ваше число простое'
        else:
            return 'Ваше число составное'

    def rectangleness(self):
        """Checks if a number is rectangular, that is, the ability to represent a number as :
    n * (n + 1)"""
        div_lst = self.factorization()
        try:
            for k in combinations(div_lst, 2):
                if k[0] * k[1] == self.num and k[0] + 1 == k[1]:
                    return 'Число можно представить в виде n * (n + 1), где n - {}'.format(k[0])
                if k[0] * k[1] == self.num and k[0] + 1 == k[1]:
                    return 'Число можно представить в виде n * (n + 1), где n - {}'.format(k[0])
                else:
                    return 'Число нельзя представить в виде n * (n + 1)'
        except UnboundLocalError:
            pass

    def unusual(self):
        """Natural number unusual if it largest divider of this number more than square of this number"""
        div_lst = self.factorization()
        if div_lst[len(div_lst) - 2] > sqrt(self.num):
            return 'Ваше число необычное т.е его наибольший делитель больше чем квадратный корень этого числа'
        else:
            return 'Ваше число не является необычным'

    def smooth(self):
        """Quantify of the dividers of the numbers, who less than 10"""
        div_lst = self.factorization()
        filtrate = filter(lambda x: x == 2 or x == 3 or x == 5 or x == 7 and x > 1, div_lst)
        result = []
        for elem in filtrate:
            result.append(elem)
        return 'Количество простых делителей числа, не превышающих десяти: {}'.format(len(result))

    def isexcess(self):
        """Checking if a sum of the dividers of the number more than number"""
        div_lst = self.factorization()
        Sum = sum(div_lst[:len(div_lst) - 1])
        if Sum > self.num:
            return 'Ваше число избыточное ведь сумма его делителей - {} > {} - числа'.format(Sum, self.num)
        else:
            return 'Ваше число не является избыточным'

    def issufficient(self):
        div_lst = self.factorization()
        Sum = sum(div_lst[:len(div_lst) - 1])
        if Sum < self.num:
            return 'Ваше число недостаточное ведь сумма его делителей - {} < {} - числа'.format(Sum, self.num)
        else:
            return 'Ваше число не является недостаточным'

    def repr_pow2(self):
        return 'Квадрат вашего числа равен: {}'.format(pow(self.num, 2))

    def repr_sqrt2(self):
        return 'Корень из вашего числа равен: {}'.format(sqrt(self.num))

if __name__ == '__main__':
    n = Num(2)
