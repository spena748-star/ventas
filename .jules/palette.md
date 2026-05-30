## 2026-05-30 - Accessible Interactive Non-Semantic Elements
**Learning:** Elements like `<span>` or `<div>` used as interactive components must include `role="button"` and `tabindex="0"` to be accessible to screen readers and keyboard users. A global `keydown` listener is a lightweight way to enable 'Enter' and 'Space' activation for these elements without modifying every click handler.
**Action:** Always include ARIA roles and tab indices for non-semantic interactive elements, and ensure a global keyboard listener is present for the `role="button"` pattern.
