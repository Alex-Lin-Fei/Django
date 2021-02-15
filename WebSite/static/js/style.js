$(document).ready(function () {
    var $table = $('.sortable');

    var $headers = $table
        .find('thead th')
        .slice(1);

    $headers
        .each(function () {
            var keyType = this.className.replace(/^sort-/, '');
            $(this).data('keyType', keyType);
        })
        .wrapInner('<a href="#"></a>')
        .addClass('sort');

    var sortKeys = {
        tag: function ($cell) {
            var key = $cell.text().length;
            return key.length;
        },
        price: function ($cell) {
            var num = $cell.text().replace(/^[^\d.]*/, '');
            var key = parseFloat(num);
            if (isNaN(key)) {
                key = 0;
            }
            return key;
        },
        datetime: function ($cell) {
            var key = Date.parse('1 ' + $cell.text());
            return key;
        }
    };

    $headers.on('click', function (event) {
        event.preventDefault();
        var $header = $(this);
        var column = $header.index();
        var keyType = $header.data('keyType');
        var sortDirection = 1;

        if (!$.isFunction(sortKeys[keyType])) {
            return;
        }

        if ($header.hasClass('sorted-asc')) {
            sortDirection = -1;
        }

        var rows = $table.find('tbody > tr').each(function () {
            var $cell = $(this).children('td').eq(column);
            $(this).data('sortKey', sortKeys[keyType]($cell));
        }).get();

        rows.sort(function (a, b) {
            var keyA = $(a).data('sortKey');
            var keyB = $(b).data('sortKey');
            if (keyA < keyB) {
                return -sortDirection;
            } else if (keyA > keyB) {
                return sortDirection;
            } else
                return 0;
        });

        $header.removeClass('sorted-asc sorted-desc');
        $header.addClass(sortDirection === 1 ? 'sorted-asc' : 'sorted-desc');

        $.each(rows, function (index, row) {
            $table.children('tbody').append(row);
        })
    });

    $('ul#rNav li').click(function () {
        var type = $(this).index() + 1;
        var url = '/saltfish/';

        if ($(this).attr("class") === "order-type") {
            url += 'get_order/';
        } else if ($(this).attr('class') === "record-type") {
            url += 'get_record/';
        } else if ($(this).attr('class') === "category-type") {
            url += 'get_category/';
        }

        $.get(url, {'type': type}, function (data) {
            $('#data-table').html(data);
        });
    });

    $('#navbar li').hover(function () {
        $(this).addClass('active');
    }, function () {
        $(this).removeClass('active');
    });

//    搜索框
    $('#suggestion').keyup(function () {
        var query = $(this).val();
        $.get('/saltfish/suggest/', {suggestion: query}, function (data) {
           $('#result').html(data);
        });
    });

});