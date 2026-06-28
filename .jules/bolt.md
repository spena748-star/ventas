## 2026-06-28 - Optimized renderVentas O(N^2) regression
**Learning:** A regression in `renderVentas` re-introduced O(N^2) behavior by using `db.ventas.indexOf(v)` inside a `forEach` loop and performing individual `appendChild` calls for each row. This caused rendering time for 5000 items to spike to ~13 seconds.
**Action:** Use a single `for` loop to capture indices directly and build a single HTML string for the entire table body to batch DOM updates via `innerHTML`. Always verify performance with a large dataset (5000+ items) to catch such regressions.
