def continued_fraction(n: int) -> list:
    if n**0.5 % 1 == 0:
        raise ValueError('Números que são quadrados perfeitos não são aceitos.')
    
    a0 = int(n**0.5) # base do algoritmo
    an = 1
    cf = []
    
    for count in itertools.count():
        if count == 100:
            raise Exception(f"Couldn't converge in less than {count} iterations")

        # Calula Pr, Qr e ar a cada iteração
        if count == 0:
            pr = 0
            qr = 1
        else:
            pr = an * qr - pr
            qr = (n - pr**2) / qr

        an = int((a0 + pr) / qr)
        cf.append(an)

        if an == 2 * a0:
            break
    
    if len(cf) % 2 == 0:
        cf = cf + cf[1:]
    cf = cf[:-1]
    num = 1
    den = 0
    size = len(cf)
    for i in cf[-1::-1]:
        if not den:
            den = i
            continue
        temp = i * den + num
        num = den
        den = temp
    return (den, num)