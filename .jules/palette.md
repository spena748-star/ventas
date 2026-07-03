## 2026-06-26 - Keyboard Accessibility for Non-Semantic Buttons
**Learning:** Interactive components implemented as non-semantic tags (spans, divs) require manual keyboard event handling and ARIA roles as they lack the native activation behavior and focusability of HTML button elements.
**Action:** When using divs or spans as interactive elements, always include `role="button"`, `tabindex="0"`, and ensure a global or local keyboard listener handles 'Enter' and 'Space' keys to trigger the click event.
