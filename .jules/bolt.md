## 2026-06-08 - [O(N^2) Bottlenecks in Render Loops]
**Learning:** In a single-file vanilla JS app like this, rendering large lists (5000+ items) becomes extremely slow due to nested O(N) operations like `indexOf` or `find` inside `forEach` loops, and repeated DOM reflows from `appendChild`.
**Action:** Use a single-pass loop (e.g. `for`) to filter and map indices simultaneously. Build HTML as a single string (or array of strings) and update `innerHTML` once to avoid reflow overhead. Use `Map` for O(1) lookups when referencing other data collections (like clients).
