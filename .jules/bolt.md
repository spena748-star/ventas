## 2025-05-15 - [Rendering Performance Optimization]
**Learning:** In vanilla JavaScript SPAs, rendering large lists using incremental `appendChild` or `innerHTML` calls within a loop causes significant performance degradation due to repeated layout reflows and repaints. Additionally, calling `indexOf` or `find` on a large array inside a render loop introduces O(N^2) complexity.
**Action:** Always batch DOM updates by constructing a single HTML string and updating `innerHTML` once at the end. Use pre-calculated indices or hash maps for O(1) lookups inside loops to maintain linear complexity.
