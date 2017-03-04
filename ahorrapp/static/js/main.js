/**
 * Created by darevalo on 30/11/16.
 */

$(".button-collapse").sideNav();
$(".dropdown-button").dropdown();
$(document).ajaxStart(function () {
	$('#mensaje').remove();
	$('#loader').show();
}).ajaxStop(function () {
	$('#loader').hide();
});
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
//esta seccion es en las consultas con manejo de fecha
moment.locale('es');
var mes_actual = moment().month();
var ano_actual = moment().year();
function mostrar_fecha() {

	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
}
function decremento_fecha(model) {
	if(mes_actual >=0 && mes_actual <=11){
		mes_actual = mes_actual -1;
	}
	if(mes_actual < 0){
		mes_actual = 11;
		ano_actual -= 1;
	}
	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
	consulta(mes_actual, ano_actual, model);
}
function incremento_fecha(model) {
	if(mes_actual >=0 && mes_actual <=11){
		mes_actual = mes_actual +1;
	}
	if(mes_actual > 11){
		mes_actual = 0;
		ano_actual +=1;
	}
	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
	consulta(mes_actual, ano_actual, model);
}
function consulta(mes, year, model) {
	var model_url, text_model, obj_model;
	obj_model = model;
	mes +=1;
	if (obj_model === 'income'){
		text_model = 'ingresos';
	}else if(obj_model === 'expense'){
		text_model = 'gastos';
	}else if(obj_model === 'obligation'){
		text_model = 'obligaciones';
	}else if(obj_model === 'cuenta_i'
		|| obj_model === 'tipo_i' ||
		obj_model === 'cuenta_expense' ||
		obj_model === 'tipo_expense'){
		text_model = 'datos en este mes';
	}
	model_url = url_model(obj_model, 'consulta');
	$.ajax({
		data: {'mes': mes, 'year': year},
		url: model_url,
		type: 'get',
		success: function (data) {
			var mensaje = '<p id="mensaje">No hay '+ text_model +'</p>';
			$('.remover').remove();
			if(data.length > 0){
				mostrar_datos(data, obj_model);
				$('#mensaje').hide();
			}else{
				$('#main').append(mensaje);
			}
		}

	});
}
function url_model(model, type) {
	var url;
	//tipo_e o tipo_i es igual a tipo_expense,
	//igual con account_i y asi ahi que acomodar a un solo estandar
	if(type === 'delete'){
		if(model === 'income'){
			url = '/cuentas/delete/ingreso/';
		}else if(model === 'expense'){
			url = '/gastos/delete/';
		}else if(model === 'obligation'){
			url = '/obligaciones/delete/';
		}else if (model === 'account'){
			url = '/cuentas/delete/';
		}else if(model === 'type_i'){
			url = '/cuentas/delete/type/';
		}else if(model === 'type_e'){
			url = '/gastos/delete/type-expense/';
		}
	}else if (type === 'consulta'){
		if(model === 'income'){
			url = '/cuentas/consulta-ingreso/';
		}else if (model === 'expense'){
			url = '/gastos/consulta-gasto/';
		}else if(model === 'obligation'){
			url = '/obligaciones/consulta-obligacion/';
		}else if (model === 'cuenta_i'){
			url = '/cuentas/group-account/';
		}else if (model === 'tipo_i'){
			url = '/cuentas/group-type/';
		}else if(model === 'cuenta_expense'){
			url = '/gastos/expense-account/';
		}else if(model === 'tipo_expense'){
			url = '/gastos/expense-type/';
		}
	}
	return url;
}
function mostrar_datos(data, model){
	var tpl = '', obj_model, fields;
	obj_model = model;
	if(obj_model === 'income'){
		data.forEach(function (obj) {
			var value_income;
			fields = obj.fields;
			value_income = number_format(fields.valor_ingreso);
			tpl = '<div id="'+ obj.pk + '" class="remover">'
				+ '<ul class="collapsible" data-collapsible="accordion">'
				+'<li>'
				+'<div class="collapsible-header">'
				+'<i class="material-icons">keyboard_arrow_down</i>'
				+'<span>' + fields.nombre_ingreso + '</span>'
				+'<a href="#"><span>'
				+'<i class="material-icons right eliminar" id="' + obj.pk + '">delete</i>'
				+'</span>'
				+'</a>'
				+'<a href="/cuentas/edit/ingreso/'+obj.pk+'/"><span>'
				+'<i class="material-icons right edit">mode_edit</i>'
				+'</span></a>'
				+'</div>'
				+'<div class="collapsible-body">'
				+'<p>Valor: $ '+ value_income +'</p>'
				+'<p>Cuenta: '+ fields.account +'</p>'
				+'<p>Tipo de ingreso: '+ fields.type_income +'</p>'
				+'<p>Descripción:'+ fields.desciption +'</p>'
				+'<p>Creada el '+ fields.created +'</p>'
				+'</div>'
				+'</li>'
				+'</ul>'
				+'</div>';
			$('#main').append(tpl);
		});
	}else if (obj_model === 'expense'){
		data.forEach(function (obj) {
			var value_expense;
			fields = obj.fields;
			value_expense = number_format(fields.value_expense);
			tpl = '<div id="'+ obj.pk + '" class="remover">'
				+ '<ul class="collapsible" data-collapsible="accordion">'
				+'<li>'
				+'<div class="collapsible-header">'
				+'<i class="material-icons">keyboard_arrow_down</i>'
				+'<span>' + fields.name_expense + '</span>'
				+'<a href="#"><span>'
				+'<i class="material-icons right eliminar" id="' + obj.pk + '">delete</i>'
				+'</span>'
				+'</a>'
				+'<a href="/gastos/editar/'+obj.pk+'/"><span>'
				+'<i class="material-icons right edit">mode_edit</i>'
				+'</span></a>'
				+'</div>'
				+'<div class="collapsible-body">'
				+'<p>Valor: $ '+ value_expense +'</p>'
				+'<p>Cuenta: '+ fields.account +'</p>'
				+'<p>Tipo de gasto: '+ fields.type_expense +'</p>'
				+'<p>Descripción: '+ fields.desciption +'</p>'
				+'<p>Creada el '+ fields.created +'</p>'
				+'</div>'
				+'</li>'
				+'</ul>'
				+'</div>';
			$('#main').append(tpl);
		});
	}else if(obj_model === 'obligation'){
		data.forEach(function (obj) {
			fields = obj.fields;
			var pago, value_obligation;
			value_obligation = number_format(fields.value_obligation);
			if(fields.completed){
				pago = 'Realizado';
			}else {
				pago = 'Pendiente';
			}
			tpl = '<div id="'+ obj.pk + '" class="remover">'
				+'<ul class="collapsible" data-collapsible="accordion">'
				+'<li>'
				+'<div class="collapsible-header">'
				+'<i class="material-icons">keyboard_arrow_down</i>'
				+'<span>' + fields.name_obligation + '</span>'
				+'<a href="#"><span>'
				+'<i class="material-icons right eliminar" id="' + obj.pk + '">delete</i>'
				+'</span>'
				+'</a>'
				+'<a href="/obligaciones/editar/'+obj.pk+'/"><span>'
				+'<i class="material-icons right edit">mode_edit</i>'
				+'</span></a>'
				+'</div>'
				+'<div class="collapsible-body">'
				+'<p>Valor: $ '+ value_obligation +'</p>'
				+'<p>Cuenta: '+ fields.account +'</p>'
				+'<p>Tipo de obligación: '+ fields.type_obligation +'</p>'
				+'<p>Pago: '+ pago +'</p>'
				+'<p>Creada el '+ fields.created +'</p>'
				+'<p>Fecha de vencimiento: '+ fields.end_obligation +'</p>'
				+'</div>'
				+'</li>'
				+'</ul>'
				+'</div>';
			$('#main').append(tpl);
		});
	}else if(obj_model === 'cuenta_i' || obj_model === 'cuenta_expense'){
		data.forEach(function (obj) {
			var total = number_format(obj.total);
			tpl = '<tr class="remover">'
				+'<td>'+ obj.name_account +'</td>'
				+'<td>$ '+ total +'</td>'
				+'</tr>';
			$('#content_table').append(tpl);
		});
	}else if(obj_model === 'tipo_i' || obj_model === 'tipo_expense'){
		data.forEach(function (obj) {
			var total = number_format(obj.total);
			tpl = '<tr class="remover">'
				+'<td>'+ obj.tipo +'</td>'
				+'<td>$ '+ total +'</td>'
				+'</tr>';
			$('#content_table_type').append(tpl);
		});

	}
	$('.collapsible').collapsible();
	$('.eliminar').click(function () {
                var text1, text2, model, id;
                text1 = "¿ Deseas eliminar este ingreso ?";
                text2 = "El ingreso se eliminó correctamente.";
                model = obj_model;
                id = $(this).attr("id");
                console.log(id);
                delete_object(text1, text2, id, model);
            });

}
/**
 *  termina sesion con manejo con fechas
 *  =======================
 *peticiones ajax
*/
function Ajax(title1, title2, text1, text2, id, url) {
	this.title1 = title1;
	this.title2 = title2;
	this.text1 = text1;
	this.text2 = text2;
	this.id = id;
	this.url = url;
}
Ajax.prototype = {
	delete_obj: function () {
		var id, url, title2, text2;
		id = this.id;
		url = this.url;
		title2 = this.title2;
		text2 = this.text2;
		swal({
				title: this.title1,
				text: this.text1,
				type: "warning",
				showCancelButton: true,
				confirmButtonColor: "#DD6B55",
				confirmButtonText: "Si, borrarla!",
				closeOnConfirm: false
		},
			function(){
				var div_deleted = 'div#' + id;
				var url_id = url + id;
				console.log(div_deleted);
				$.ajax({
					url: url_id,
					type: 'get',
					success: function (data) {
						console.log(data);
						$(div_deleted).hide();
						swal(title2, text2, "success");
					}
				});
			});
	}
};
function delete_object(text1, text2, id, model) {
	var title1, title2, obj, url;
	title1 = "¿Esta seguro?";
	title2 = "¡Eliminado!";
	url = url_model(model, 'delete');
	obj = new Ajax(title1, title2, text1, text2, id, url);
	obj.delete_obj();
}
function number_format(amount, decimals) {
	var amount_parts, regexp;
    amount += ''; // por si pasan un numero en vez de un string
	// elimino cualquier cosa que no sea numero o punto
    amount = parseFloat(amount.replace(/[^0-9\.]/g, ''));
	// por si la variable no fue fue pasada
    decimals = decimals || 0;

    // si no es un numero o es igual a cero retorno el mismo cero
    if (isNaN(amount) || amount === 0)
        return parseFloat(0).toFixed(decimals);

    // si es mayor o menor que cero retorno el valor formateado como numero
    amount = '' + amount.toFixed(decimals);

    amount_parts = amount.split('.');
	regexp = /(\d+)(\d{3})/;

    while (regexp.test(amount_parts[0]))
        amount_parts[0] = amount_parts[0].replace(regexp, '$1' + '.' + '$2');

    return amount_parts.join('.');
}