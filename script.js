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

// Motion enhances visible content; nothing depends on an animation to appear.
(() => {
  if (!Element.prototype.animate || !("IntersectionObserver" in window)) return;
  const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
  const active = new Map();
  const seen = new WeakSet();
  const targets = document.querySelectorAll(
    ".section-heading, .project, .skill, .credential, .badge-card, .about-copy, .contact-panel",
  );
  let observer;

  function reveal(element, delay = 0, distance = 20) {
    if (preference.matches || element.contains(document.activeElement)) return;
    active.get(element)?.cancel();
    const animation = element.animate(
      [
        { opacity: 0.4, transform: `translateY(${distance}px)` },
        { opacity: 1, transform: "translateY(0)" },
      ],
      { duration: 620, delay, fill: "backwards", easing: "cubic-bezier(0.22, 1, 0.36, 1)" },
    );
    active.set(element, animation);
    const cleanup = () => {
      if (active.get(element) === animation) active.delete(element);
    };
    animation.addEventListener("finish", cleanup, { once: true });
    animation.addEventListener("cancel", cleanup, { once: true });
  }

  function observeSections() {
    observer?.disconnect();
    if (preference.matches) return;
    observer = new IntersectionObserver(
      (entries) => {
        let stagger = 0;
        for (const entry of entries) {
          if (!entry.isIntersecting) continue;
          observer.unobserve(entry.target);
          if (seen.has(entry.target)) continue;
          seen.add(entry.target);
          reveal(entry.target, Math.min(stagger++ * 55, 165));
        }
      },
      { threshold: 0.06, rootMargin: "0px 0px -24px 0px" },
    );
    targets.forEach((element) => {
      if (!seen.has(element)) observer.observe(element);
    });
  }

  if (!location.hash || location.hash === "#home") {
    document.querySelectorAll(".hero-copy > *, .portrait").forEach((element, i) => {
      reveal(element, Math.min(i * 35, 175), 12);
    });
  }
  observeSections();
  preference.addEventListener("change", () => {
    active.forEach((animation) => animation.cancel());
    active.clear();
    observeSections();
  });
  // Never delay a keyboard user reaching a link within an animated card.
  document.addEventListener("focusin", (event) => {
    active.forEach((animation, element) => {
      if (element.contains(event.target)) animation.cancel();
    });
  });
  document.querySelectorAll(".additional-credentials").forEach((details) => {
    details.addEventListener("toggle", () => {
      const content = details.querySelector(".badge-groups");
      if (!content) return;
      if (details.open) reveal(content, 0, 8);
      else active.get(content)?.cancel();
    });
  });
  menuButton?.addEventListener("click", () => {
    if (menuButton.getAttribute("aria-expanded") === "true") {
      reveal(navigation, 0, -6);
    } else {
      active.get(navigation)?.cancel();
    }
  });
  window.addEventListener("beforeprint", () => {
    active.forEach((animation) => animation.cancel());
  });
})();
