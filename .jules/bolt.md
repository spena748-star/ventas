## 2025-05-14 - O(N^2) index lookups in render loops
**Learning:** Using `db.ventas.indexOf(v)` inside a loop over filtered data results in O(N^2) complexity. As the dataset grows, this becomes a major bottleneck for UI responsiveness.
**Action:** Always pre-map arrays with their original indices using `.map((v, i) => ({v, i}))` before filtering and rendering to ensure O(1) index access during iteration.

## 2025-05-14 - DOM Throttling via innerHTML Batching
**Learning:** Incremental `appendChild` calls in large loops trigger repeated reflows. While modern browsers are optimized, batching remains more efficient for vanilla JS.
**Action:** Accumulate HTML templates in a string and perform a single `tbody.innerHTML` update to minimize DOM thrashing in data-heavy tables.
