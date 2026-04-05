(function () {
  "use strict";

  var xpFill = document.getElementById("xpFill");
  var yearEl = document.getElementById("year");
  var menuToggle = document.getElementById("menuToggle");
  var mobileNav = document.getElementById("mobileNav");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  function updateXpBar() {
    if (!xpFill) return;
    var doc = document.documentElement;
    var scrollTop = doc.scrollTop || document.body.scrollTop;
    var height = doc.scrollHeight - doc.clientHeight;
    var pct = height > 0 ? (scrollTop / height) * 100 : 0;
    xpFill.style.width = Math.min(100, Math.max(0, pct)) + "%";
  }

  window.addEventListener("scroll", updateXpBar, { passive: true });
  window.addEventListener("resize", updateXpBar);
  updateXpBar();

  if (menuToggle && mobileNav) {
    menuToggle.addEventListener("click", function () {
      var open = mobileNav.hasAttribute("hidden");
      if (open) {
        mobileNav.removeAttribute("hidden");
        menuToggle.setAttribute("aria-expanded", "true");
        menuToggle.setAttribute("aria-label", "Close menu");
      } else {
        mobileNav.setAttribute("hidden", "");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Open menu");
      }
    });

    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        mobileNav.setAttribute("hidden", "");
        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Open menu");
      });
    });
  }

  var achievementCards = document.querySelectorAll(".pillar-card, .game-card");
  if (achievementCards.length && "IntersectionObserver" in window) {
    var seen = new WeakSet();
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting || seen.has(entry.target)) return;
          seen.add(entry.target);
          entry.target.classList.add("achievement-pop");
          setTimeout(function () {
            entry.target.classList.remove("achievement-pop");
          }, 600);
        });
      },
      { rootMargin: "-10% 0px -10% 0px", threshold: 0.2 }
    );
    achievementCards.forEach(function (card) {
      observer.observe(card);
    });
  }

  var galleryVideos = document.querySelectorAll(".game-media-gallery--dense video");
  if (galleryVideos.length) {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      galleryVideos.forEach(function (v) {
        v.removeAttribute("autoplay");
        v.pause();
      });
    } else {
      galleryVideos.forEach(function (v) {
        var p = v.play();
        if (p && typeof p.catch === "function") {
          p.catch(function () {});
        }
      });
    }
  }
})();
