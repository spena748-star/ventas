## 2024-05-19 - Improved Keyboard Accessibility and Screen Reader Support
**Learning:** In vanilla SPAs using non-semantic elements for interaction (like spans as buttons), it is critical to explicitly provide `role="button"`, `tabindex="0"`, and `aria-label` along with keyboard event listeners for 'Enter' and 'Space' to ensure accessibility.
**Action:** Always check for non-semantic interactive elements and apply the accessibility pattern (role, tabindex, keyboard listeners) plus a visible focus state.
