// Tooltip
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

//+++++++++ Botón ir arriba ++++++++++//
mybutton = document.getElementById("btn_gototop");
window.onscroll = function() {scrollFunction()};
// Cuando se hace scroll hacia abajo a los 600px el botón aparece
function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 50) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}
    // Se suaviza el desplazamiento
var scrollToTopBtn = document.getElementById("btn_gototop");
var rootElement = document.documentElement;
function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth" //Es necesario tener declarado "scroll-behavior:smooth" en el :root de los estilos
  });
}
btn_gototop.addEventListener("click", scrollToTop);