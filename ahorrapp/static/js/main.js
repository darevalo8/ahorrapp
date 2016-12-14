/**
 * Created by darevalo on 30/11/16.
 */
$(".button-collapse").sideNav();
$(".dropdown-button").dropdown();
function saludo() {
	var dia = 12;
	var tarde = 17;
	var time = moment().format('HH');
	var user = document.getElementById('saludo').innerHTML;
	if(time >= dia && time <= tarde){
		document.getElementById('saludo').innerHTML = 'Buenas tardes, '+user;
	}else if (time >= tarde){
		document.getElementById('saludo').innerHTML = 'Buenas noches, '+user;
	}else{
		document.getElementById('saludo').innerHTML = 'Buenos días, '+user;
	}
}
/*codigo para eliminar elementos*/
// function eliminar(text, enlance) {
// 	$('.eliminar').click(function () {
//             var id = $(this).attr("id");
//             console.log(id);
//             swal({
//                         title: "Estas seguro?",
//                         text:  text,
//                         type: "warning",
//                         showCancelButton: true,
//                         confirmButtonColor: "#DD6B55",
//                         confirmButtonText: "Si, borrarla!",
//                         closeOnConfirm: false
//             },
//                     function(){
//
//                         div_deleted = 'div#' + id;
//                         console.log(div_deleted);
//                         url_id = enlance + id;
//                         $.ajax({
//                             url: url_id,
//                             type: 'get',
//                             success: function (data) {
//                                 console.log(data);
//                                 $(div_deleted).hide();
//                                 swal("Deleted!", "Se elimino correctamente.", "success");
//                             }
//                         });
//             });
//         });
// }
