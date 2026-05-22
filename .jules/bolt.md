## 2026-05-22 - Initializing Bolt Journal
**Learning:** Found the application is a vanilla JS SPA that uses `innerHTML` and `appendChild` in loops for rendering.
**Action:** Will perform a benchmark to measure performance of `renderVentas` with 2000 items and optimize it.

## 2026-05-22 - DOM Batching and O(N^2) removal
**Learning:** Batching DOM updates using `innerHTML` instead of multiple `appendChild` calls, and avoiding O(N^2) operations like `indexOf` in a loop, significantly improves rendering performance for large datasets. In this app, `renderVentas` with 2000 items went from ~524ms to ~209ms (~60% improvement).
**Action:** Always batch DOM updates and pre-map data with indices when filtering.
