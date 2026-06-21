## 2026-06-21 - Enhancing Accessibility in Vanilla JS Legacy Apps

**Learning:** In applications where interactivity is added via JavaScript to non-semantic elements (like `div` or `span`), simple ARIA roles and `tabindex` are not enough for a great UX. A global keyboard event listener is essential to bridge the gap for "click" behaviors on 'Enter' and 'Space' keys, ensuring these elements behave like native buttons. Additionally, icon-only buttons in dynamically rendered tables (using `innerHTML`) are a common place where accessibility attributes like `aria-label` and `title` are frequently forgotten.

**Action:** Always check for non-semantic interactive elements and apply `role="button"`, `tabindex="0"`, and a global keyboard listener. For dynamic table rendering, ensure the template strings include necessary ARIA labels for icon-only actions.
