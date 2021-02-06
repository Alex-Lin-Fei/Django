$(document).ready(function() {
    $('#likes').click(function () {
        var catid;
        catid = $(this).attr('data-catid');
        $.get('/myrango/like/', {category_id: catid}, function (data) {
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });

    $('#suggestion').keyup(function () {
        var query = $(this).val();
        $.get('/myrango/suggest/', {suggestion: query}, function (data) {
            $('#cats').html(data);
        });
    });
});