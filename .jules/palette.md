## 2024-05-24 - Interactive Non-Semantic Elements Accessibility
**Learning:** Using `div` or `span` as interactive elements (buttons/nav) without ARIA roles and tabindex makes them invisible to keyboard and screen-reader users. A global keyboard listener can bridge the gap without adding 100+ event listeners.
**Action:** Always add `role="button"`, `tabindex="0"`, and a global `keydown` listener for custom interactive components.

## 2024-05-24 - Focus Visibility for UX
**Learning:** Native focus outlines can be visually jarring and are often removed by designers, but are essential for accessibility. `:focus-visible` allows for high-visibility indicators only for keyboard users.
**Action:** Use `*:focus-visible` with a clear outline and offset to provide accessible focus states without affecting mouse users.

## 2024-05-24 - XSS Safety in Dynamic Rendering
**Learning:** Injecting user-controlled data directly into `innerHTML` (e.g., in ARIA labels or titles) within template literals is a security risk (XSS).
**Action:** Avoid large-scale refactors of dynamic render functions that handle user data unless using proper sanitization or `textContent`/`setAttribute` methods.
