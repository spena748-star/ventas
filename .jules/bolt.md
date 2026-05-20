## 2025-05-14 - Batch DOM Updates and Index Mapping

**Learning:** Incremental DOM updates using `appendChild` in a loop are significantly slower than batching via `innerHTML` and string concatenation, especially for large tables (2000+ rows). Additionally, using `Array.indexOf` inside a loop over the same array creates an O(N^2) complexity bottleneck.

**Action:** Always batch DOM updates for lists. Pre-map datasets with their original indices when filtering if those indices are needed for event handlers (like edit/delete buttons), ensuring O(N) performance.
