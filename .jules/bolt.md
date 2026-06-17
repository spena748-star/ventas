## 2026-06-17 - O(N²) regression in renderVentas
**Learning:** Even after previous optimizations, performance regressions can occur if high-complexity patterns like `indexOf` inside a `forEach` loop over a filtered array are reintroduced. This pattern is particularly expensive in this codebase when handling thousands of entries.
**Action:** Always use a single-pass `for` loop to capture the original array index and avoid nested O(N) lookups. Combine this with string accumulation for `innerHTML` to minimize DOM reflows.
