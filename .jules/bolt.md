## 2026-06-20 - O(N²) regressions in render loops
**Learning:** Using `indexOf` inside a `forEach` loop over an array that was already filtered creates an O(N²) complexity bottleneck. Similarly, multiple `reduce` and `filter` calls on large datasets cause redundant iterations and object allocations.
**Action:** Use a single-pass `for` loop to handle filtering, aggregation, and HTML construction. Access original array indices directly from the loop counter to maintain O(1) lookups for action buttons. Batch DOM updates by building a single HTML string and setting `innerHTML` once.
