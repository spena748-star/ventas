## 2025-05-18 - [Accessibility for Non-Semantic Elements]
**Learning:** In vanilla HTML/JS apps, non-semantic interactive elements like `<span>` badges and `<div>` navigation items are common but completely inaccessible to keyboard and screen reader users. Simply adding `onclick` is not enough.
**Action:** Always convert interactive `<span>` elements to `<button type="button">` and add `role="button"`, `tabindex="0"`, and `keydown` listeners to custom navigation items to ensure full accessibility.
