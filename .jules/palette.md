## 2025-05-29 - Global Accessibility and Keyboard Support
**Learning:** For single-page applications using non-semantic elements (like divs/spans) for navigation and controls, implementing a global keyboard listener paired with explicit ARIA roles is the most efficient way to ensure universal accessibility without breaking existing layouts or event listeners.
**Action:** Always include role="button" and tabindex="0" on interactive non-semantic elements, and ensure a global listener handles Enter/Space activation.
