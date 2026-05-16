## 2025-05-16 - [DOM Optimization in Vanilla JS]
**Learning:** In a vanilla JavaScript SPA with frequent data updates and input tracking, redundant DOM lookups and incremental table row appends are the primary performance bottlenecks. Caching elements once and batching innerHTML updates provides a significant, measurable boost in responsiveness and rendering speed.
**Action:** Always implement a central DOM reference cache and build HTML strings for loops instead of multiple appendChild calls in similar architectures.
