## 2024-05-31 - Optimized Render Loops
**Learning:** Large data sets in vanilla JS benefit significantly from $O(1)$ lookups and batched DOM updates. Using `db.clientes.find` inside a loop over thousands of sales items was a major bottleneck ($O(N*C)$). Batching DOM updates by constructing a single HTML string instead of multiple `appendChild` calls also reduces reflows.
**Action:** Always pre-calculate maps/dictionaries for lookups inside loops and prefer `innerHTML` for large table rendering in vanilla JS.
