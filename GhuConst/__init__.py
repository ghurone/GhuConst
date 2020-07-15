"""
GhuConst v0.1 - Fundamental Physical Constants and their units
-------------------------------------------------------------------------

Built-in physical constants
-------------------------------------------------------------------------
c                                   speed o light in vacuum
mu_0                                vacuum mag. permeability
epsilon_0                           vacuum electric permittivity
Z_0                                 characteristic impedance of vacuum
G                                   Newtonian constant of gravitation
g_iag                               gravity measured at IAG-USP
h                                   Planck constant
hbar                                Planck constant / 2 * pi
e                                   elementary charge
elementary_charge                   elementary charge
R                                   molar gas constant
Avogadro                            Avogadro constant
Boltzmann                           Boltzmann constant
Stefan-Boltzmann                    Stefan-Boltzmann constant
Bohr_Radius                         Bohr radius
atm                                 standard atmosphere
Wien                                Wien Constant (wavelength)
Rydberg                             Rydberg Constant
mass_electron                       electron mass
mass_proton                         proton mass
mass_neutron                        neutron mass
mass_muon                           muon mass
mass_tau                            tau mass
mass_deuteron                       deuteron mass
mass_triton                         triton mass
mass_helion                         helion mass
mass_alpha_p                        alpha particle mass
mass_atomic                         atomic mass constant
-------------------------------------------------------------------------

Constants Database
-------------------------------------------------------------------------
    All data was taken from CODATA, you can enter their
website for more information.

http://physics.nist.gov/constants

    Also, you can take a look at the full list of constants.

https://physics.nist.gov/cuu/Constants/Table/allascii.txt

-------------------------------------------------------------------------

Constants's Functions
-------------------------------------------------------------------------
    The "name" parameter is the name of the constant in CODATA list.
This name can be found in the complete list (link above)

    val(name): returns constant's value
        example:
            val('conductance quantum') = > returns 7.748091729e-5

    unit(name): returns constant's unit
        example:
            unit('speed of light in vacuum') = > returns m s^-1

    uncertainty(name): returns constant's uncertainty
        example:
            uncertainty('Planck constant') = > returns 0.0

    If any function returns the number 0 with the type int, it means that
the name you entered is wrong or not in the list. When the function needs
to return the number 0, the type returned is float
-------------------------------------------------------------------------

Temperature Functions
-------------------------------------------------------------------------
The "number" parameter is the temperature value you want to convert

c_to_f(number)          Convert Celsius to Fahrenheit
f_to_c(number)          Convert Fahrenheit to Celsius
c_to_k(number)          Convert Celsius to Kelvin
k_to_c(number)          Convert Kelvin to Celsius
f_to_k(number)          Convert Fahrenheit to Kelvin
k_to_f(number)          Convert Kelvin to Fahrenheit
"""
from .const import *
