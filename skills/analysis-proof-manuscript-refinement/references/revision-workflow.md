# Proof Revision Workflow

Use this reference for a substantial audit or revision of an existing proof.
The goal is to improve correctness and exposition without enlarging the claim.

## 1. Freeze the Contract

Record, when applicable:

```text
Editable material:
Protected statements and notation:
Read-only context:
Permitted mathematical changes:
Build or validation commands:
Unavailable checks:
```

If the request is review-only, produce findings rather than edits. If the
scope is unusually strict and files are available, use a diff or checksum to
confirm that protected material did not change.

## 2. Map the Argument Backward

Begin with the stated conclusion and identify the minimal load-bearing
dependency chain that genuinely supports it:

```text
claimed conclusion
  <- final implication or estimate
  <- decisive intermediate statement
  <- hypotheses and earlier results
```

Record any gap where the manuscript supplies no valid implication. Do not hide
such a gap by improving the surrounding prose.

## 3. Track the Load-Bearing Steps

For a long, complex, or disputed proof, build an explicit ledger for the
load-bearing steps. For a short proof, apply the same questions directly
without materializing the table.

| Item | Audit question |
|---|---|
| Goal | What exact statement must this step establish? |
| Inputs | Which hypotheses, definitions, and earlier results are used? |
| Type | Is the step an identity, implication, bound, equivalence, or limit? |
| Quantities | Which constants, signs, ranges, or normalizations matter? |
| Discarded parts | What property makes each omitted contribution harmless? |
| Passage | What theorem or convergence principle justifies the operation? |
| Downstream use | Where is the result used, and in what exact form? |

Do not begin stylistic compression until the load-bearing ledger closes.

## 4. Audit Correctness

Check the points relevant to the proof:

- domains, types, dimensions, quantifiers, and boundary cases;
- definitions before use and consistency of notation;
- equality versus inequality and one-way versus two-way implication;
- signs, constants, dependence on parameters, and uniformity claims;
- exchanges of limits, sums, derivatives, integrals, or expectations;
- use of compactness, completeness, measurability, regularity, or positivity;
- exceptional sets and the mode of convergence;
- exact hypotheses and conclusions of cited results;
- the final bridge from the intermediate statement to the theorem.

If a claim cannot be justified from the available material, mark it as an open
gap and state what additional fact would close it.

## 5. Choose the Necessary Resolution

Determine whether the conclusion needs an exact formula, a one-sided estimate,
an equivalence, or only a leading-order statement. Preserve a more detailed
calculation when it is reused or independently informative; otherwise keep the
main proof at the lowest resolution that still proves the claim.

Do not remove a contribution merely because it is inconvenient. State the
sign, estimate, cancellation, domination, or absorption that makes it
dispensable. Define a remainder by the mathematical property that controls it,
not only as the difference between two displayed expressions.

## 6. Improve the Exposition

Keep the active mathematical object visible through a calculation. Use prose
to state purpose, invoke a theorem, explain a non-obvious implication, or mark
a change of case. Use formulas when they make a chain of reasoning easier to
check.

Promote a repeated mechanism to a lemma only when it is reused or has
independent conceptual value. Split a long result when its parts use different
proof mechanisms or are cited independently; length alone is not a reason to
split it.

## 7. Control Notation and Terminology

Prefer established notation. Introduce a symbol when it reduces repeated
complexity enough to justify the lookup cost and does not conflict with the
surrounding manuscript. Remove one-use aliases and provisional terminology
that does not represent a stable mathematical concept.

Preserve nonstandard terminology when the author intentionally defines it and
it performs real work. Do not present an internal working label as established
literature terminology.

## 8. Reverse-Audit and Report

Read backward from the conclusion. Confirm that every implication is supported,
every referenced statement has the asserted content, and every auxiliary term
has already received the bound or property used later.

Report:

- what is now established;
- any unresolved gap or conditional step;
- constants, signs, hypotheses, or ranges that changed;
- compression, notation, or structural changes;
- validation performed and validation unavailable.
