jQuery.fn.dataTable.Api.register( 'sum()', function ( ) {
	return this.flatten().reduce( function ( a, b ) {
		if ( typeof a === 'string' ) {
			a = a.replace(/[^\d.-]/g, '') * 1;
		}
		if ( typeof b === 'string' ) {
			b = b.replace(/[^\d.-]/g, '') * 1;
		}

		return a + b;
	}, 0 );
} );
$(document).ready(function(){
        $('#tablaReporte').DataTable({
            drawCallback: function () {
                  var api = this.api();
                  $( api.table().footer() ).html(
                        $('#suma').text(api.column( 3, {page:'current'} ).data().sum())
                  );
                }
        });
  }); 