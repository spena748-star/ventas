## 2026-07-04 - [renderVentas O(N^2) Regression]
**Learning:** Using `indexOf` inside a loop over a large dataset (5000 items) created a significant performance bottleneck (O(N^2)), causing rendering to take ~11s. Batching DOM updates using `innerHTML` concatenation is an order of magnitude faster than multiple `appendChild` calls.
**Action:** Always use a single-pass `for` loop to capture indices and accumulate HTML strings for batched `innerHTML` updates when rendering large tables in vanilla JS.
