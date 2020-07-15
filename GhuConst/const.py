from math import pi

from .data import val, unit, uncertainty

# Physical Constants
c = val('speed of light in vacuum')
mu_0 = 4 * pi * 1e-7
epsilon_0 = 1 / (c ** 2 * mu_0)
Z_0 = mu_0 * c  # Characteristic impedance of vacuum
G = val('Newtonian constant of gravitation')
g_iag = 9.7864137  # gravity measured at IAG-USP
h = val('Planck constant')
hbar = h / (2 * pi)
e = elementary_charge = val('elementary charge')
R = val('molar gas constant')
Avogadro = val('Avogadro constant')
Boltzmann = val('Boltzmann constant')
Stefan_Boltzmann = val('Stefan-Boltzmann constant')
Bohr_Radius = val('Bohr radius')
atm = val('standard atmosphere')
Wien = val('Wien wavelength displacement law constant')
Rydberg = val('Rydberg constant')

# Some mass
mass_electron = val('electron mass')
mass_proton = val('proton mass')
mass_neutron = val('neutron mass')
mass_muon = val('muon mass')
mass_tau = val('tau mass')
mass_deuteron = val('deuteron mass')
mass_triton = val('triton mass')
mass_helion = val('helion mass')
mass_alpha_p = val('alpha particle mass')
mass_atomic = val('atomic mass constant')


# Prefixes in SI
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3
hecto = 1e2
deka = 1e1
deci = 1e-1
centi = 1e-2
milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21


# bool
earth_is_round = True  # I don't care if the earth is not perfectly round, it's just a joke.
earth_is_flat = False  # KKKKK BURRÃO


# Temperature converter
def c_to_f(tempe):
    """Receives a temperature in Celsius and returns in Fahrenheit"""
    return 1.8 * tempe + 32


def f_to_c(tempe):
    """Receives a temperature in Fahrenheit and returns in Celsius"""
    return (tempe - 32) / 1.8


def c_to_k(tempe):
    """Receives a temperature in Celsius and returns in Kelvin"""
    return tempe + 273.15


def k_to_c(tempe):
    """Receives a temperature in Kelvin and returns in Celsius"""
    return tempe - 273.15


def f_to_k(tempe):
    """Receives a temperature in Fahrenheit and returns in Kelvin"""
    return (tempe - 32) * 5 / 9 + 273.15


def k_to_f(tempe):
    """Receives a temperature in Kelvin and returns in Fahrenheit"""
    return (tempe - 275.5) * 9 / 5 + 32
