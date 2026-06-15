## 2026-06-15 - Optimization of renderVentas
**Learning:** Using `db.ventas.indexOf(v)` inside a `forEach` loop created an O(N^2) bottleneck. Additionally, appending DOM elements one-by-one with `appendChild` was significantly slower than batching the entire table as an HTML string for a single `innerHTML` update.
**Action:** Use a standard `for` loop to access the index directly and build HTML strings for batch DOM updates to ensure O(N) performance and minimal reflows.
