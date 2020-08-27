$(document).ready(function(){
    $('#id_paciente').change(function(){
        $.ajax({
            url : 'getPaciente',
            data:{id:$(this).val()},
            type:'GET',
            dataType:'json',
            success:function(result){
                if(result["success"]==true){
                    $('#telefono').val(result["telefono"]);
                    $('#edad').val(result["edad"]);
                }
            }
        })
    })
  }); 