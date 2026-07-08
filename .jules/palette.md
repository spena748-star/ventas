## 2026-07-08 - Keyboard Accessibility for Non-Semantic Buttons
**Learning:** Non-semantic elements (divs, spans) used as interactive components lack native keyboard activation. In this single-file app, they require `tabindex="0"`, `role="button"`, and a global 'keydown' listener to handle 'Enter' and 'Space' keys to ensure they are accessible to keyboard users.
**Action:** When adding interactivity to non-button elements, always include ARIA roles, tab indexing, and ensure the global keyboard listener in `initApp` is active.
