## 2024-06-03 - [Keyboard Accessibility for Custom Components]
**Learning:** In a vanilla JS app using non-semantic elements (divs, spans) as buttons, adding `tabindex="0"` and `role="button"` is not enough; a global keyboard listener for 'Enter' and 'Space' is required to match native button behavior.
**Action:** Always implement a global keyboard event listener when using custom interactive elements to ensure they are accessible to keyboard-only users.

## 2024-06-03 - [Form Label Association]
**Learning:** Explicitly associating labels with inputs using `for` and `id` attributes is crucial even when labels are visually adjacent to inputs, especially for screen readers and improving click targets.
**Action:** Consistently use the `for` attribute on all `<label>` elements and ensure they point to the correct `id` of the target input/select.
