## 2026-06-18 - O(N^2) Regression in renderVentas
**Learning:** The `renderVentas` function had an (N^2)$ bottleneck because it used `db.ventas.indexOf(v)` inside a `.forEach()` loop over a filtered array to get the original index. Additionally, appending DOM elements one by one was causing excessive reflows.
**Action:** Always use a single `for` loop to maintain the original array index and batch DOM updates by building a single HTML string for `innerHTML`.
