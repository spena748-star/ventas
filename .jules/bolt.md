## 2026-07-20 - O(N²) Render Loop Regression
**Learning:** The `renderVentas` function used `db.ventas.indexOf(v)` inside a `filter().forEach()` loop, leading to O(N²) complexity. Combined with multiple `appendChild` calls, this significantly degraded performance with large datasets (5000+ items).
**Action:** Always use a single-pass `for` loop to capture the original array index and build the table as a single string to batch `innerHTML` updates.
