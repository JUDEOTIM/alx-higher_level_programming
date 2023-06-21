/* Fetch data from hello and display inside div#hello */
$(document).ready(function () {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    type: "GET",
    dataType: "json",
    success: function (data) {
      $("DIV#hello").text(data.hello);
    },
  });
});
