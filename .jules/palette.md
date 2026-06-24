## 2026-06-24 - Enhancing keyboard accessibility for non-semantic interactive elements
**Learning:** In applications using <div> and <span> as buttons, it is critical to provide role="button" and tabindex="0" alongside a global keyboard listener (Enter/Space) to ensure parity with native <button> elements for screen readers and keyboard-only users.
**Action:** Always check for interactive non-button elements and apply these ARIA attributes and keyboard listeners.
