const burger = document.getElementById('burger');
const navlinks = document.getElementById('navlinks');

if (burger && navlinks){
  burger.addEventListener('click', () => {
    const isOpen = navlinks.classList.toggle('open');
    burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  // close on link click (mobile)
  navlinks.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      navlinks.classList.remove('open');
      burger.setAttribute('aria-expanded', 'false');
    });
  });
}
