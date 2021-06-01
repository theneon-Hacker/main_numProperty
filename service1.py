from itertools import dropwhile
def roman(n):
    if n > 0 and n < 3999:
        ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hunds = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thounds = ["","M","MM","MMM","MMMM"]

        t = thounds[n // 1000]
        h = hunds[n // 100 % 10]
        te = tens[n // 10 % 10]
        o =  ones[n % 10]

        return t + h + te + o
    else:
        return " - "


def romanize(num):
    if num < 0 or num > 3999:
        return "Ваше число нельзя представить в римской системе счисления"
    else:
        return f"Число в римской системе счисления: {roman(num)}"


def bitize(num):
    return f"Число в двоичной системе счисления: {str(bin(num))[2:]}"


def print_all(numData, num):
    print('Число {}:'.format(num), end='\n\t')
    for k, item in enumerate(numData):
        print(numData[k], end='\n\t')
    print('')

isS = rct = unus = isEx = suf = False
def formData(numData, MC, num):
    global rct, unus, isEx
    global isS, suf
    if 'простое' in numData[1]:
        isS = True
    elif 'составное' in numData[1]:
        isS = False
    if ',' in numData:
        rct = True
    elif ',' not in numData:
        rct = False
    if '.' in numData:
        unus = True
    elif '.' not in numData:
        unus = False
    if '>' in numData:
        isEx = True
    if '>' not in numData:
        isEx = False
    if '<' in numData:
        suf = True
    else:
        suf = False
    datapiece = f'''
  "Число %d":
    "{MC.dividers()}",
    "Число простое": {str(isS).lower()},
    "Число является прямоугольным": {str(rct).lower()},
    "Число - необычное": {str(unus).lower()},
    "%s",
    "Число избыточное": {str(isEx).lower()},
    "Число недостаточное": {str(suf).lower()},
    "{MC.repr_pow2()}",
    "{MC.repr_sqrt2()}",
    "Число в римской системе счисления": {romanize(num)[35:]},
    "Число в двоичной системе счисления": {str(bin(num))[2:]}.

''' % (num, MC.smooth())
    return datapiece


def check_savings(file, patterns_list):
    with open(file, 'r') as f:
        try:
            all_ = f.read()
            all_ = ''.join(all_)
            all_ = all_.split('\n')
            all_ = reversed(all_)
            for line in all_:
                for elem in patterns_list:
                    if elem in line: continue
                    else:
                        break
                else:
                    character_map = {

                    }
                    for j in patterns_list[1:]:
                        character_map.update({ord(j): ''})
                    line = line.translate(character_map)
                    line = line.replace(f"{patterns_list[0]}", '')
                    line = line.lstrip(' \n').rstrip(' \n')
                    line = line.split(", ")
                    line = [i for i in map(int, line)]
                    return line
            assert False
        except:
            return []

if __name__ == '__main__':
    pass

    
