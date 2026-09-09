// Progressive enhancement: navigation and contact links also work without JS.
const menuButton = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#site-navigation");
const navContainer = document.querySelector(".nav-container");
const mobileViewport = window.matchMedia("(max-width: 900px)");

if (menuButton && navigation && navContainer) {
  function setMenuOpen(open, restoreFocus = false) {
    menuButton.setAttribute("aria-expanded", String(open));
    navigation.classList.toggle("is-open", open);
    const label = menuButton.querySelector(".menu-label");
    if (label) label.textContent = open ? "Close" : "Menu";
    if (restoreFocus) menuButton.focus();
  }
  menuButton.hidden = false;
  navContainer.classList.add("menu-enabled");
  menuButton.addEventListener("click", () =>
    setMenuOpen(menuButton.getAttribute("aria-expanded") !== "true"),
  );
  navigation.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link) return;
    setMenuOpen(false);
    if (mobileViewport.matches && link.hash) {
      const target = document.querySelector(link.hash);
      if (target) {
        // Do not leave keyboard focus in a hidden menu after navigation.
        target.setAttribute("tabindex", "-1");
        target.focus({ preventScroll: true });
        target.addEventListener(
          "blur",
          () => target.removeAttribute("tabindex"),
          { once: true },
        );
      }
    }
  });
  document.addEventListener("keydown", (event) => {
    if (
      event.key === "Escape" &&
      menuButton.getAttribute("aria-expanded") === "true"
    )
      setMenuOpen(false, true);
  });
  document.addEventListener("click", (event) => {
    if (!navContainer.contains(event.target)) setMenuOpen(false);
  });
  navContainer.addEventListener("focusout", (event) => {
    if (!navContainer.contains(event.relatedTarget)) setMenuOpen(false);
  });
  mobileViewport.addEventListener("change", () => {
    const focusWouldBeHidden =
      mobileViewport.matches && navigation.contains(document.activeElement);
    setMenuOpen(false, focusWouldBeHidden);
  });
}

const copyButton = document.querySelector(".copy-email");
const copyStatus = document.querySelector(".copy-status");
if (copyButton && copyStatus && navigator.clipboard?.writeText) {
  copyButton.hidden = false;
  copyButton.addEventListener("click", async () => {
    copyStatus.textContent = "";
    try {
      await navigator.clipboard.writeText(copyButton.dataset.email);
      copyStatus.textContent = "Email address copied.";
    } catch {
      copyStatus.textContent =
        "Could not copy automatically. Select the email address above to copy it.";
    }
  });
}
const year = document.querySelector("#year");
if (year) year.textContent = String(new Date().getFullYear());
