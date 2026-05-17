## 2025-05-14 - [Initial UX Audit]
**Learning:** The application is a single-page vanilla JS app with many icon-only buttons and decorative emojis that lack ARIA labels and proper semantic markup for screen readers.
**Action:** Implement ARIA labels for all icon-only buttons and wrap decorative emojis with `aria-hidden="true"` to improve the accessibility of the interface.

## 2025-05-14 - [Interactive Badges Accessibility]
**Learning:** Using `span` or `badge` elements as buttons without `role="button"` and `tabindex="0"` makes them inaccessible to keyboard and screen reader users.
**Action:** Always add `role="button"`, `tabindex="0"`, and a keyboard event listener (Enter/Space) to non-button elements that perform actions on click.
