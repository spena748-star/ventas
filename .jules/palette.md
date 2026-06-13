## 2026-06-13 - [Accessibility audit]
**Learning:** Many form fields were missing explicit label associations, and icon-only buttons lacked ARIA descriptions, which significantly impacts screen reader usability.
**Action:** Always check for `for`/`id` associations in forms and ensure `aria-label` is present on interactive elements that do not have visible text.
