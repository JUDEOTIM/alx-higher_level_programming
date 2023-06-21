/* Toggle class */
$(document).ready(function () {
  $("DIV#toggle_header").click(function () {
    $("header").toggleClass("red green");
  });
});
