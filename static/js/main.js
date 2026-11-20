"use strict";

document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const toggle = document.getElementById("menuToggle");

    if (sidebar && toggle) {
        toggle.addEventListener("click", () => {
            const isOpen = sidebar.classList.toggle("sidebar-open");
            toggle.setAttribute("aria-expanded", String(isOpen));
        });
    }

    // Evita enviar el formulario comparador sin seleccionar alimentos.
    const compareForm = document.querySelector(".compare-form");
    if (compareForm) {
        compareForm.addEventListener("submit", (event) => {
            const checked = compareForm.querySelectorAll('input[name="food_ids"]:checked');
            if (checked.length === 0) {
                event.preventDefault();
                window.alert("Selecciona al menos un alimento.");
            }
        });
    }
});
