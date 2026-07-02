## 2026-06-25 - Accessibility and Keyboard Navigation Sweep
**Learning:** In single-page vanilla JS apps, interactive elements like spans need explicit ARIA roles, tabindices, and keyboard event listeners to be accessible. Icon-only buttons are invisible to screen readers without aria-labels.
**Action:** Always check for non-semantic interactive elements and add proper roles/tabindex. Ensure all icon-only buttons have descriptive aria-labels.
