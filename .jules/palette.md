## 2024-05-24 - Accessibility and Interaction Safety
**Learning:** Interactive elements implemented as non-semantic tags (like spans or divs used as buttons) require `role="button"`, `tabindex="0"`, and manual keyboard event listeners for 'Enter' and 'Space' to be fully accessible. Additionally, icon-only buttons need both `aria-label` and `title` to ensure they are understandable by screen readers and provide visual context on hover.
**Action:** Always audit non-button interactive elements for ARIA roles/tabindex and ensure icon buttons have descriptive labels.

## 2024-05-24 - Safety for Destructive Actions
**Learning:** Users can easily misclick small delete icons in data-heavy tables. Adding a simple `confirm()` dialog to all destructive actions (deleting sales, clients, or catalog items) significantly reduces accidental data loss.
**Action:** Ensure all `splice` operations or similar data-removing logic are preceded by a user confirmation.
