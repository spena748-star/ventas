# Palette's Journal

## 2026-06-30 - Improving Keyboard Accessibility in Vanilla JS Apps
**Learning:** In single-file applications using non-semantic tags (spans, divs) for interactive elements, adding `tabindex="0"` and `role="button"` is not enough; a global keyboard listener for 'Enter' and 'Space' is required to ensure full keyboard accessibility.
**Action:** Always include a global keyboard event listener and a `:focus-visible` CSS rule when enhancing accessibility for custom interactive components.
