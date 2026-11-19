---
name: fabrication-release
description: "Review hardware acceptance and only prepare manufacturing files after explicit release authorization."
---

# Fabrication Release

Audit `../../../docs/safety-gates.md`, source delta matrix, native EasyEDA ERC/DRC, exact mechanical footprints, real physical tests, 18650 charging behavior, microphone power, BOM stock and PCB voltage ratings. Fail closed on unknown protected-cell length or supply peaks. Before any Gerber release, require owner and qualified engineering signoff; automated tools cannot certify electrical safety. Keep fabrication exports ignored until approved and versioned.

Record evidence level, source links, requested approvals and the next blocking step.
