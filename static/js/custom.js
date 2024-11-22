$(document).ready(function () {
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.event_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.event_data').find('.qty-input').val(value)
        }
    });
    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var dec_value = $(this).closest('.event_data').find('.qty-input').val();
        var value = parseInt(dec_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.event_data').find('.qty-input').val(value);
        }
    });
    $('.addtoQueuesbtn').click(function (e) {
        e.preventDefault();

        var event_id = $(this).closest('.event_data').find('.evt_id').val();
        var event_qty = $(this).closest('.event_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/add-to-queues",
            data: {
                'event_id': event_id,
                'event_qty': event_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
                // console.log(response)
            }
        });
    });
    $('.changeQuantity').click(function (e) {
        e.preventDefault();

        var event_id = $(this).closest('.event_data').find('.evt_id').val();
        var event_qty = $(this).closest('.event_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/update-queues",
            data: {
                'event_id': event_id,
                'event_qty': event_qty,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                // alertify.success(response.status)
                // console.log(response)
            }
        });
    });
    $(document).on('click', '.delete-cart-item', function(e) {
        e.preventDefault();
        var event_id = $(this).closest('.event_data').find('.evt_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "delete-cart-item",
            data: {
                'event_id': event_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status)
                $('.queuesdata').load(location.href + " .queuesdata");
                // console.log(response)
            }
        });

    });
});
