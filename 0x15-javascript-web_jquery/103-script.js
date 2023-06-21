$(document).ready(function () {
  $("#btn_translate #language_code").keypress(function (e) {
    if (e.which == 13) {
      const lang = $("#language_code").val();
      $.ajax({
        url: `https://fourtonfish.com/hellosalut/?lang=${lang}`,
        type: "GET",
        dataType: "json",
        success: function (data) {
          $("DIV#hello").text(data.hello);
        },
      });
    }
  });
});
