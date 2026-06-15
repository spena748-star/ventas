## 2026-06-15 - Deletion Confirmations and ARIA Labels
**Learning:** Destructive actions should always have a confirmation dialog, and icon-only buttons need ARIA labels and titles for both accessibility and visual context (tooltips).
**Action:** Always check for `confirm()` in delete handlers and add `aria-label`/`title` to icons.
