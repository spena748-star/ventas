## 2026-05-27 - Optimized renderCobranza lookup and batching
**Learning:** In a vanilla JS application with large datasets, $O(N \cdot M)$ lookups (like `Array.find` inside a loop) and incremental DOM updates (`appendChild`) are major performance killers. Building a lookup Map and batching `innerHTML` updates yields dramatic improvements.
**Action:** Always check for nested lookups in render loops and consolidate DOM updates into a single batch operation using string concatenation for large tables.
