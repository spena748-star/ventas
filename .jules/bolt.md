
## 2026-06-22 - Rendering Bottlenecks in Vanilla JS
**Learning:** O(N^2) lookups (like `indexOf` or `find` inside a loop) and incremental DOM updates (`appendChild` in a loop) are the primary performance killers in this architecture. Consolidating multiple array passes into a single iteration also provides a noticeable boost.
**Action:** Always use single-pass loops for data processing and batch DOM updates using `innerHTML` concatenation for large lists.
