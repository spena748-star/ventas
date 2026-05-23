## 2026-05-23 - Optimized renderVentas loop and DOM updates
**Learning:** Found an O(N^2) bottleneck in `renderVentas` caused by `indexOf` inside a filtered loop. Also observed performance hit from incremental `appendChild` calls.
**Action:** Use the original array index directly from the loop and batch DOM updates using a single `innerHTML` assignment to significantly improve rendering speed for large datasets.
