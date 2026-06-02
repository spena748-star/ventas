## 2026-06-02 - Enhanced Keyboard Accessibility and Visual Focus
**Learning:** Non-semantic interactive elements (like <div> or <span> used as buttons) require explicit 'role="button"' and 'tabindex="0"' to be accessible. Furthermore, a global keydown listener is necessary to handle 'Enter' and 'Space' activation for these elements to match native button behavior.
**Action:** Always ensure custom interactive components have correct ARIA roles and tab indices, and implement a global or component-level keyboard listener to support non-mouse interaction.
