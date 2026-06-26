## 2026-06-26 - Keyboard Accessibility for Non-Semantic Buttons
**Learning:** In this vanilla JS SPA, interactive elements like navigation items and status badges are implemented using non-semantic `div` and `span` tags. These lack native keyboard support (Tab focus and Enter/Space activation).
**Action:** Always apply `tabindex="0"`, `role="button"`, and a global `keydown` listener to handle keyboard activation for non-semantic interactive components. Ensure `focus-visible` styles are defined to provide visual feedback during keyboard navigation.
