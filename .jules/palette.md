## 2023-10-27 - Global Keyboard Support for Custom Buttons
**Learning:** Elements using `role="button"` for interactivity must be explicitly handled in a global keydown listener if they are not semantic `<button>` elements, ensuring that 'Enter' and 'Space' keys trigger the same action as a mouse click.
**Action:** Always include a global keydown listener and set `tabindex="0"` when using `role="button"` on non-semantic elements.

## 2023-10-27 - Form Label Association
**Learning:** Explicit association between `<label>` and form controls via `for` and `id` attributes is essential for both accessibility and improved tap targets on mobile devices.
**Action:** Audit all forms to ensure every `<label>` has a corresponding `for` attribute matching an input's `id`.
