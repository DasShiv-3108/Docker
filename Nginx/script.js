// ════════════════════════════════════════════
//   Senior Secondary School Tamber — script.js
// ════════════════════════════════════════════

/**
 * showPage()
 * ──────────
 * Ye function SPA-style page navigation handle karta hai.
 * Jab bhi koi nav link click hota hai, ye:
 *   1. Saare pages hide karta hai (.page class)
 *   2. Target page dikhata hai
 *   3. Nav link ka active state update karta hai
 *   4. Page ko top pe scroll karta hai
 *
 * @param {string} id  - Page div ka ID (e.g. 'home', 'about')
 * @param {Element} el - Jo nav link click hua
 */
function showPage(id, el) {
  // Step 1: Saare pages hide karo
  document.querySelectorAll('.page').forEach(function(page) {
    page.classList.remove('active');
  });

  // Step 2: Target page dikhao
  var targetPage = document.getElementById(id);
  if (targetPage) {
    targetPage.classList.add('active');
  }

  // Step 3: Saare nav links se 'active' class hato
  document.querySelectorAll('.nav-links a').forEach(function(link) {
    link.classList.remove('active');
  });

  // Step 4: Clicked link ko active karo
  if (el) {
    el.classList.add('active');
  }

  // Step 5: Page ke top pe scroll karo (smooth)
  window.scrollTo({ top: 0, behavior: 'smooth' });

  // Event propagation rokna (optional)
  return false;
}
