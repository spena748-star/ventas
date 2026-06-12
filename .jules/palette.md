# Palette's Journal - UX & Accessibility

## 2026-06-25 - Initial Accessibility Audit
**Learning:** Found several accessibility gaps in the core interface, including missing focus indicators (due to `outline: none`), missing ARIA labels on icon-only buttons, and form inputs without associated labels.
**Action:** Implementing a global focus-visible style, adding a .sr-only utility for hidden labels, and ensuring all interactive elements have appropriate ARIA attributes.
