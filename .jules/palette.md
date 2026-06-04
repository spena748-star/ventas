## 2025-05-14 - Accessible Forms and Icon Buttons
**Learning:** In a single-page application with many icon-only buttons and forms, ensuring accessibility through ARIA labels and explicit label associations significantly improves the screen reader experience without altering the visual design. Using :focus-visible provides necessary feedback for keyboard users while keeping a clean look for mouse users.
**Action:** Always verify that icon-only buttons have both `aria-label` and `title`, and ensure all `<input>` elements have a corresponding `<label>` with a `for` attribute.
