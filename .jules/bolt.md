## 2025-05-15 - Optimization of Large List Rendering
**Learning:** In this vanilla JS architecture, using `db.ventas.indexOf(v)` inside a `forEach` loop created an O(N^2) bottleneck. Additionally, incremental `appendChild` calls caused significant reflow overhead.
**Action:** Always favor batched `innerHTML` updates and use the index from `forEach` or a pre-computed `Map` for lookups to ensure O(N) performance.
