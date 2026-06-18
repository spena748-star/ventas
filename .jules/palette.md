## 2023-10-27 - Improving Accessibility in Non-Semantic Single-Page Apps

**Learning:** In applications that rely heavily on non-semantic tags (like `div` or `span`) for interactive elements, basic accessibility can be restored by adding `role="button"`, `tabindex="0"`, and a global keyboard event listener for 'Enter' and 'Space'. Additionally, global `outline: none` styles often hide focus indicators, necessitating a `:focus-visible` override (sometimes with `!important` to ensure visibility across varied components).

**Action:** When encountering a "div-soup" UI, prioritize adding semantic roles and a unified keyboard interaction handler to provide immediate, app-wide accessibility wins.
