## 2026-07-03 - Optimized renderVentas with O(1) lookups and batched DOM updates

**Learning:** Large datasets (5000+ items) in index.html triggered O(N^2) complexity due to `indexOf` calls inside the render loop and inefficient DOM manipulation with repeated `appendChild`.

**Action:** Replace `filter().forEach()` chains with single `for` loops to capture original indices and build table rows as a single string to batch `innerHTML` updates, significantly reducing rendering time and reflows.
