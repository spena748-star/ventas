## 2026-05-19 - O(N^2) indexing and DOM batching
**Learning:** Found a significant O(N^2) bottleneck in `renderVentas` caused by calling `indexOf()` inside a loop over a filtered array. Additionally, repeated `appendChild` or `innerHTML +=` calls within loops caused unnecessary reflows.
**Action:** Use `.map((v, i) => ({...v, originalIdx: i}))` to pre-index data before filtering. Batch DOM updates by building a single HTML string and updating `innerHTML` once. Use a global `dom` cache to avoid repeated `getElementById` calls.
