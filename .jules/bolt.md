## 2025-10-27 - Render Loop Optimization
**Learning:** O(N^2) operations (like `Array.indexOf` or `Array.find`) inside render loops significantly degrade performance as data grows. Batching DOM updates by constructing a full HTML string and setting `innerHTML` once is much faster than multiple `appendChild` calls.
**Action:** Always pre-map data with indices before filtering for lookup in render loops. Use string accumulation for large table renders.
