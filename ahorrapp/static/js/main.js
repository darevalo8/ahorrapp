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

//esta seccion es en las consultas con manejo de fecha
moment.locale('es-do');
var mes_actual = moment().month();
var ano_actual = moment().year();
document.getElementById('incremento').addEventListener('click', incremento_fecha);
document.getElementById('decremento').addEventListener('click', decremento_fecha);
function mostrar_fecha() {

	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
}
function decremento_fecha() {
	if(mes_actual >=0 && mes_actual <=11){
		mes_actual = mes_actual -1;
	}
	if(mes_actual < 0){
		mes_actual = 11;
		ano_actual -= 1;
	}
	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
	consulta(mes_actual, ano_actual);
}
function incremento_fecha() {
	if(mes_actual >=0 && mes_actual <=11){
		mes_actual = mes_actual +1;
	}
	if(mes_actual > 11){
		mes_actual = 0;
		ano_actual +=1;
	}
	document.getElementById('mes').innerHTML= moment().month(mes_actual).format("MMMM");
	document.getElementById('año').innerHTML= moment().year(ano_actual).format("YYYY");
	consulta(mes_actual, ano_actual);
}