## 2026-07-06 - Optimized Table Rendering and Dashboard Stats
**Learning:** In vanilla JS, replacing multiple `.reduce`/`.map` calls with a single `forEach` loop for dashboard stats, and switching from repeated `appendChild` to a single `innerHTML` update for large tables, significantly improves performance. Using a `Map` for O(1) lookups instead of `.find()` (O(N)) inside render loops is critical for scalability.
**Action:** Always prefer single-pass loops and batched DOM updates when dealing with potentially large datasets in rendering functions.
