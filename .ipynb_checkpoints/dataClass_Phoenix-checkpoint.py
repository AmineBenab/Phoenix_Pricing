from dataclasses import dataclass, field
import numpy as np

@dataclass
class PhoenixProduct :
    maturity : float
    coupon_barrier : float
    protection_barrier : float
    coupon_rate : float
    nominal : float = 1000
    autocall_barrier : float = 1
    memory_effect : bool = True

    def __post_init__(self):
        self.observation_dates = np.arange(1,self.maturity+1,1)
        assert self.protection_barrier < self.coupon_barrier <= self.autocall_barrier, "Les barrrièes ne sont pas bonnes (protection < coupon < autocall)"

