## 2026-06-05 - List Rendering Optimization
**Learning:** Repeatedly calling `appendChild` within a loop triggers multiple DOM reflows, significantly degrading performance for large datasets. Furthermore, using `indexOf` inside a loop to find an item's index results in $O(N^2)$ time complexity.
**Action:** Batch DOM updates by constructing a single HTML string and setting `innerHTML` once. Use `.map((v, idx) => ({v, idx}))` before filtering to preserve original indices without $O(N)$ lookups in the render loop.
