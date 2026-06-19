## 2026-06-15 - O(N²) Bottleneck in renderVentas
**Learning:** The `renderVentas` function had O(N²) complexity because it used `db.ventas.indexOf(v)` inside a `forEach` loop to find the original index of each item. This caused a ~9.5s delay when rendering 5,000 items. Additionally, repeated `appendChild` calls in a loop are significantly slower than batching `innerHTML` updates.
**Action:** Use a single-pass `for` loop to track original indices and batch HTML string construction for `innerHTML` updates.
