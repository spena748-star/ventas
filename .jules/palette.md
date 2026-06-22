## 2026-06-22 - [Keyboard Accessibility for Non-Semantic Buttons]
**Learning:** Interactive components implemented as non-semantic tags (spans, divs) require manual keyboard event handling for Enter and Space keys, as well as `role="button"` and `tabindex="0"`, to be accessible to keyboard and screen reader users.
**Action:** Apply `role="button"` and `tabindex="0"` to all non-semantic interactive elements and implement a global keyboard listener to trigger clicks on 'Enter' and 'Space'.
