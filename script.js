// ---------------- HAMBURGER MENU ----------------
const hamburgerIcon = document.querySelector(".hamburger-icon");
const menuLinks = document.querySelector(".menu-links");

function toggleMenu() {
  if (!menuLinks || !hamburgerIcon) return;
  menuLinks.classList.toggle("open");
  hamburgerIcon.classList.toggle("open");
}

// Close menu on outside click
document.addEventListener("click", (e) => {
  if (!menuLinks || !hamburgerIcon) return;
  if (!menuLinks.contains(e.target) && !hamburgerIcon.contains(e.target)) {
    menuLinks.classList.remove("open");
    hamburgerIcon.classList.remove("open");
  }
});

if (hamburgerIcon) hamburgerIcon.addEventListener("click", toggleMenu);

// ---------------- SMOOTH SCROLL ----------------
const navLinks = document.querySelectorAll('a[href^="#"]');

navLinks.forEach(link => {
  link.addEventListener("click", (e) => {
    e.preventDefault();
    const target = document.querySelector(link.getAttribute("href"));
    if (target) target.scrollIntoView({ behavior: "smooth", block: "start" });
  });
});

// ---------------- SCROLL ANIMATION ----------------
const sections = document.querySelectorAll("section");

sections.forEach(section => section.classList.add("hidden"));

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      entry.target.classList.remove("hidden");
    }
  });
}, { threshold: 0.1 });

sections.forEach(section => observer.observe(section));

// ---------------- SCROLL TO TOP BUTTON ----------------
const scrollBtn = document.createElement("div");
scrollBtn.id = "scrollToTop";
scrollBtn.textContent = "↑";
scrollBtn.style.cssText = `
  position: fixed;
  bottom: 2rem;
  right: 2rem;
  background: black;
  color: white;
  padding: 1rem;
  border-radius: 50%;
  cursor: pointer;
  font-size: 1.5rem;
  z-index: 9999;
  display: none;
  text-align: center;
  transition: all 0.3s ease;
`;
document.body.appendChild(scrollBtn);

window.addEventListener("scroll", () => {
  if (window.scrollY > 400) scrollBtn.style.display = "block";
  else scrollBtn.style.display = "none";
});

scrollBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});

// ---------------- PROJECT HOVER EFFECTS ----------------
const isTouchDevice = ('ontouchstart' in window) || (navigator.maxTouchPoints > 0);

if (!isTouchDevice) {
  const projectCards = document.querySelectorAll(".color-container");
  projectCards.forEach(card => {
    card.addEventListener("mouseenter", () => card.classList.add("hovered"));
    card.addEventListener("mouseleave", () => card.classList.remove("hovered"));
  });
}

// ---------------- TYPING EFFECT FOR INTRO ----------------
const introText = "Software Developer | Aspiring Full Stack Engineer";
const introElement = document.querySelector(".section__text__p2");
let idx = 0;

function typeIntro() {
  if (!introElement) return;
  introElement.textContent = introText.slice(0, idx);
  idx++;
  if (idx <= introText.length) setTimeout(typeIntro, 50);
}

typeIntro();

// ---------------- FUN CONSOLE MESSAGE ----------------
console.log("%cHey there! 👋 Welcome to Mpho Matseka's portfolio.", 
  "color: #ff6600; font-size: 18px; font-weight: bold;");
