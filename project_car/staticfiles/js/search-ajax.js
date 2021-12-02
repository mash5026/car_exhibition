$(function() {
    $('#search').keyup(function() {
        $.ajax({
            type: "GET",
            url: '/',
            data: {
                'search_text': $('#search').val()
            },
            success: SearchSucces,
            dataType: "html"
        })
    })
})

function SearchSucces(data, textStatus, jqXHR) {
    $("#self_result").html(data)
    console.log(data)
}