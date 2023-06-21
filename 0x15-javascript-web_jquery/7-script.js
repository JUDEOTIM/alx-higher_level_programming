/* Fetch character name from an Api */
$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.hbtn.io/api/people/5/?format=json",
    type: "GET",
    dataType: "json",
    success: function (data) {
      $("DIV#character").text(data.name);
    },
    error: function () {
      $("DIV#character").text("An error occurred while fetching data");
    },
  });
});
