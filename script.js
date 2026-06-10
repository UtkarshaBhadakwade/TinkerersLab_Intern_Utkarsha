/* ===============================
   TINKERERS LAB INTERACTIONS
================================ */

const sidebar = () => document.getElementById("sidebar");

function toggleMenu() {
    const panel = sidebar();
    if (!panel) return;

    panel.classList.toggle("open");
}

function closeMenu() {
    const panel = sidebar();
    if (panel) panel.classList.remove("open");
}

function toggleWeek(id) {
    const selectedWeek = document.getElementById(id);
    if (!selectedWeek) return;

    const shouldOpen = !selectedWeek.classList.contains("open");

    document.querySelectorAll(".days").forEach(week => {
        week.classList.remove("open");
    });

    selectedWeek.classList.toggle("open", shouldOpen);
}

function openDocumentation(pageId) {
    const targetPage = document.getElementById(pageId);
    if (!targetPage) return;

    document.querySelectorAll(".documentation-page").forEach(page => {
        page.classList.remove("active");
    });

    document.body.classList.add("doc-open");
    targetPage.classList.add("active");
    targetPage.scrollTop = 0;
    closeMenu();
}

function closeDocumentation() {
    document.querySelectorAll(".documentation-page").forEach(page => {
        page.classList.remove("active");
    });

    document.body.classList.remove("doc-open");

    if (window.location.hash) {
        history.pushState("", document.title, window.location.pathname + window.location.search);
    }
}

function openHashDocumentation() {
    const pageId = window.location.hash.replace("#", "");
    if (!pageId) return;

    const targetPage = document.getElementById(pageId);
    if (targetPage && targetPage.classList.contains("documentation-page")) {
        openDocumentation(pageId);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".day-btn[href^='#']").forEach(link => {
        link.addEventListener("click", event => {
            const pageId = link.getAttribute("href").slice(1);
            const targetPage = document.getElementById(pageId);

            if (targetPage && targetPage.classList.contains("documentation-page")) {
                event.preventDefault();
                history.pushState(null, "", `#${pageId}`);
                openDocumentation(pageId);
            }
        });
    });

    document.querySelectorAll(".sidebar a").forEach(link => {
        const currentPage = window.location.pathname.split("/").pop() || "index.html";
        if (link.getAttribute("href") === currentPage) {
            link.classList.add("active");
        }

        link.addEventListener("click", closeMenu);
    });

    document.addEventListener("click", event => {
        const panel = sidebar();
        const menuButton = document.querySelector(".menu-icon");

        if (!panel || !panel.classList.contains("open")) return;
        if (panel.contains(event.target) || menuButton?.contains(event.target)) return;

        closeMenu();
    });

    openHashDocumentation();
});

window.addEventListener("hashchange", openHashDocumentation);

document.addEventListener("keydown", event => {
    if (event.key === "Escape") {
        closeMenu();

        if (document.body.classList.contains("doc-open")) {
            closeDocumentation();
        }
    }
});
