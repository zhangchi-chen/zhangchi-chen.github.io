# Mathematical Manuscript Structure Audit

Use this reference for a whole paper or a substantial collection of sections.
Settle the manuscript's logical structure before sentence-level polishing.

## 1. Freeze Mathematical Scope

Record the definitions, principal claims, applications, examples, and proofs
that must survive. Identify protected notation, terminology, acknowledgments,
disclosures, files, and any changes that require prior approval.

Distinguish exposition work from new research. Do not solve a structural
problem by silently strengthening or generalizing a theorem.

## 2. Inventory the Manuscript

List sections, theorem-like environments, substantial definitions, examples,
open questions, appendices, and repeated explanatory blocks. For each item,
record:

| Item | Role | Depends on | Used by | Source status | Proposed action |
|---|---|---|---|---|---|
| result or section | main, support, application, background, interpretation | exact prerequisites | later uses | original, standard, or cited | keep, merge, move, demote, or remove |

Search labels and citations when source files are available. Distinguish actual
logical use from a result that is merely announced, compared, or proved later.

## 3. Identify the Logical Spine

Select the small set of claims that would remain in a short research summary.
For each line of argument, trace backward from its final result through the
supporting results and definitions. Arrange the exposition so that readers
encounter prerequisites before substantive use unless a deliberate preview is
needed for motivation.

Do not force every manuscript into one universal section order. Use the order
that best exposes the actual dependency graph and the paper's motivating
problem.

## 4. Evaluate Each Item

Consider:

1. mathematical novelty;
2. load-bearing use in later arguments;
3. independent citation or application value;
4. necessity for understanding a definition, method, or boundary case;
5. duplication elsewhere in the manuscript.

### Keep

Keep principal results, reusable supporting results, sharp statements, and
applications that close an important line of argument.

### Merge

Merge items that have the same role and proof mechanism when separate
statements add visual weight without improving navigation or reuse. Preserve
separate parts when readers are likely to cite them independently.

### Move

Move prerequisites before first substantive use. Move standard background out
of the main line when it interrupts the argument. An appendix is appropriate
for a long self-contained input that remains necessary but is not part of the
paper's narrative spine.

### Demote

Use unnumbered prose for material without independent mathematical or
navigational value, such as a short interpretation, transition, or local
well-definedness note. Use an example environment when the material's real
function is illustrative rather than assertive.

### Remove

Recommend removal only after checking references, downstream uses, novelty,
and scope. Do not remove a complete original proof, necessary technical input,
or substantive open problem without explicit authorization.

## 5. Audit Result Types

- A theorem or proposition should have its essential motivation and terminology
  available before the statement.
- A corollary merits separate status when it closes a main line or gives a form
  readers will reuse.
- A remark should perform a clear function: interpretation, attribution,
  boundary warning, or explanation of a choice.
- An example should illuminate a definition, test sharpness, or show a genuine
  boundary case.
- A question or conjecture should be checked for current status when source
  verification is authorized and feasible. State uncertainty instead of
  guessing.

Changing an environment type can alter references and reader expectations;
validate both after structural edits.

## 6. Introduce Definitions and Notation

Place a definition before the first result that needs it and explain the
problem it resolves when that motivation is not already clear. Add examples
only when they materially clarify possible behavior or a later invariant; do
not impose a fixed number of examples.

Check that every symbol is defined before use, independence from choices is
proved or cited, and later theorems do not supply an unstated premise needed by
the definition.

## 7. Design the Abstract and Introduction

The abstract should identify the setting, principal contribution, and most
important consequence without becoming a proof sketch or section list. Include
technical notation only when it is essential to state the main result.

The introduction should motivate the problem, locate it accurately in the
literature, state the main results in an intelligible dependency order, and
give enough organization for navigation. The appropriate order depends on the
paper; do not force definitions, examples, literature, or applications into a
fixed template when another order is clearer.

## 8. Use Literature Carefully

Before shortening a proof by citation, verify that the source has compatible
hypotheses, setting, and conclusion. Preserve the local argument when it adds a
case, uniformity, sharpness, construction, or explanation not supplied by the
source.

Follow the entrypoint's privacy and authorization rules. When source
verification is authorized, use bibliographic data already provided by the
user or a generic search that does not disclose manuscript content.

## 9. Execute and Validate

Separate recommendations from authorized edits. Apply structural changes in
small, reviewable groups. When files and tools are available:

1. update and search labels, references, terminology, and citations;
2. compile until cross-references stabilize;
3. inspect warnings and affected rendered pages;
4. trace each principal theorem backward through the revised dependency graph;
5. confirm protected material and unrelated files remain unchanged.

When any check cannot be performed, report it as unverified rather than
assuming success.

The target is not a universally shortest manuscript. It is a manuscript whose
scope, logical dependencies, novelty, and attribution are visible at the level
of detail appropriate to its audience.
