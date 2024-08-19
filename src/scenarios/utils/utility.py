
import numpy as np

def get_vel( r, a, MU ):

    v = np.sqrt( 2*MU/r - MU/a )

    return v

def get_vels( r_p, r_a, MU ):
    a = (r_p + r_a)/2
    v_p = get_vel( r_p, a, MU )
    v_a = get_vel( r_a, a, MU )
    return (v_p,v_a)

def r2d( a ):
    return a * 180 / np.pi

def get_apo( r_p, v_p, MU ):
    a = MU/(2*MU/r_p - v_p**2)
    e = 1 - r_p/a
    r_a = a * (1 + e)
    return r_a


### Rocket Equation
def rocket_equation( dv, m0, Isp, g0 ):
    # dv = Isp * g0 * np.log(m0/mf)
    mf = m0 / np.exp( dv / (Isp * g0) )
    return mf

### Rocket Equation
def mass_fraction( dv, Isp, g0 ):
    # dv = Isp * g0 * np.log(m0/mf)
    m0_over_mf = np.exp( dv / (Isp * g0) )
    return m0_over_mf

