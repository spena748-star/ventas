## 2026-06-11 - Optimized renderVentas with single-pass iteration
**Learning:** Using `filter().forEach()` and calling `indexOf(v)` inside the loop creates an $O(N^2)$ complexity which severely impacts performance for large datasets (5000+ items). Additionally, multiple `appendChild` calls cause excessive reflows.
**Action:** Always prefer a single `forEach` loop and use the index provided by the callback. Batch DOM updates by concatenating an HTML string and setting `innerHTML` once.
