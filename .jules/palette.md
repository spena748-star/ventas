# Palette's Journal - UX & Accessibility

## 2025-05-14 - Spanish Accessibility Patterns in Admin Ventas
**Learning:** In this vanilla Spanish-language app, interactive table actions (Editar, Registrar Pago, WhatsApp, Eliminar) used only emojis, providing zero context for screen readers. Additionally, the complex "Captura" form had detached labels, which negatively impacted mobile usability as clicking the label wouldn't focus the tiny input fields.
**Action:** Always wrap or associate labels with inputs using 'for/id' and provide Spanish aria-labels for emoji-based action buttons to maintain consistency with the 'es-ES' lang attribute.
