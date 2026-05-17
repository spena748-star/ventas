## 2025-05-17 - Performance Bottlenecks in Vanilla JS
**Learning:** Found O(n^2) bottleneck in `renderVentas` due to `indexOf` inside a loop over filtered results. Also identified multiple array traversals in `renderDashboard` and DOM thrashing from repeated `appendChild` calls.
**Action:** Consolidate data processing into single-pass loops, map indices to items before filtering to preserve original index at O(1), and use `innerHTML` string concatenation for batched DOM updates. Use a `dom` cache object initialized early to avoid repeated element lookups.
