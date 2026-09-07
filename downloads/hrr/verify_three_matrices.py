"""Exact checks for Section 5.4 of main.tex. Run with Python 3 and SymPy."""
from itertools import combinations
import sympy as sp

u, v, w = sp.symbols("u v w")
pairs = list(combinations(range(6), 2))


def q(i, j):
    if i//2 == j//2:
        return 2
    return 2*{(0, 1): u, (0, 2): v, (1, 2): w}[(i//2, j//2)]


def entry(R, S):
    if set(R) & set(S):
        return 0
    i, j = sorted(set(range(6)) - set(R) - set(S))
    return q(i, j)


D = sp.Matrix([[entry(R, S) for S in pairs] for R in pairs])


def product(a, sign_a, b, sign_b):
    # (V_2a + sign_a V_(2a+1))(V_2b + sign_b V_(2b+1))/2.
    result = sp.zeros(15, 1)
    for i, ci in [(2*a, 1), (2*a+1, sign_a)]:
        for j, cj in [(2*b, 1), (2*b+1, sign_b)]:
            result[pairs.index(tuple(sorted((i, j))))] = sp.Rational(ci*cj, 2)
    return result


invariant = [
    sp.Matrix([int((i, j) == (2*a, 2*a+1)) for i, j in pairs])
    for a in range(3)
]
invariant += [product(a, 1, b, 1) for a, b in combinations(range(3), 2)]
P0 = sp.Matrix.hstack(*invariant)
T = sp.Matrix([
    [0, 1, 1, 0, 0, 2*w], [1, 0, 1, 0, 2*v, 0],
    [1, 1, 0, 2*u, 0, 0], [0, 0, 2*u, 1, 2*w, 2*v],
    [0, 2*v, 0, 2*w, 1, 2*u], [2*w, 0, 0, 2*v, 2*u, 1],
])
assert P0.T*P0 == sp.eye(6)
assert P0.T*D*P0 == 2*T

columns = invariant[:]
blocks = [2*T]
for a, parameter in enumerate((w, v, u)):
    others = [b for b in range(3) if b != a]
    columns += [product(a, -1, b, 1) for b in others]
    blocks.append(-2*sp.Matrix([[1, 2*parameter], [2*parameter, 1]]))
columns += [product(a, -1, b, -1) for a, b in combinations(range(3), 2)]
blocks.append(2*sp.eye(3))
P = sp.Matrix.hstack(*columns)
assert P.T*P == sp.eye(15)
assert P.T*D*P == sp.diag(*blocks)
print("Full orthogonal block decomposition, dimension 15: PASS")

S = T[3:, 3:] - T[3:, :3]*T[:3, :3].inv()*T[:3, 3:]
expected_S = sp.Matrix([
    [1+2*u*u, 2*w-2*u*v, 2*v-2*u*w],
    [2*w-2*u*v, 1+2*v*v, 2*u-2*v*w],
    [2*v-2*u*w, 2*u-2*v*w, 1+2*w*w],
])
assert S == expected_S
delta = 1+2*u*v*w-u*u-v*v-w*w
F = 36*u*v*w-9+18*delta-8*delta**2
assert sp.expand(S.det()-F) == 0
for i, j in combinations(range(3), 2):
    a, b = [u, v, w][i], [u, v, w][j]
    assert sp.expand(S.extract([i, j], [i, j]).det()
                     -(4*delta+6*a*a+6*b*b-3)) == 0
assert sp.expand(sp.diff(F, w) -
                 (36*u*v+2*(u*v-w)*(18-16*delta))) == 0
assert sp.expand(sp.diff(F, w, 3)-192*(u*v-w)) == 0
print("Schur complement, discriminant, principal minors and derivatives: PASS")

# Two exact feasible endpoints with the two nonsingular inertias.
assert F.subs({u: 1, v: 1, w: 1}) == 27
assert delta.subs({u: 2, v: 2, w: 2}) == 5
assert F.subs({u: 2, v: 2, w: 2}) > 0
assert delta.subs({u: 3, v: 3, w: 3}) == 28
assert F.subs({u: 3, v: 3, w: 3}) < 0
print("Feasible parameters with both signs of F: PASS")
print("ALL CHECKS PASSED.")
