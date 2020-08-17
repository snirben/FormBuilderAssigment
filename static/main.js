



$(document).ready( function () {
    $('#form_list').DataTable({
         rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true
    });

    $('#submissionstable').DataTable({
         rowReorder: {
            selector: 'td:nth-child(2)'
        },
        responsive: true
    });
} );




var addfield = function (type, inputname, fieldlabel) {
    $("#form-area").append('<div class="form-group ">\n' +
        '  <label for="usr">' + fieldlabel + '</label>\n' +
        '  <input name="' + inputname + '" type="' + type + '" class="form-control">\n' +
        '</div>'
    )
}

var ajaxSubmit = function (data) {

    data["form_name"] = $("#form_name").text()
    // var csrf_token = $("[name='csrfmiddlewaretoken']").val();
    // ajax form submit
    $.ajax({
        url: '/ajax/form_create/',
        type: 'GET',
        dataType: 'json',
        //   headers: {'X-CSRFToken': csrf_token},
        data: {'data': JSON.stringify(data)},
        success: function (data) {
            if(data["hogback"]==="ok")
                window.location.replace(window.location.origin);


        }

    });

};


var ajaxSubmitform = function () {
    var data = {}
    data["input"] = []
    $("input").each(function () {
        data["input"].push({"id": $(this).attr("val"),"name":$(this).attr("name"), "input": $(this).val(), "type": $(this).attr("type")})
    })
    data["formid"]=$(".form_title").attr("value")
     var csrf_token = $("[name='csrfmiddlewaretoken']").val();
    // ajax form submit
    $.ajax({
        url: '/ajax/form_submit/',
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf_token},
        data: {'data': JSON.stringify(data)},
        success: function (data) {
            if(data["hogback"]==="ok")
                window.location.replace(window.location.origin);


        }
    });
};

$(document).ready(function () {
    var list = {};
    list["fields"] = []
    // add new field handler
    $(document).on('click', '#add-new-field', function () {
        var type = $("#inputType").val();
        var inputname = $("#inputName").val();
        var fieldlabel = $("#inputLabel").val();
        list["fields"].push({"type": type, "inputname": inputname, "fieldlabel": fieldlabel})
        addfield(type, inputname, fieldlabel)

    });


    $(document).on('click', '.create-form', function (e) {
        e.preventDefault();
        ajaxSubmit(list);

    });

    $(document).on('click', '.submit-form', function (e) {
        e.preventDefault();
        ajaxSubmitform();

    });

});