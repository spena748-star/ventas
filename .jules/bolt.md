## 2025-05-24 - Optimization of large list rendering
**Learning:** The application had $O(N^2)$ bottlenecks in `renderVentas` due to `indexOf` calls inside loops. Batching DOM updates with `innerHTML` instead of `appendChild` is critical for performance when dealing with 2000+ items.
**Action:** Always check for array lookups inside loops when rendering large datasets. Favor single-pass data processing and batch DOM updates.
