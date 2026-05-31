## 2026-05-31 - Universal Keyboard Accessibility for Non-Semantic Buttons
**Learning:** In vanilla JS applications using `div` or `span` as interactive elements, accessibility is often overlooked. Adding `role="button"` and `tabindex="0"` is necessary but insufficient; a global `keydown` listener is required to ensure these elements respond to "Enter" and "Space" keys, mimicking native button behavior.
**Action:** Always pair `role="button"` with a global keyboard listener and `:focus-visible` styles to ensure complete keyboard parity with native elements.
