# Phoenix Structured Product Pricer

A Monte Carlo pricer for Phoenix autocallable structured products, built from scratch in Python.

## Description

This project implements a full pricing engine for Phoenix structured products. The pricer simulates thousands of price trajectories using Geometric Brownian Motion (GBM) and applies the Phoenix payoff mechanics on each trajectory to compute a fair value via Monte Carlo.

## Features

- **GBM Simulation** : Vectorised exact discretisation (no Euler bias) using NumPy
- **Full Phoenix Mechanics** : Autocall barrier, coupon barrier, PDI (Put Down-and-In), memory effect
- **Monte Carlo Pricing** : Risk-neutral pricing with continuous discounting
- **Modular Architecture** : Clean separation between product definition, simulation, and pricing

## Project Structure

```
Phoenix/
├── dataClass_Phoenix.py   # PhoenixProduct dataclass with parameter validation
├── simul_gbm.py           # GBM trajectory simulator (generic, reusable)
├── Calc_Payoff.py         # Phoenix payoff mechanics
└── Price_Phoenix.ipynb    # Main pricing notebook
```

## Product Mechanics

At each observation date, the following checks are applied in order:

1. **Autocall** : If spot ≥ autocall barrier × S0 → product recalled, investor receives nominal + coupons (including memory)
2. **Coupon** : If spot ≥ coupon barrier × S0 → coupon paid, memory reset
3. **Below coupon barrier** : No coupon paid, memory accumulates (if memory effect enabled)

At maturity (if never recalled):
- **PDI not breached** → full nominal repayment + accumulated coupons
- **PDI breached** → capital at risk, repayment = nominal × (S_T / S_0)

## Installation

```bash
pip install numpy
```

## Usage

```python
from dataClass_Phoenix import PhoenixProduct

# Define the product
product = PhoenixProduct(
    maturity=5.0,
    coupon_barrier=0.70,
    protection_barrier=0.60,
    coupon_rate=0.08
)

# Price it
price = phoenix_price(product, S0=100, r=0.03, sigma=0.20, nb_simulations=10000)
print(f"Prix Phoenix : {price:.2f} €")
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `maturity` | Product maturity in years | required |
| `coupon_barrier` | Coupon barrier as % of S0 | required |
| `protection_barrier` | PDI barrier as % of S0 | required |
| `coupon_rate` | Annual coupon rate | required |
| `nominal` | Nominal value (€) | 1000 |
| `autocall_barrier` | Autocall barrier as % of S0 | 1.0 (100%) |
| `memory_effect` | Enable coupon memory | True |

## Example Results

Standard Phoenix (sigma=20%, r=3%, coupon=8%, barriers: 100%/70%/60%) prices around **950-1000€** on a 1000€ nominal — reflecting the value of the coupon stream net of the capital risk.

