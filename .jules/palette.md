## 2025-05-14 - Improve keyboard accessibility and ARIA labels
**Learning:** Non-semantic interactive elements like <span> badges and <div> nav items need explicit roles, tab indices, and keyboard listeners to be accessible. Icon-only buttons require ARIA labels for screen readers.
**Action:** Always add role="button", tabindex="0", and keyboard listeners to non-semantic interactive elements. Ensure all icon-only buttons have descriptive aria-labels.
