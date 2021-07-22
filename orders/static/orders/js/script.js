$(document).ready(function(){

  $('#statusFilter').change(function(){
    console.log("status func");
    var url = $('#filterStatus').attr('filter-status');
    console.log(url);
    var status = $(this).val();
    console.log(status);



        $.ajax({
            url:url,
            data:{
                'status':status,
            },
            success: function (data){
                console.log(data);
                $("#filtered").html(data);
                $("#filtered").show;
                $('#defaultfilter').fadeOut();

            }
        });

  });

});
