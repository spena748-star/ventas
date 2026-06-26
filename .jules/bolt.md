## 2026-06-26 - [Loop Optimization and DOM Batching]
**Learning:** Replacing O(N²) `indexOf` lookups within rendering loops and consolidating multiple array iterations (`reduce`, `filter`, `map`) into a single pass significantly reduces JS execution time for large datasets (5000+ items). Building HTML as a single string and updating `innerHTML` once also minimizes layout reflows compared to multiple `appendChild` calls.
**Action:** Always prefer single-pass `for` or `forEach` loops for data aggregation and batch DOM updates using template strings for high-performance rendering.
