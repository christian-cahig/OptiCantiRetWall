"""
Core functionalities for the repository github.com/christian-cahig/OptiCantiRetWall

(c) 2026, Christian Cahig
"""

import math as mt

__author__ = "Christian Cahig"
__version__ = "0.3.0"
__all__ = [
    "Fa_MazGanj",
    "Fp_MazGanj",
    "Qb_linear",
]

WALL_PROPS_KEYS = {
    "b_t",  # Toe length
    "b_h",  # Heel length
    "b_sb", # Stem width at base
    "b_st", # Stem width at tip
    "b_f",  # Footing width
    "h_s",  # Stem height
    "h_f",  # Footing thickness
    "x_k",  # Shear key location (from toe tip)
    "b_k",  # Shear key width
    "h_k",  # Shear key height
}
DEV_WEIGHT_KEYS = {"mag", "loc"}
LAT_FORCES_KEYS = {"mag", "ang", "loc"}
SOIL_QDIST_KEYS = {"min", "max", "ecc", "Mr", "Mo"}

def Fa_Rankine(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); theta = 0.0
    
    Ka = (1 - mt.sin(phi_)) / (1 + mt.sin(phi_))
    Pa = y * Ka * z
    Fa = 0.5 * Pa * z
    Fa = Fa - (2 * c * mt.sqrt(Ka) * z)

    return {"mag" : Fa, "ang" : theta, "loc" : z / 3}

def Fp_Rankine(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); theta = 0.0
    
    Kp = (1 + mt.sin(phi_)) / (1 - mt.sin(phi_))
    Pp = y * Kp * z
    Fp = 0.5 * Pp * z
    Fp = Fp + (2 * c * mt.sqrt(Kp) * z)

    return {"mag" : Fp, "ang" : theta, "loc" : z / 3}

def Fa_ChuRank(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); the_ = mt.radians(theta)
    cphi = mt.cos(phi_); cthe = mt.cos(the_)
    cp2ct2 = mt.sqrt((cthe ** 2) - (cphi ** 2))

    Ka = cthe * (cthe - cp2ct2) / (cthe + cp2ct2)
    Pa = y * Ka * z
    Fa = 0.5 * Pa * z
    Fa = Fa - (2 * c * mt.sqrt(Ka) * z)

    return {"mag" : Fa, "ang" : theta, "loc" : z / 3}

def Fp_ChuRank(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); the_ = mt.radians(theta)
    cphi = mt.cos(phi_); cthe = mt.cos(the_)
    cp2ct2 = mt.sqrt((cthe ** 2) - (cphi ** 2))

    Kp = cthe * (cthe + cp2ct2) / (cthe - cp2ct2)
    Pp = y * Kp * z
    Fp = 0.5 * Pp * z
    Fp = Fp + (2 * c * mt.sqrt(Kp) * z)

    return {"mag" : Fp, "ang" : theta, "loc" : z / 3}

def Fa_MazGanj(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); the_ = mt.radians(theta)
    zc = c / (y * z)
    cts = mt.cos(the_) ** 2
    cp = mt.cos(phi_); cps = cp ** 2
    csp = cp * mt.sin(phi_)

    Ka = (4 * cts * (cts - cps)) + (4 * (zc ** 2) * cps) + (8 * zc * cts * csp)
    Ka = (2 * cts) + (2 * zc * csp) - mt.sqrt(Ka)
    Ka = (Ka / cps) - 1

    Pa = y * Ka * z * mt.cos(the_)
    Fa = 0.5 * Pa * z

    return {"mag" : Fa, "ang" : theta, "loc" : z / 3}

def Fp_MazGanj(
    z : float,
    y : float,
    phi : float,
    c : float = 0.0,
    theta : float = 0.0,
) -> dict[float]:
    phi_ = mt.radians(phi); the_ = mt.radians(theta)
    zc = c / (y * z)
    cts = mt.cos(the_) ** 2
    cp = mt.cos(phi_); cps = cp ** 2
    csp = cp * mt.sin(phi_)

    Kp = (4 * cts * (cts - cps)) + (4 * (zc ** 2) * cps) + (8 * zc * cts * csp)
    Kp = (2 * cts) + (2 * zc * csp) + mt.sqrt(Kp)
    Kp = (Kp / cps) - 1

    Pp = y * Kp * z * mt.cos(the_)
    Fp = 0.5 * Pp * z

    return {"mag" : Fp, "ang" : theta, "loc" : z / 3}

def Qb_linear(
    b : float,
    Fa : dict[float],
    Fg : dict[float],
    Fp : dict[float] = {k : 0.0 for k in LAT_FORCES_KEYS},
) -> dict[float]:
    assert b > 0
    assert set(Fa.keys()) == LAT_FORCES_KEYS
    assert set(Fg.keys()) == DEV_WEIGHT_KEYS
    assert set(Fp.keys()) == LAT_FORCES_KEYS

    bet_ = mt.radians(Fa["ang"])
    Fah = Fa["mag"] * mt.cos(bet_); Fav = Fa["mag"] * mt.sin(bet_)
    bet_ = mt.radians(Fp["ang"])
    Fph = Fp["mag"] * mt.cos(bet_); Fpv = Fp["mag"] * mt.sin(bet_)
    Rh = Fah - Fph
    Rv = Fg["mag"] + Fav + Fpv

    Mr = (Fg["mag"] * Fg["loc"]) + (Fav * b) + (Fph * Fp["loc"])
    Mo = Fah * Fa["loc"]
    x_ = (Mr - Mo) / Rv
    e = (b / 2) - x_

    b6 = b / 6
    qmax = (Rv / b) * (1 + (e / b6)) if mt.fabs(e) <= b6 else (2 * Rv) / (3 * x_)

    return {
        "Rh" : Rh, "Rv" : Rv,
        "Mr" : Mr, "Mo" : Mo,
        "min" : None, "max" : qmax, "ecc" : e,
    }
