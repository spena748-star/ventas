## 2026-07-08 - O(N²) Anti-pattern in render loops
**Learning:** Calling `db.ventas.indexOf(v)` inside a `forEach` loop over a filtered subset of `db.ventas` creates an O(N²) bottleneck. For 5,000 items, this alone accounted for ~1.8s of rendering time. Additionally, repetitive `appendChild` calls cause significant DOM thrashing.
**Action:** Use a single `for` loop over the source array to maintain access to the original index `i` without re-searching, and batch DOM updates by accumulating a single HTML string for a single `innerHTML` assignment.
