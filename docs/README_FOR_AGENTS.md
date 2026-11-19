# Suggested multi-agent orchestration

1. **Circuit Architect** owns original schematic reconstruction and the Rev C functional-delta matrix. Stops if any original function cannot be interpreted.
2. **Power Path Reviewer** independently evaluates battery charger, USB/external input, power continuity, 3V3 peak current and voltage rail requirements. May veto unsafe modifications.
3. **EasyEDA Builder** creates/selects the dedicated EasyEDA Pro project; reads native nets, chooses verified symbols/footprints, drafts edits in preview, applies only with user approval, runs ERC then PCB DRC.
4. **BOM / India Sourcing** researches manufacturer-verified parts and Indian suppliers, procurement prices, pinouts and holder package. Mark stock/price observation date.
5. **Test Engineer** writes reproducible hardware validation with scopes, battery emulator and fault injections; reports pass only for actual measurements.
6. **Release Reviewer** compares all requirements/functional deltas, checks evidence traceability and makes a recommendation, never automated fabrication authorization.

For each phase write `evidence/PHASE-<id>-template.md` copy with a truth-labelled observation table; unknown data stays `NOT_RUN`. Draft all code and data in feature branches. Never make uncontrolled changes to original or Rev B source.
