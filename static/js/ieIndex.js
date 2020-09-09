$(document).ready(function(){
    $('#id_tipo').change(function(){
        if($(this).val()==""){
            $('#egreso').hide();
            $('#ingreso').hide();
            $('#mensaje').show();
        }
        if($(this).val()=="Ingreso"){
            $('#ingreso').show();
            $('#egreso').hide();
            $('#mensaje').hide();
            
        }
        if($(this).val()=="Egreso"){
            $('#mensaje').hide();
            $('#egreso').show();
            $('#ingreso').hide();

        }
    });
  }); 