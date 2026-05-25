## 2025-05-25 - Improve Keyboard and Screen Reader Accessibility
**Learning:** Non-semantic interactive elements like `div` or `span` used as buttons need explicit `role="button"`, `tabindex="0"`, and a global keyboard listener for 'Enter' and 'Space' keys to be accessible to keyboard and screen reader users.
**Action:** Apply `role="button"` and `tabindex="0"` to all non-semantic interactive elements and implement a global keyboard listener.
