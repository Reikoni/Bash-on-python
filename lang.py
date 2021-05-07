import main as m

def lag(file):
    f = open(file, 'r')
    s = f.read()
    ln = s.split(';')
    for ls in ln:
        w = ls.replace('\n', '').split(' ')

        if w[0] == 'wrt':
            m.wrt(m.spl(w[1:]))

        elif w[0] == 'ln':
            m.ln(m.spl(w[1:]))

        elif w[0] == 'sudo':
            m.sudo('1', 1)
        
        elif w[0] == 'lef':
            m.lef(w[1], m.spl(w[3:]))

        elif w[0] == 'tp':
            m.tp(m.spl(w[1:]))

        elif w[0] == '.':
            m.ex()

        elif w[0] == 'clr':
            m.col(m.spl(w[4:]), w[2], w[3], w[1])

        elif w[0] == 'xcer':
            m.er(w[1], m.spl(w[2:]), 'p', 'm')

        elif w[0] == 'file':
            m.fil(w[1], w[2], m.spl(w[3:]))
        
        elif w[0] == 'cls':
            m.cls()

        elif w[0] == 'man' or w[0] == 'manual':
            m.manual(w[1])

        elif w[0] == 'mnt': 
            m.mnt(w[1], w[2], m.spl(w[3:]))

        elif w[0] == 'cnv':
            m.conv(w[1], m.spl(w[2:]))

        elif w[0] == 'math':
            m.mah('def', m.spl(w[1:]))
        elif w[0] == 'math.fact':
            m.mah('fact', m.spl(w[1:]))

        elif w[0] == 'wrts':
            m.wrts(m.spl(w[1:]))

        elif w[0] == 'cut':
            m.cut(w[1], w[2], m.spl(w[3:]))

       # else:
       #     m.er(list(m.errs)[1], f'{m.spl(w[0:])}', 'p', 'w', m.errs[list(m.errs)[1]][10])