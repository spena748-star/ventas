## 2026-06-09 - Global Keyboard Support for Accessible Role="button"
**Learning:** When a legacy codebase uses non-semantic elements (like `<span>`) as interactive controls, adding `role="button"` and `tabindex="0"` is only half the battle. They also need a global keyboard event listener for 'Enter' and 'Space' to be truly accessible.
**Action:** Use a document-level event listener in `initApp` that checks `e.target.getAttribute('role') === 'button'` to catch all such elements, including those dynamically rendered, and trigger their `click()` event.

## 2026-06-09 - High-Contrast Focus Indicator Override
**Learning:** Widespread use of `outline: none` on `:focus` in CSS can make keyboard navigation impossible. A global `:focus-visible` rule with `!important` and `outline-offset` provides a safe way to restore accessibility without breaking the visual design for mouse users.
**Action:** Apply `:focus-visible { outline: 2px solid var(--blue-light) !important; outline-offset: 2px; }` to ensure visibility across all interactive components.
