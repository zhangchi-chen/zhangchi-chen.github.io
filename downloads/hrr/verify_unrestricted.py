"""Exact checks for Section 3 of main.tex. Run with Python 3 and SymPy."""
from itertools import combinations
import sympy as sp

t = sp.symbols("t")


def add(*forms):
    result = {}
    for form in forms:
        for mask, coefficient in form.items():
            result[mask] = sp.expand(result.get(mask, 0) + coefficient)
    return {m: c for m, c in result.items() if c != 0}


def scale(c, form):
    return {m: sp.expand(c * x) for m, x in form.items() if c * x != 0}


def wedge(left, right):
    result = {}
    for a, x in left.items():
        for b, y in right.items():
            if a & b:
                continue
            inversions = sum(
                bin(b & ((1 << i) - 1)).count("1")
                for i in range(a.bit_length()) if a & (1 << i)
            )
            result[a | b] = sp.expand(
                result.get(a | b, 0) + (-1)**inversions * x * y
            )
    return {m: c for m, c in result.items() if c != 0}


def power(form, exponent):
    result = {0: sp.Integer(1)}
    for _ in range(exponent):
        result = wedge(result, form)
    return result


def forms(n):
    # Bits 0,...,n-1 are dz; bits n,...,2n-1 are dbar z.
    def E(i, j):
        return {(1 << i) | (1 << (n + j)): sp.I / 2}
    V = [E(i, i) for i in range(n)]
    B = [
        [add(V[0], V[2]), add(E(0, 1), E(2, 3))],
        [add(E(1, 0), E(3, 2)), add(V[1], V[3])],
    ]
    eta = add(E(0, 2), scale(-1, E(2, 0)),
              E(1, 3), scale(-1, E(3, 1)))
    return V, B, eta


V, B, eta = forms(4)
theta_U = add(*V)
det_B = add(wedge(B[0][0], B[1][1]),
            scale(-1, wedge(B[0][1], B[1][0])))
assert not add(wedge(eta, det_B),
               scale(sp.Rational(1, 2), wedge(eta, power(theta_U, 2))))
assert not wedge(eta, power(theta_U, 3))
assert eta
print("Two exterior identities, with the i/2 normalization: PASS")

# Construct the determinant directly from the 2x2 block and scalar blocks.
# These finite checks supplement the all-rank binomial argument in the text.
for k in range(2, 6):
    n = k + 2
    V, B, eta = forms(n)
    theta = add(*V)
    theta_U, theta_W = add(*V[:4]), add(*V[4:])
    block = [
        [add(theta, scale(t, B[0][0])), scale(t, B[0][1])],
        [scale(t, B[1][0]), add(theta, scale(t, B[1][1]))],
    ]
    det_block = add(wedge(block[0][0], block[1][1]),
                    scale(-1, wedge(block[0][1], block[1][0])))
    determinant = wedge(det_block, power(theta, k - 2))
    coefficient = sp.binomial(k, 2) + (k - 1)*t - t**2/2
    expected = scale(coefficient, wedge(
        wedge(eta, power(theta_U, 2)), power(theta_W, k - 2)))
    assert not add(wedge(eta, determinant), scale(-1, expected))

    # Nakano coefficient tensor of the displayed matrix.
    w1, w2 = sp.zeros(k*n, 1), sp.zeros(k*n, 1)
    w1[0] = w1[n+1] = 1
    w2[2] = w2[n+3] = 1
    P = w1*w1.T + w2*w2.T
    assert P.rank() == 2 and P**2 == 2*P
    # I+tP has eigenvalues 1 and 1+2t, hence is positive for t>=0.
print("Direct determinants and Nakano tensors for k=2,3,4,5: PASS")

k = sp.symbols("k", integer=True, positive=True)
tk = k - 1 + sp.sqrt((k - 1)*(2*k - 1))
assert sp.expand(k*(k-1)/2 + (k-1)*tk - tk**2/2) == 0
print("All-rank scalar root t_k: PASS")
print("ALL CHECKS PASSED.")
