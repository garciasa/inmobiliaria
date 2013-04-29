$(document).ready(function () {
    $(":button").not(':input[type=submit]').click(function(){
        var data = this.id;
        var arr = data.strip("-");
        $.ajax({
            type: "POST",
            url: url_modificar + arr[2],
            data: { id_img: arr[3] },
            success: function(response){
                return false;
            }
        });

        return false;
    });


});