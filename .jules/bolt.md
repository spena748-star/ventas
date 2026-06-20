## 2026-06-20 - Consolidated O(N) Passes and Batched DOM Updates
**Learning:** Replacing multiple array traversals (reduce, map, filter) with a single pass significantly reduces overhead, especially for large datasets. In vanilla JS, batching HTML string construction before updating `innerHTML` is much faster than multiple `appendChild` calls or `innerHTML` updates in a loop.
**Action:** Always prefer single-pass loops and batched DOM updates for render functions handling potentially large data.
