$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
        const lang = $("INPUT#language_code").val();
        $.ajax({
            url: `https://fourtonfish.com/hellosalut/?lang=${lang}`,
            type: "GET",
            dataType: "json",
            success: function (data) {
                $("DIV#hello").text(data.hello);
            }
        });
    });
});
