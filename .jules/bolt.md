## 2026-06-07 - Optimization of renderVentas and renderCobranza
**Learning:** O(N^2) lookups (like `indexOf` in a loop over filtered results) and incremental DOM updates (`appendChild` in a loop) are the primary bottlenecks for list rendering in this codebase.
**Action:** Use `.map((v, i) => ({v, i}))` to preserve original indices before filtering, and batch DOM updates using string concatenation followed by a single `innerHTML` assignment.
