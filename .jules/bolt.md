## 2026-06-09 - O(N^2) Lookup and Incremental DOM Updates in Table Rendering
**Learning:** In the single-file architecture of this app, complex table render functions (`renderVentas`, `renderCobranza`) were bottlenecks due to $O(N^2)$ lookups (e.g., `indexOf` inside a loop to find the original data index) and incremental `appendChild` calls.
**Action:** Always pre-map indices before filtering (`.map((v, idx) => ({v, idx}))`) and batch HTML strings for a single `innerHTML` update when dealing with datasets over 1000 items.
