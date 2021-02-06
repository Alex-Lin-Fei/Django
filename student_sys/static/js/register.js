$(document).ready(function () {
    $('#register').click(function () {
        $.post('/student/register/', {
            name: $('#name').val(),
            sex: $('#sex').val(),
            profession: $('#profession').val(),
            email: $('#email').val(),
            qq: $('#qq').val(),
            phone: $('#phone').val()
        }, function (data) {
            $('#text').html(data);
        });
    });
});