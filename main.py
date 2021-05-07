import configparser, os, math, lang

cnf = configparser.ConfigParser()

#term vars
root = False
vrs = {}

#sys vars
ftps = ['other', 'xc', 'mn', 'mni']
tps = ['int', 'str', 'float', 'bool', 'list', 'dict']
utps = ['root', 'default', 'guest']
chrs = ['%n', '%s', '&', '||', '|', '!', '=?', '=>', '<=']
kw = ['@class', '@void', 'constructor', 'if' 'else', 'elseif', 'while', 'for', 'do']
errs = {'MathError': ['DivideByZero', 'FloatFactorial', 'NegativeFactorial'], 'FoundError': ['AppNoFound', 'AttribyteNoFound', 'VoidNoFound', 'ClassNoFound', 'LibNoFound', 'VarNoFound', 'TypeNoFound', 'UserNoFound', 'SystemVarNoFound', 'ErrorNoFound', 'CommandNoFound', 'FileNoFound', 'NoFoundSystemFile'], 'SyntaxError': '', 'ListDictError': ['IndexError', 'NameError', 'ValueError'], 'FormatError': ['IntToStr', 'FloatToStr', 'BoolToStr']}
prcs = {'lg': 'main.py/lg()'}
sh = {'name': '', 'ver': '', 'date': '', 'fs': ''}

cnf.read('mni.tc')
sh['name'] = cnf['sh']['nm']
sh['ver'] = cnf['sh']['ver']
sh['fs'] = cnf['sh']['fs']
cms = cnf['sh']['cms']


#methods for gen

def isfloat(what):
    if what.replace('.', '', 1).isdigit():
        return True
    else:
        return False

