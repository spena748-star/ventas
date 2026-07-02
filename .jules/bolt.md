## 2026-07-03 - [Regression in renderVentas performance]
**Learning:** Performance optimizations like replacing `indexOf` with loop indices and batching DOM updates are prone to regression during feature updates if not carefully maintained. The O(N²) `indexOf` lookup inside `forEach` and repeated `appendChild` calls significantly degrade performance as the dataset grows (e.g., 5000+ items).
**Action:** Always check for $O(N^2)$ patterns in rendering loops and prefer string accumulation for large table updates.
