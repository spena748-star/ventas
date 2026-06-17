## 2025-05-14 - Keyboard accessibility for non-semantic buttons
**Learning:** In this codebase, many interactive elements are implemented as `<span>` tags. These do not have native keyboard support (Space/Enter to trigger click) or focusability.
**Action:** When adding interactivity to non-semantic elements, always add `tabindex="0"`, `role="button"`, and a global or local keyboard event listener to handle 'Enter' and 'Space' keys.