def spl(what):
    return str(what).replace("'", '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('(', '').replace(')', '').replace(',', '')

def ibol(what):
    if str(what).lower() == 'true' or str(what).lower() == 'false':
        return True
    else:
        return False

def indot(what):
    what = what.replace('"', "'")
    if what.startswith("'") and what.endswith("'"):
        return True
    else:
        return False

#main methods
def col(text, col='', eff='', w=''):
    cols = {'r': '31', 'g': '32', 'y': '33', 'b': '34', 'v': '35', 'w': '37', 'bl': '30'}
    effs = {'b': '1', 'i': '3'}
    
    if text == 'pd':
        pd = str(f'\033[31m\033[1mPermission Denied' + '\033[37m\033[0m ').replace('None', '')
        if w == 'r':
            return pd
        else:
            print(pd)
    elif text == 'pa':
        pa = str(f'\033[32m\033[1mPermission Access' + '\033[37m\033[0m ').replace('None', '')
        if w == 'r':
            return pa
        else:
            print(pa)
    else:
        txt = (f'\033[{cols[col]}m\033[{effs[eff]}m{text}\033[37m\033[0m')
        if w == 'r':
            return txt
        else:
            print(txt)

def er(nm, dic, w, a, n=''):
    if a == 'w':
        if nm in errs:
            if w == 'p':
                if n.strip() == '':
                    a = col(f'{nm} : {dic}', 'r', 'b', 'r')
                else:
                    a = col(f'{nm}.{n} : {dic}', 'r', 'b', 'r')
                print(a)
            else:
                return a
        else:
            if w == 'p':
                a = col(errs[list(errs)[1]][9], 'r', 'b', 'r')
                print(a)
            else:
                return a
    elif a == 'm':
        if nm in errs:
            print(errs[nm])
        else:
            er('FoundError', nm, 'p', 'w', 'ErrorNoFound')

def wrt(what):
    if what in vrs:
        print(spl(vrs[what]).partition(':')[2])
    else:
        if what == '-sys -ftps':
            print(spl(ftps))
        elif what == '-sys -tps':
            print(spl(tps))
        elif what == '-sys -utps':
            print(spl(utps))
        elif what == '-sys -chrs':
            print(spl(chrs))
        elif what == '-sys -kw':
            print(spl(kw))
        elif what == '-sys -errs':
            print(spl(errs))
        elif what == '-sys -n':
            print(sh['name'])
        elif what == '-sys -v':
            print(sh['ver'])
        elif what == '-sys -date':
            print(sh['date'])
        elif root and what == '-sys -fs':
            print(sh['fs'])
        elif what == '-sys -cms':
            print(spl(cms))
        elif what == '-sys -root':
            if root:
                col('True', 'g', 'b', 'p')
            if root == False:
                col('False', 'r', 'b', 'p')
        elif what == '-sys -vrs':
            print(vrs)
        elif what == '-sys -fs':
            print(sh['fs'])
        else:
            print(what)

def wrts(what):
    a = what.split(' ')
    for c in a:
        if c in vrs:
            v = vrs[c]
            if list(v.keys())[0] == 'str':
                a[a.index(c)] = c.replace(c, list(v.values())[0])
            if list(v.keys())[0] != 'str':
                if list(v.keys())[0] == 'int':
                    er('FormatError', v, 'p', 'w', 'IntToStr')
                    break
                elif list(v.keys())[0] == 'float':
                    er('FormatError', v, 'p', 'w', 'FloatToStr')
                    break

            v = ' '.join(a)

    try:
        print(v)
    except UnboundLocalError:
        col('Print other var, if it not, then use comand wrt (man wrt)', 'r', 'b', 'p')

def usr(ind, what):
    cnf.read('usr.tc')
    usrn = cnf[ind]['nm']
    usrt = cnf[ind]['tp']
    usrp = cnf[ind]['ps']
    if what == 'n':
        return usrn
    if what == 'p':
        return usrp
    if what == 't':
        return usrt

def sudo(id, type):
    global root
    if type == 1:
        nm = usr(id, 'n')
        p = usr(id, 'p')
        _p = input(f'Entry password from {nm}: ')
        if root:
            print('You a root')
        else:
            if _p == p:
                col('pa', 'p')
                root = True
                return True
            else:
                col('pd', 'p')
                root = False
                return False

    if type == 0:
        nam = usr(id, 'n')
        pas = usr(id, 'p')
        _pas = input(f'Entry a password from {nam}: ')
        if root:
            return ''
        else:
            if _pas == pas:
                root = True
                return True
            else:
                root = False
                return False

def lef(nm, vl, what=''):
    t = ''
    if vl.isdigit():
        t = tps[0]
    elif isfloat(vl):
        t = tps[2]
    elif ibol(vl):
        t = tps[3]
    else:
        t = tps[1]
    vrs[nm] = {t: vl}
    if what == 't':
        return t
    elif what == 'vl':
        return vl
    elif what == 'tvl':
        return t, vl
    elif what == 'n':
        return nm
    else:
        return ''

def tp(what):
    if what in vrs:
        print(spl(vrs[what]).partition(':')[0].strip())
    else:
        if what.isdigit():
            print(tps[0])
        elif isfloat(what):
            print(tps[2])
        elif ibol(what):
            print(tps[3])
        elif what.isdigit() == False and isfloat(what) == False and ibol(what) == False:
            print(tps[1])
        else:
            er('FoundError', what, 'p', 'w', 'TypeNoFound')

def ex():
    exit()

def ln(what):
    if what:
        print(f'{what} length : {len(what)}')

def fil(file, action, what=''):
    try:
        global f
        f = open(file, 'r+')
    except FileNotFoundError:
        er('FoundError', file, 'p', 'w', 'FileNoFound')
    if action == '-rd*':
        print(f.read())
    elif action == '-rdl':
        h = f.readlines()
        s = str(h[int(what) - 1])
        if s.endswith('\n'):
            s = s.replace('\n', '')
        else:
            s = s
        print(s)
    elif action == '-rdls':
        h = f.readlines()
        one = int(what.partition('-')[0]) -1
        two = int(what.partition('-')[2])
        #print(one, two)
        s = [i for i in h[one:two]]
        for u in s:
            if u.endswith('\n'):
                u = u.replace('\n', '')
            else:
                u = u
            print(u)
    elif action == '-n':
        print(os.path.splitext(file)[0])
    elif action == '-e':
        print(os.path.splitext(file)[1])

def cls():
    os.system('clear')

def manual(what):
    if what in cms:
        cnf.read('help.tc')
        base = cnf[what]['base']
        main = cnf[what]['1']
        print(f'EXAMPLE COMMAND: {base}\n{main}')

def mnt(frm, what, new):
    global root
    if root:
        if frm == '-sys':
            if what == '-fs':
                sh['fs'] = new
            elif what == '-n':
                sh['name'] = new
            elif what == '-v':
                sh['ver'] = new
            elif what == '-root':
                if new.lower() == 'true':
                    root = True
                else:
                    root = False
            elif what == '-tps':
                if new.startswith('-a'):
                    tps.append(new.replace('-a', '').strip())
            elif what == '-utps':
                if new.startswith('-a'):
                    utps.append(new.replace('-a', '').strip())
            elif what == '-ftps':
                if new.startswith('-a'):
                    ftps.append(new.replace('-a', '').strip())
        else:
            er(list(errs)[1], f'{frm} {what}', 'p', 'w', errs[list(errs)[1]][8])
    else:
        col('pd')

def conv(to, what):
    if what in vrs:
        if to == 'str':
            vrs[what] = {'str': spl(vrs[what]).partition(':')[2].strip()}
        elif to == 'int':
            vrs[what] = {'int': spl(vrs[what]).partition(':')[2].strip()}
        elif to == 'float':
            vrs[what] = {'float': spl(vrs[what]).partition(':')[2].strip()}
    else:
        if to == 'str':
            print(str(what))
            return str(what)
        elif to == 'int':
            print(int(what))
            return int(what)
        elif to == 'float':
            print(float(what))
            return float(what)

def mah(mod, ex):
    a = list(ex)
    for i in a:
        if i in vrs:
            c = vrs[i]
            if list(c.keys())[0] == 'int' or list(c.keys())[0] == 'float':
                a[a.index(i)] = i.replace(i, list(c.values())[0])
    c = ''.join(a)
    try:
        v = str(eval(compile(c, 'string', 'eval')))
        if v.endswith('.0'):
            v = v.replace('.0', '')
        else:
            v = v
        if mod == 'fact':
            try:
                print(math.factorial(int(v)))
            except ValueError:
                if isfloat(v):
                    er('MathError', v, 'p', 'w', 'FloatFactorial')
                elif v.startswith('-'):
                    er('MathError', v, 'p', 'w', 'NegativeFactorial')
        elif mod == 'def':
            print(v)
    except ZeroDivisionError:
        er('MathError', c, 'p', 'w', 'DivideByZero')
    
def cut(i1, i2, what):
    print(what[int(i1) - 1:int(i2)])

def logs(what):
    logs = open('logs.tc', 'a+')
    logs.seek(0)
    if logs.readline().startswith('#tc/logs'):
        logs.write(what + '\n')
    else:
        er('FoundError', 'logs.tc', 'p', 'w', 'NoFoundSystemFile')

def traim(frm, what):
    if frm == '-l':
        if what in vrs:
            print(spl(str(list(vrs.values())[0])).partition(':')[2].lstrip())
        else:
            print(what.lstrip())
    elif frm == '-r':
        if what in vrs:
            print(spl(str(list(vrs.values())[0])).partition(':')[2].rstrip())
        else:
            print(what.rstrip())
    elif frm == '-a':
        if what in vrs:
            print(spl(str(list(vrs.values())[0])).partition(':')[2].strip())
        else:
            print(what.strip())
    else:
        er('FoundError', frm, 'p', 'w', errs['FoundError'][1])

def xc(whatst, name, act):
    if whatst == '-void':
        os.chdir('./funcs/')
        info = open(name, 'r')
        info.seek(0)
        name = info.readline().partition(' = ')[2]
        version = info.readline().partition(' = ')[2]
        file = info.readline().partition(' = ')[2]
        if act == 'st':
            if file.endswith('.py'):
                os.system(f'python {file}')

            elif file.endswith('.tcy'):
                lang.lag(file)
    os.chdir('..')    
    