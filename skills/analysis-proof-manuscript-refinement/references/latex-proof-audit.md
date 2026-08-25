# LaTeX Proof Audit

Use this checklist when source integrity, macros or environments,
cross-references, compilation, build configuration, or rendered layout is part
of the authorized task. Apply only the checks supported by the available files
and tools, and follow the entrypoint's scope and privacy rules.

## Notation Propagation

- Renamed notation has been propagated through statements, proofs, captions,
  indexes, and references in the authorized scope.
- Local macro use agrees with established manuscript conventions.
- Obsolete spellings and command names no longer appear in active source.

## Equations and References

- Every referenced display has a unique label.
- Labels are attached to the intended counter and hyperlink target.
- Equation and theorem references use the manuscript's established commands.
- Manual tags are retained only when the numbering exception is intentional.
- Alignment and line breaks reflect mathematical structure.
- Renumbering has not left stale hard-coded references in text or captions.

## Source Structure

- Environments, delimiters, and groups are balanced.
- Theorem and proof environments are paired as intended.
- Renamed commands, labels, citation keys, and environment names have no stale
  uses in the edited scope.
- Macro changes do not silently alter protected notation or unrelated content.
- Source comments and disabled blocks do not retain obsolete identifiers that
  will later be reactivated accidentally.

For proof-level mathematical checks, follow
[revision-workflow.md](revision-workflow.md); do not duplicate that workflow
here.

## Compilation

Use the user's build command when supplied. Otherwise use an available project
command only when doing so is within scope. Check for:

```text
fatal errors
undefined control sequences
undefined references or citations
duplicate or multiply defined labels
rerun warnings
overfull or underfull boxes
```

Compile again when numbering, bibliography data, or cross-references changed.
If compilation cannot be run, state that explicitly.

Treat unfamiliar build configuration as untrusted until inspected. Do not
enable shell escape, run unrelated project scripts, install dependencies, or
change the toolchain merely to obtain a successful build without authorization.

## Rendered Output

Inspect affected pages when changes alter long displays, theorem placement,
page breaks, tables, figures, captions, footnotes, or hyperlinks. Confirm that
content is legible, anchors point to the intended objects, and moved material
does not leave misleading transitions.

If no renderer is available, report the missing visual check rather than
inferring layout quality from source alone.

## Final Verification

Review the final diff, confirm that protected material and unrelated files are
unchanged, and record the build command, build result, inspected pages or
objects, and unresolved diagnostics.

Report compilation and layout evidence separately from mathematical review.
