# -*- coding: utf-8 -*-
'''Chemical Engineering Design Library (ChEDL). Utilities for process modeling.
Copyright (C) 2021 Caleb Bell <Caleb.Andrew.Bell@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.'''

from __future__ import division
from fluids.numerics.special import py_cacos, py_catanh, py_hypot, trunc_exp, trunc_log
from fluids.numerics import assert_close
from math import hypot, exp, isnan, isinf, log

def test_hypot():
    values = [(.5, -1), (-.5, 1), (100, -100), (-100, 100)]
    rtol = 1e-14
    for (x, y) in values:
        assert_close(py_hypot(x, y), hypot(x, y), rtol=rtol)
        
        
def test_trunc_exp():
    for v in (-1e100, -1e-10, -1e-1, 0.0, 0.1, 10.0, 300.0, 709.782712893384):
        assert_close(trunc_exp(v), exp(v), atol=0.0, rtol=0.0)
        
    assert trunc_exp(1000.0) >= exp(709.0)
    assert not isnan(trunc_exp(1000.0))
    assert not isinf(trunc_exp(1000.0))
    
def test_trunc_log():
    for v in (5e-324, 1e-100, 1e-10, 0.1, 10.0, 300.0, 1e10, 1e100, 3e300):
        assert_close(trunc_log(v), log(v), atol=0.0, rtol=0.0)

    assert not isnan(trunc_log(0.0))
    assert not isinf(trunc_log(0.0))
    assert trunc_log(0.0) < trunc_log(1e-100)

def test_py_cacos():
    # Missed a asinh in this case
    assert_close(py_cacos(1.0000000000000033), 8.16170211889097e-08j, rtol=1e-11)

