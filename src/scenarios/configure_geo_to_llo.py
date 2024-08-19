
from astropy.constants import GM_earth as GravitationalParameter
from astropy.constants import R_earth

MU = GravitationalParameter.value # Unit("m3 / (s2)")
RE = R_earth.value # Unit("m")

from utils.utility import get_vel, get_vels, r2d
import numpy as np

###
### Set up initial orbit
###

h_leo = 185e3 # m
h_geo = 36000e3 # m




########
# Initial setup / conversions

R_leo = h_leo + RE
R_geo = h_geo + RE
R_esoi_ref = 924000e3 # https://g.co/gemini/share/830165665f3c
R_msoi_ref = 66100e3 # https://g.co/gemini/share/830165665f3c
R_m = 384400e3
R_esoi = R_esoi_ref/(R_esoi_ref + R_msoi_ref) * R_m
R_msoi = R_msoi_ref/(R_esoi_ref + R_msoi_ref) * R_m

print(f'R_esoi (km) = {R_esoi/1000}, R_msoi (km) = {R_msoi/1000}')


#######
# Compute speeds

v_geo = get_vel( R_geo, R_geo, MU )

print(f'v_geo (km/s) = {v_geo/1000}')


(vp_gto,va_gto) = get_vels( R_leo, R_geo, MU )

print(f'vp_gto (km/s) = {vp_gto/1000}, va_gto (km/s) = {va_gto/1000}')

dv_gto2geo = v_geo - va_gto
print(f'DV GTO 2 GEO = v_geo - va_gto (m/s) = {dv_gto2geo}')


(vp_lti,va_lti) = get_vels( R_leo, R_esoi, MU )

print(f'vp_lti (km/s) = {vp_lti/1000}, va_lti (km/s) = {va_lti/1000}')

dv_gto2lti = vp_lti - vp_gto
print(f'DV GTO 2 LTI = vp_lti - vp_gto (m/s) = {dv_gto2lti}')




#######
# Compute epoch
# 22 Jul 2014 11:29:10.811
# 04 Jul 2024 12:00:00

# RAAN
# 112.8362
# 90

# Intersect:
# 05 Jul 2024 12:00:00
# 150
# Sat Arrives 07-jul-24 11:23
# Moon Arrives 10-jul-24 17:17
# -- Turn forward moon by 3days 6hrs
# .... Turn back RAAN by same
# day2sec = 86400
day2sec = 86164.0905
w_earth = 2*np.pi / day2sec
Wnew = 150 + r2d(w_earth)