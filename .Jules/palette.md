## 2025-05-14 - [A11y patterns in dynamic tables and icon-only buttons]
**Learning:** In applications using template literals to render dynamic tables and dashboard cards, accessibility features like `aria-label`, `title`, and `aria-hidden` are often overlooked. Emojis used as icons should be hidden from screen readers to reduce noise, and icon-only buttons must have descriptive labels for non-visual users.
**Action:** Always check dynamic rendering logic for missing ARIA attributes and ensure decorative emojis are marked with `aria-hidden="true"`.
