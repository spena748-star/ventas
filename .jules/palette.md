## 2023-10-27 - [Global Keyboard Navigation]
**Learning:** In a single-page app using non-semantic elements (div/span) as buttons, adding `tabindex="0"` and `role="button"` is not enough; a global keyboard listener is required to bridge the gap between keyboard focus and native click behavior for 'Enter' and 'Space' keys.
**Action:** Always pair `role="button"` with a global `keydown` listener that triggers `click()` on these elements to ensure full keyboard accessibility.
