import numpy as np
def payoff(path, product, S):
    stock = 0
    nb_coupons = 0
    matur = 0
    recalled = False 
    for i, St in enumerate(path):
        if St >= S * product.autocall_barrier :
            payoff = product.nominal * (1 + product.coupon_rate * (stock +1))
            recalled = True 
            matur = product.observation_dates[i]
            break 
        elif St >= S * product.coupon_barrier :
            nb_coupons+= stock +1 
            stock = 0 
        else:
            stock += 1
            
    pdi_breached = np.any(path < S* product.protection_barrier)
    if not recalled :
        matur = product.maturity
        if pdi_breached :
            payoff = (St/ S) * product.nominal
        else : 
            payoff = product.nominal * ( 1+ product.coupon_rate * (nb_coupons + stock))
    return payoff, matur
    