## 2026-07-07 - Accessibility for Non-Semantic Buttons
**Learning:** In applications using `div` or `span` for navigation or interactive elements, adding `role="button"` and `tabindex="0"` is necessary but not sufficient; a global keyboard listener for "Enter" and "Space" must be implemented to ensure parity with native HTML `<button>` elements.
**Action:** Always pair `role="button"` with a global or component-level keyboard listener to handle activation.
