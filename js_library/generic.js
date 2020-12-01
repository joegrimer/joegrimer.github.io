/*
	This javascript file is full of generic functions that I hope to turn ito some kind of awesome 'library' some day :)
	Joseph Grimer, 17:10, 25th of May, 2011
*/

	var alertXNumber = 0;

function checkEnter() {

	if (window.event.keyCode == 13) {
		return true;
	} else {
		return false;
	}
}

function getId(_id) {
	return document.getElementById(_id);	
}

function getIdCont(_id) {
	var data = document.getElementById(_id).innerHTML;
	return data;
}
  
function getIdVal(_id) {
	var data = document.getElementById(_id).value;
	return data;
}
  
function alertx(_what) {

	var dSplit = arguments.callee.caller.toString().split("{");
	var fNam = dSplit[0];
	var fName = fNam.split("function ")[1];
	
	alertXNumber = alertXNumber + 1;

	alert(fName +  "{" + alertXNumber +"} says\n>" + _what + "<");
}

