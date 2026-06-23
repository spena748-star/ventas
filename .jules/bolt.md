## 2026-06-25 - O(N^2) Regression in renderVentas
**Learning:** Using `indexOf` inside a `forEach` or `map` loop on an array of objects creates an O(N^2) bottleneck, especially when the array grows large (5000+ items).
**Action:** Always use a standard `for` loop to access the original index directly when rendering lists that require interaction with the source data. Batch DOM updates using `innerHTML` concatenation to minimize reflows.
