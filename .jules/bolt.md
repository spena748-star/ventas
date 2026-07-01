## 2026-06-25 - DOM Batching and Single-Pass Iteration
**Learning:** Consolidating multiple array passes (`filter`, `map`, `reduce`) into a single `forEach` or `for` loop and batching DOM updates using string concatenation (`innerHTML`) significantly reduces execution time and layout thrashing in vanilla JS. Specifically, avoiding `indexOf` inside loops prevents $O(N^2)$ performance regressions as the dataset grows.
**Action:** Always prefer single-pass iteration and `innerHTML` accumulation for rendering large tables or dashboards instead of chained array methods and repeated `appendChild`.
