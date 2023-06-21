/* Fetch all movie tilte */
$(document).ready(function () {
  $.ajax({
    url: "https://swapi-api.hbtn.io/api/films/?format=json",
    type: "GET",
    dataType: "json",
    success: function (data) {
      for (let i = 0; i < data.results.length; i++) {
        $("UL#list_movies").append("<li>" + data.results[i].title + "</li>");
      }
    },
    error: function () {
      $("DIV#character").text("An error occurred while fetching data");
    },
  });
});
