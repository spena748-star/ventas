## 2025-05-15 - Initial Accessibility Audit and Strategy
**Learning:** The application uses many non-semantic elements (div, span) for critical navigation and actions without providing necessary accessibility markers (roles, tabindex) or visual focus indicators, which prevents keyboard-only users from navigating the system.
**Action:** Implement a global keyboard listener for elements with `role="button"` and ensure all interactive elements have visible `:focus-visible` states to balance accessibility with the app's clean design.