def test_py_catanh():
    from cmath import atanh as catanh

    tests = [(-9.8813129168249309e-324, 0.0),
    (-9.8813129168249309e-324, -0.0),
    (-1e-305, 0.0),
    (-1e-305, -0.0),
    (-1e-150, 0.0),
    (-1e-150, -0.0),
    (-9.9999999999999998e-17, 0.0),
    (-9.9999999999999998e-17, -0.0),
    (-0.001, 0.0),
    (-0.001, -0.0),
    (-0.57899999999999996, 0.0),
    (-0.57899999999999996, -0.0),
    (-0.99999999999999989, 0.0),
    (-0.99999999999999989, -0.0),
    (-1.0000000000000002, 0.0),
    (-1.0000000000000002, -0.0),
    (-1.0009999999999999, 0.0),
    (-1.0009999999999999, -0.0),
    (-2.0, 0.0),
    (-2.0, -0.0),
    (-23.0, 0.0),
    (-23.0, -0.0),
    (-10000000000000000.0, 0.0),
    (-10000000000000000.0, -0.0),
    (-9.9999999999999998e+149, 0.0),
    (-9.9999999999999998e+149, -0.0),
    (-1.0000000000000001e+299, 0.0),
    (-1.0000000000000001e+299, -0.0),
    (9.8813129168249309e-324, 0.0),
    (9.8813129168249309e-324, -0.0),
    (1e-305, 0.0),
    (1e-305, -0.0),
    (1e-150, 0.0),
    (1e-150, -0.0),
    (9.9999999999999998e-17, 0.0),
    (9.9999999999999998e-17, -0.0),
    (0.001, 0.0),
    (0.001, -0.0),
    (0.57899999999999996, 0.0),
    (0.57899999999999996, -0.0),
    (0.99999999999999989, 0.0),
    (0.99999999999999989, -0.0),
    (1.0000000000000002, 0.0),
    (1.0000000000000002, -0.0),
    (1.0009999999999999, 0.0),
    (1.0009999999999999, -0.0),
    (2.0, 0.0),
    (2.0, -0.0),
    (23.0, 0.0),
    (23.0, -0.0),
    (10000000000000000.0, 0.0),
    (10000000000000000.0, -0.0),
    (9.9999999999999998e+149, 0.0),
    (9.9999999999999998e+149, -0.0),
    (1.0000000000000001e+299, 0.0),
    (1.0000000000000001e+299, -0.0),
    (-0.54460925980633501, -0.54038050126721027),
    (-1.6934614269829051, -0.48807386108113621),
    (-1.3467293985501207, -0.47868354895395876),
    (-5.6142232418984888, -544551613.39307702),
    (-0.011841460381263651, -3.259978899823385),
    (-0.0073345736950029532, 0.35821949670922248),
    (-13.866782244320014, 0.9541129545860273),
    (-708.59964982780775, 21.984802159266675),
    (-30.916832076030602, 1.3691897138829843),
    (-0.57461806339861754, 0.29534797443913063),
    (0.40089246737415685, -1.632285984300659),
    (2119.6167688262176, -1.5383653437377242e+17),
    (756.86017850941641, -6.6064087133223817),
    (4.0490617718041602, -2.5784456791040652e-12),
    (10.589254957173523, -0.13956391149624509),
    (1.0171187553160499, 0.70766113465354019),
    (0.031645502527750849, 0.067319983726544394),
    (0.13670177624994517, 0.43240089361857947),
    (0.64173899243596688, 2.9008577686695256),
    (0.19313813528025942, 38.799619150741869),
    (5.3242646831347954e+307, 1.3740396080084153e+308),
    (1.158701641241358e+308, -6.5579268873375853e+307),
    (-1.3435325735762247e+308, 9.8947369259601547e+307),
    (-1.4359857522598942e+308, -9.4701204702391004e+307),
    (0.0, 5.6614181068098497e+307),
    (-0.0, 6.9813212721450139e+307),
    (0.0, -7.4970613060311453e+307),
    (-0.0, -1.5280601880314068e+308),
    (8.2219472336000745e+307, 0.0),
    (1.4811519617280899e+308, -0.0),
    (-1.2282016263598785e+308, 0.0),
    (-1.0616427760154426e+308, -0.0),
    (1.2971536510180682e+308, 5.2847948452333293),
    (1.1849860977411851e+308, -7.9781906447459949),
    (-1.4029969422586635e+308, 0.93891986543663375),
    (-4.7508098912248211e+307, -8.2702421247039908),
    (8.2680742115769998, 8.1153898410918065e+307),
    (1.2575325146218885, -1.4746679147661649e+308),
    (-2.4618803682310899, 1.3781522717005568e+308),
    (-4.0952386694788112, -1.231083376353703e+308),
    (3.8017563659811628e-314, 2.6635484239074319e-312),
    (1.7391110733611878e-321, -4.3547800672541419e-313),
    (-5.9656816081325078e-317, 9.9692253555416263e-313),
    (-6.5606671178400239e-313, -2.1680936406357335e-309),
    (0.0, 2.5230944401820779e-319),
    (-0.0, 5.6066569490064658e-320),
    (0.0, -2.4222487249468377e-317),
    (-0.0, -3.0861101089206037e-316),
    (3.1219222884393986e-310, 0.0),
    (9.8926337564976196e-309, -0.0),
    (-1.5462535092918154e-312, 0.0),
    (-9.8813129168249309e-324, -0.0),
    (1.0, 1e-153),
    (1.0, 9.9999999999999997e-155),
    (-1.0, 1e-161),
    (1.0, -1e-165),
    (-1.0, -9.8813129168249309e-324)]


    rtol = 1e-13
    atol = 0.0
    for (real, imag) in tests:
        res_good = catanh(real + imag*1j)
        res_implemented = py_catanh(real + imag*1j)
        assert_close(res_good.real, res_implemented.real, rtol=rtol, atol=atol)
        assert_close(res_good.imag, res_implemented.imag, rtol=rtol, atol=atol)
        # Windows 2.7 fails on Appveyor
#        assert res_good.real == res_implemented.real
#        assert res_good.imag == res_implemented.imag


