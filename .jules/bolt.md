## 2026-06-30 - O(N²) Lookup in Render Loops
**Learning:** In `renderVentas`, the code was using `db.ventas.indexOf(v)` inside a `forEach` loop over a filtered version of `db.ventas`. This caused an O(N²) bottleneck because `indexOf` is O(N) and it's called N times. On a dataset of 5000 items, this resulted in a ~10 second delay.
**Action:** Use a standard `for` loop `for (let i = 0; i < db.ventas.length; i++)` to access both the element and its original index in a single O(N) pass. Combined with batching `innerHTML` updates, logic execution time dropped from ~10s to <600ms.
