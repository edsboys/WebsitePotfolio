document.addEventListener("DOMContentLoaded", () => {
      
  // --- 1. NAVIGATION (HAMBURGER & SCROLL) ---
  const hamburger = document.querySelector(".hamburger");
  const navLinks = document.querySelector(".nav-links");
  const navLinksItems = document.querySelectorAll(".nav-links a");
  const navbar = document.getElementById("navbar");
  
  // Toggle mobile menu
  function toggleMenu() {
    hamburger.classList.toggle("active");
    navLinks.classList.toggle("active");
    const isExpanded = hamburger.classList.contains("active");
    hamburger.setAttribute("aria-expanded", isExpanded);
    document.body.style.overflow = isExpanded ? "hidden" : "";
  }
  
  hamburger.addEventListener("click", toggleMenu);
  
  // Close menu when a link is clicked
  navLinksItems.forEach(link => {
    link.addEventListener("click", () => {
      if (navLinks.classList.contains("active")) {
        toggleMenu();
      }
    });
  });
  
  // Close menu on outside click
  document.addEventListener("click", (e) => {
    if (
      navLinks.classList.contains("active") &&
      !navLinks.contains(e.target) &&
      !hamburger.contains(e.target)
    ) {
      toggleMenu();
    }
  });
  
  // Add shadow to navbar on scroll
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  });
  
  // --- 2. SCROLL TO TOP BUTTON ---
  const scrollTopBtn = document.getElementById("scrollTop");
  
  window.addEventListener("scroll", () => {
    if (window.scrollY > 400) {
      scrollTopBtn.classList.add("visible");
    } else {
      scrollTopBtn.classList.remove("visible");
    }
  });
  
  scrollTopBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  // --- 3. TYPING EFFECT ---
  const typingElement = document.querySelector(".typing-text");
  const roles = [
    "Full-Stack Engineer",
    "AI/ML Enthusiast",
    "Software Developer",
    "Problem Solver"
  ];
  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;

  function type() {
    if (!typingElement) return;
    
    const currentRole = roles[roleIndex];
    let typeSpeed = 100;

    if (isDeleting) {
      // Deleting
      typingElement.textContent = currentRole.substring(0, charIndex - 1);
      charIndex--;
      typeSpeed = 50;
    } else {
      // Typing
      typingElement.textContent = currentRole.substring(0, charIndex + 1);
      charIndex++;
      typeSpeed = 100;
    }

    if (!isDeleting && charIndex === currentRole.length) {
      // Pause at end of word
      typeSpeed = 2000;
      isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
      // Finished deleting
      isDeleting = false;
      roleIndex = (roleIndex + 1) % roles.length;
      typeSpeed = 500;
    }

    setTimeout(type, typeSpeed);
  }
  
  type(); // Start the typing effect

  // --- 4. ANIMATE ON SCROLL (Sections & Skills) ---
  const scrollObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        
        // Specific logic for skill bars
        if (entry.target.id === "skills") {
          const skillBars = entry.target.querySelectorAll(".skill-progress");
          skillBars.forEach(bar => {
            bar.style.width = bar.dataset.progress + "%";
          });
        }
        
        // Animate project cards
        if (entry.target.id === "projects") {
           const projectCards = entry.target.querySelectorAll(".project-card");
           projectCards.forEach((card, index) => {
             setTimeout(() => {
               card.classList.add("visible");
             }, index * 100); // Stagger the animation
           });
        }
        
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  // Observe all sections with the class
  document.querySelectorAll(".fade-in-section").forEach(section => {
    scrollObserver.observe(section);
  });
  
  // --- 5. PROJECT FILTERING ---
  const filterButtons = document.querySelectorAll(".filter-btn");
  const projectCards = document.querySelectorAll(".project-card");
  
  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      const filter = button.dataset.filter;
      
      // Update button active state
      filterButtons.forEach(btn => btn.classList.remove("active"));
      button.classList.add("active");
      
      // Filter projects
      projectCards.forEach(card => {
        const categories = card.dataset.category;
        if (filter === "all" || categories.includes(filter)) {
          card.style.display = "flex";
          card.classList.add("visible");
        } else {
          card.style.display = "none";
          card.classList.remove("visible");
        }
      });
    });
  });

  // --- 6. DEMO ALERT (from your original code) ---
  const demoAlertLinks = document.querySelectorAll(".demo-alert");
  demoAlertLinks.forEach(link => {
    link.addEventListener("click", (e) => {
      e.preventDefault();
      alert('Live demo not available yet.');
    });
  });

  // --- 7. FUN CONSOLE MESSAGE (from your original code) ---
  console.log("%cHey there! 👋 Welcome to Mpho Matseka's portfolio.", 
    "color: #6366f1; font-size: 18px; font-weight: bold;");
  
});