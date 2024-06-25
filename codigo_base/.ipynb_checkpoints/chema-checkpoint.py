def fa_grouped(datos, lim_inf, lim_sup):

    fa = [0] * len(lim_inf)
    
    clases = [0] * len(lim_inf)
    
    for i in range(len(lim_inf)):
        clases[i] = i + 1 
    
    for dato in datos:
        for j in range(0, len(lim_inf)):
            # Para crear la otra distribucion se cambian las contidiones
            if j == len(lim_inf)-1:
                if lim_inf[j] <= dato <= lim_sup[j]:
                    fa[j] += 1
                    break
            else:
                if lim_inf[j] <= dato < lim_sup[j]:
                    fa[j] += 1
                    break
    return fa, clases