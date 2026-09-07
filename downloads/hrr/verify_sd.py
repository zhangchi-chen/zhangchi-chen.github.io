"""Section 5 seed case: n=6, k=2 under SD (main-2.tex).
Run with Python 3 and SymPy, or paste into SageMathCell in Python mode.
The named seed check verifies positive definite coefficients and a nonzero kernel.
Additional exact identities support the rank extension proved in the paper.
"""
from itertools import combinations
import sympy as sp

t, x, y, z = sp.symbols("t x y z")
S1 = sp.diag(1, -1)
S2 = sp.Matrix([[-1, sp.sqrt(3)], [sp.sqrt(3), 1]]) / 2
S3 = sp.Matrix([[-1, -sp.sqrt(3)], [-sp.sqrt(3), 1]]) / 2
for S in (S1, S2, S3):
    assert S**2 == sp.eye(2) and sp.trace(S) == 0
matrix = sum(((sp.eye(2)+sp.sqrt(t)*S)*a
              for S, a in zip((S1, S2, S3), (x, y, z))), sp.zeros(2))
A = x*x+y*y+z*z
B = x*y+x*z+y*z
assert sp.expand(matrix.det() - ((1-t)*A+(2+t)*B)) == 0


def reduce_polynomial(f):
    # W_j^3=0: discard monomials containing a cube.
    return sp.Poly.from_dict(
        {a: c for a, c in sp.Poly(sp.expand(f), x, y, z).terms()
         if max(a) < 3}, (x, y, z)
    ).as_expr()


assert reduce_polynomial(B**2-A**2/2-2*A*B) == 0
u = sp.symbols("u")
assert reduce_polynomial(
    (A+2*u*B)*(B-u*A)-(1+4*u-2*u*u)*A*B) == 0
print("Determinant and identities with W_j^3=0: PASS")


def q(i, j, parameter):
    return 2*(1-parameter) if i//2 == j//2 else 2+parameter


def D(m, parameter):
    pairs = list(combinations(range(m+6), 2))
    def entry(R, S):
        if set(R) & set(S):
            return 0
        return sum(q(a, b, parameter)
                   for a, b in combinations(range(6), 2)
                   if not ({a, b} & (set(R) | set(S))))
    return sp.Matrix([[entry(R, S) for S in pairs] for R in pairs])


factor = (2**15 * 3**6 * (1-t)**3 * (2*t+1)**3
          * (t*t+t+1)**2 * (t*t+4*t-2))
for value in range(16):
    assert D(0, value).det() == factor.subs(t, value)
print("15x15 determinant factorization (16 exact values, degree <=15): PASS")

tstar, ustar = sp.sqrt(6)-2, 1+sp.sqrt(6)/2
pairs6 = list(combinations(range(6), 2))
kernel = sp.Matrix([-2*ustar if i//2 == j//2 else 1
                    for i, j in pairs6])
assert all(sp.simplify(c) == 0 for c in D(0, tstar)*kernel)
assert tstar.is_positive is True
assert (sp.Rational(1, 2)-tstar).is_positive is True
assert any(c != 0 for c in kernel)
for S in (S1, S2, S3):
    coefficient = sp.eye(2)+sp.sqrt(tstar)*S
    assert coefficient == coefficient.conjugate().T
    assert coefficient[0, 0].is_positive is True
    assert sp.simplify(coefficient.det()-(1-tstar)) == 0
assert (1-tstar).is_positive is True
print("Section 5 seed (n=6, k=2): positive definite SD coefficients and nonzero kernel: PASS")

# The text proves these counting identities for every m.
# Check the full matrices at three successive sizes, symbolically in t.
for m in range(3):
    n = m + 6
    pairs = list(combinations(range(n), 2))
    L = sp.Matrix([[int(i in R) for i in range(n)] for R in pairs])
    dm = D(m, t)
    R = sp.Matrix(n, n, lambda i, j: 0 if i == j else sum(
        q(a, b, t) for a, b in combinations(range(6), 2)
        if not ({a, b} & {i, j})))
    explicit_R = sp.Matrix(n, n, lambda i, j:
        0 if i == j else
        (12 if i//2 == j//2 else 12+3*t) if max(i, j) < 6 else
        4*(5+t) if min(i, j) < 6 else 6*(5+t))
    assert sp.expand(R-explicit_R) == sp.zeros(n)
    assert sp.expand(L.T*dm*L-(m+1)*(m+2)*R) == sp.zeros(n)
    block = dm.row_join(dm*L/(m+1)).col_join(
        (L.T*dm/(m+1)).row_join(sp.zeros(n)))
    change = sp.eye(len(pairs)).row_join(-L/(m+1)).col_join(
        sp.zeros(n, len(pairs)).row_join(sp.eye(n)))
    assert sp.expand(change.T*block*change-sp.diag(
        dm, -sp.Rational(m+2, m+1)*R)) == sp.zeros(len(pairs)+n)
    pairs_next = list(combinations(range(n+1), 2))
    order = [pairs_next.index(R) for R in pairs]
    order += [pairs_next.index((i, n)) for i in range(n)]
    assert sp.expand(D(m+1, t).extract(order, order)-block) == sp.zeros(len(order))
print("Rank-extension matrix identities for m=0,1,2, symbolically in t: PASS")

m = sp.symbols("m", integer=True, positive=True)
assert sp.expand(12-2*(12+3*t)+6*(2+t)) == 0
Q = 2*(5+t)*sp.Matrix([[6, 2*m], [12, 3*(m-1)]])
assert sp.expand(Q.det()+24*(m+3)*(5+t)**2) == 0
assert factor.subs(t, 0) < 0 < factor.subs(t, sp.Rational(1, 2))
print("All-m quotient determinant and endpoint signs: PASS")
print("ALL CHECKS PASSED.")
