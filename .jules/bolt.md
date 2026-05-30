## 2026-05-30 - Optimize list rendering performance
**Learning:** In a vanilla JS SPA, repeated `appendChild` calls in a loop cause significant performance degradation due to multiple layout reflows. Additionally, using `indexOf` or `find` inside render loops leads to (N^2)$ or (N \times M)$ complexity.
**Action:** Always batch `innerHTML` updates using string concatenation and pre-calculate lookups using Maps or objects to ensure (1)$ access within loops.
