## 2025-05-14 - Accessibility for Non-Semantic Interactive Elements
**Learning:** Custom interactive elements like sidebar items and top-bar badges often lack keyboard accessibility. Using `role="button"` and `tabindex="0"` makes them discoverable by assistive technologies and focusable by keyboard.
**Action:** Always include `role="button"` and `tabindex="0"` for non-button interactive elements, and implement a global keydown listener for 'Enter' and 'Space' activation.

## 2025-05-14 - Visual Focus Indicators
**Learning:** Default browser focus rings can be inconsistent or clash with dark UI themes. `:focus-visible` allows for custom, high-contrast focus indicators that only appear when navigating via keyboard.
**Action:** Implement custom `:focus-visible` styles using CSS variables to ensure consistency with the application's color palette.
