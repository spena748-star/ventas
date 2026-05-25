## 2026-05-25 - DOM Batching vs O(N^2) Lookups
**Learning:** In vanilla JS apps with large data tables, the primary bottlenecks are usually redundant $O(N)$ lookups (like `Array.indexOf`) inside render loops and frequent DOM reflows caused by multiple `appendChild` calls.
**Action:** Always batch `innerHTML` updates with string concatenation and use single-pass `for` loops with pre-mapped or direct indices to ensure $O(N)$ complexity.
