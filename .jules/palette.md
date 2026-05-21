# Palette Journal

## 2025-05-14 - Initial Accessibility Audit
**Learning:** Found several non-semantic interactive elements (spans/divs) lacking ARIA roles and keyboard support, and labels missing associations with inputs.
**Action:** Implementing role="button", tabindex="0", global keyboard listener, and proper label-input associations to ensure the app is usable by keyboard-only users.
