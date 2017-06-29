/**
 * Created by goo on 27.05.17.
 */

$("#checkname").click(function () {

//Отправка Ajax на сервер
    $.ajax({

    type:"GET",
    url:"check_username/",
    date:{
        'user_name': $("username").val(),
    },
    dataType: "text",
    cache: false,
    success: function (date) {
        if (date == 'yes'){

        }
        else if (date == 'no'){


        }
    }


    });

})