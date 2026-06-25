## 2023-10-27 - O(N^2) Regression in renderVentas
**Learning:** Using `filter().forEach()` and then calling `indexOf` inside the loop to find the original index causes an O(N^2) complexity bottleneck, which is particularly severe when rendering large datasets in a single-page app. Batching DOM updates by constructing a single HTML string and setting `innerHTML` once is significantly faster than multiple `appendChild` calls.
**Action:** Always use a single-pass `for` loop to maintain access to indices and build HTML strings for batched `innerHTML` updates in high-frequency render functions.
