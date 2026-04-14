import numpy as np

def simul_gbm(S,r, sigma, observation_dates, nb_simulations):
    obs = np.array(observation_dates)
    nb_dates = len(obs)
    dt = np.diff(np.append(0,obs))
    Z = np.random.standard_normal((nb_simulations, nb_dates))
    log_returns = (r-(sigma**2)/2)*dt + sigma * np.sqrt(dt)*Z
    cum_log = np.cumsum(log_returns, axis = 1)
    paths = S * np.exp(cum_log)
    return paths

    
    