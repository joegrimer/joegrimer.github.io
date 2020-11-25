/* go.js
 *
 * this javascript file contains the main functionality for go.html
 * - a program intended to simulate a go game
 * 23/1/2014
 */

var BLACK = 'rgb(0, 0, 0)';
var WHITE = 'rgb(255, 255, 255)';
var EMPTY = 'rgba(0, 0, 0, 0)';
var TURN; // will be initialised as black
var gridSize = 7; // change this variable to easily change grid size
var chain = []; // this will be populated when chains are scanned
var koPiece; // a similified ko variable to solve the ko problem
var lastKiller = ""; // used by ko

// initialisation functions ----------------------------------------------------

function init() {
	
	// make sure the grid size wont cause problems
	if (gridSize<7) gridSize = 7;
	else if (gridSize>19) gridSize = 19;
	
	// generates the grid the user can see
	generate_under_grid('underGrid');
	
	// generates the "peg board"
	generate_table('mainTable');
	
	// sets the turn to black
	TURN = BLACK;
}

// generates HTML for the table that the user clicks on
function generate_table(_tableId) {

	var content = "<tbody>";
	var topSize = gridSize + 1;

	for (var j = 1; j < topSize; j++) {

		content += "<tr>";
		for (var i = 1; i < topSize; i++) {
			content += "<td id='" + j +
				"x" + i + "' onclick=\"place('" + j + "x" + i + "')\">"+
				"</td>";
		}
		content += "</tr>";
	}
	content += "</tbody>";

	$("#" + _tableId).html(content);
}

// generates the HTML for the visible grid
function generate_under_grid(_gridID) {

	var underSize = gridSize - 1;
	var data = "<tbody>";

	for (var j = 0; j < underSize; j++) {
		data += "<tr>";
		for (var i = 0; i < underSize; i++) {
			data += "<td></td>";
		}
		data += "</tr>";
	}

	data += "</tbody>";

	$("#" + _gridID).html(data);
}

// main functions (triggered by user's clicks) ---------------------------------

// this function is called when user click on a new empty cell
function place(_cellId) {
	if(legal(_cellId)) playOn(_cellId);
	else alert("Illegal Move!"); //+ "Piece There", "Ko" or "Suicide"
}

function legal(_cellId) {

//	return true;
	// this function is the main meat of the program,
	// to basically look for surrounded groups:
	if(checkChains(_cellId)) return true;
	else return false;

//	if ($("#" + _cellId).css('backgroundColor') == EMPTY) return true;
}

function playOn(_cellId) {

	// actually put the pebble on the board
	putPebble(_cellId);

	// kill off bad guys
	
	// tell the user whose turn it is
	updateTurn();
}

// for actually putting the pebble on the board
function putPebble(_cellId) {
	if (TURN == BLACK) {
		$("#" + _cellId).css("backgroundColor", "#000");
	}
	else if (TURN == WHITE) {
		$("#" + _cellId).css("backgroundColor", "#FFF");
	} else tsnh();
}

function checkChains(_cellId) {

	var placeLibs = scanForLife();
	
	a(placeLibs);
//	return true;
	
//	a(placeLibs[coords[0]-1][coords[1]-1]);

	if (suicidal([_cellId],placeLibs)) return false;
	else return true;
//	if placeLibs()

	
}

function scanForLife() {

	var topSize = gridSize + 1;
	var gridValues = [];

	for (var j = 1; j < topSize; j++) {
		gridValues.push([]);
		for (var i = 1; i < topSize; i++) {
			gridValues[j-1].push(cellState((i)+"x"+(j)));
		}
	}
	return gridValues;
}

function cellState(_cellId) {

	var compass = getBearings(_cellId);
	var count = 0;

	var color = $("#"+_cellId).css('backgroundColor');
	
	
	if((color !=EMPTY) && (color != TURN)) return 0;
	
	for (n=0;n<4;n++) {
		var color = $("#" + compass[n]).css('backgroundColor');

		if (!color || ((color !=EMPTY) && (color != TURN))) continue;
		else return 1;
	}
	return 0;
}

// checks if current move is suicidal for a chain
function suicidal(_chain,_placeLibs) {

	var coords = _chain[_chain.length-1].split("x");

//	aa(_placeLibs);
//	a(_placeLibs[coords[0]-1][coords[1]-1]);
	
//	return false;
	
	if(_placeLibs[coords[0]-1][coords[1]-1]==1) return false;
//	aa(_placeLibs);
//	else if(_placeLibs[coords[0]-1][coords[1]-1]==1) return false;

//	var compass = getBearings(_chain[_chain.length-1]);
//	a(compass+_chain[_chain.length-1]);/*
/*
	for(i in compass) {
		a(compass[i]);
		if (searchAry(_chain,compass[i])) {a("iffy");continue;}
		else {_chain.push(compass[i]); a("pushy")}
		
		if (suicidal(_chain,_placeLibs)) return true;
	}*/
	return true;
}
// this function is the main meat of the program,
// to basically look for surrounding groups:
function beginCheck(_curCell) {

	var compass = getBearings(_curCell);
	var murder = 0;

	// check all other pieces
	for (q = 0; q < compass.length; q++) {
		if (haveBG(compass[q]) && !sameColor(_curCell, compass[q]) && !findChain(compass[q]) /*&& !repeating(_curCell)*/) {
			destroyChain(_curCell);
		murder = 1;
		}
		chain = []
	}

	if ( !murder && (surrounded(_curCell) || !findChain(_curCell)) ) {
		revTurn(_curCell);
		updateTurn();
		alert("Illegal Move! Surrounded?");
	}

	chain=[]
}

// this changes from black to white in the heading based on variable turn
function updateTurn() {

	if (TURN == BLACK) {
		var colour = "White"
		TURN = WHITE
	} else {
		var colour = "Black"
		TURN = BLACK
	}

	$("#turnBox").html(colour + "'s Turn")
}

// sub-functions of the functions that place calls -----------------------------------------------------------------------------------------------

// returns cell bearings
function getBearings(_curCell) {

	var cellAry = _curCell.split("x")

	var bearings = [((parseInt(cellAry[0]) - 1) + "x" + cellAry[1]),
									(cellAry[0] + "x" + (parseInt(cellAry[1]) + 1)),
									((parseInt(cellAry[0]) + 1) + "x" + cellAry[1]),
									(cellAry[0] + "x" + (parseInt(cellAry[1]) - 1))]

	return bearings
}

// a fairly simple function to check if a spot actually has a background colour
function haveBG(_id) {

	if ($("#" + _id).css("backgroundColor") == EMPTY) {return false}
	else return true
}

// function to actually find a chain!
function findChain(_curPeg) {

	chain.push(_curPeg)

	if(!document.getElementById(_curPeg)) return false

	var compass = getBearings(_curPeg)

	if (!haveBG(compass[0]) || !haveBG(compass[1]) || !haveBG(compass[2]) || !haveBG(compass[3]) ||
		 (!searchAry(chain, compass[0]) && sameColor(compass[0], _curPeg) && findChain(compass[0])) ||
		 (!searchAry(chain, compass[1]) && sameColor(compass[1], _curPeg) && findChain(compass[1])) ||
		 (!searchAry(chain, compass[2]) && sameColor(compass[2], _curPeg) && findChain(compass[2])) ||
		 (!searchAry(chain, compass[3]) && sameColor(compass[3], _curPeg) && findChain(compass[3]))) {

		return true
	} else {
		return false
	}
}

// checks for the ko rule - not really!
function ruleOfKo(_curCell) {

	if(koPiece == _curCell) {
		return true
	} else return false
}

// checks if two cells are the same colour or not
function sameColor(_cellid1, _cellid2) {

	if ($("#" + _cellid1).css("backgroundColor") ==
			$("#" + _cellid2).css("backgroundColor")) {
		return true
	} else {
		return false
	}
}

// for destroying chains (pebble groups)
function destroyChain(_curCell) {

	if (chain.length == 1) koPiece = chain;
	lastKiller = _curCell

	for (k = 0; k < chain.length; k++) {
		$("#" + chain[k]).fadeTo("slow", 0, function() {
			$(this).css({
				"backgroundColor": "",
				"opacity": 1
			})
		})
	}
}

// this function checks if the piece is surrounded and returns true if it is
function surrounded(_cellId) {

	var compass = getBearings(_cellId);
	var count = 0;
	var curColour = $("#" + _cellId).css('backgroundColor');

	for (n=0;n<4;n++) {
		if (!document.getElementById(compass[n]) ||
			($("#" + compass[n]).css('backgroundColor') != curColour) != TURN) {
			count = count + 1;
		}
	}

	if (count > 0) return false
	else return true
}

// reverse the turn(illegal move)
function revTurn(_curCell) {

	$("#" + _curCell).fadeTo("slow", 0, function() {
		$(this).css({
			"backgroundColor": "",
			"opacity": 1
		})
	})

}

// ai functions ----------------------------------------------------------------

function aiMain() {

//	boardVals = scanBoard();
	
	for(i=0;i<boardVals.length;i++) {
		for(j=0;j<boardVals[i].length;j++) {
			boardVals[i][j] = libertyCount((i+1)+"x"+(j+1));
		}
	}
	
// update values based on nearby liberties
	boardVals = passValues(boardVals,3);
	
// heat map
/*
	for(m=0;m<boardVals.length;m++) {
		for(n=0;n<boardVals[m].length;n++) {
			var num=boardVals[m][n].toString();
			while(num.length < 6) num=num+"0";
//			alert("after while"+num);
//				alert(num);
				$("#" + (m+1)+"x"+(n+1)).css("backgroundColor", "#" + num);
		}
	}*/

	var bestCoords = [0];

	for(o=0;o<boardVals.length;o++) {
		for(p=0;p<boardVals[o].length;p++) {
			if($("#"+(o+1)+"x"+(p+1)).css('backgroundColor')!=EMPTY)
				continue;
			else if(surrounded2("#"+(o+1)+"x"+(p+1)))
				alert(o+p);
			else if(boardVals[o][p] > bestCoords[0])
				bestCoords=[boardVals[o][p],o+1,p+1];
		}
	}

//	alert(bestCoords);
//	randCoor = Math.floor((Math.random() * boardVals.length) + 1) ;
	doMove(bestCoords[1]+"x"+bestCoords[2]);
}

function passValues(oldVals,times) {

	for(i=0;i<times;i++) {
		var newVals=[];
		for(k=0;k<oldVals.length;k++) {
			newVals.push(oldVals[k].slice(0));
			for(l=0;l<oldVals[k].length;l++) {

				if( k>0 )					newVals[k][l]=newVals[k][l]+oldVals[k-1][l];
				else						newVals[k][l]=newVals[k][l]-2
				if( k<oldVals.length-1 ) 	newVals[k][l]=newVals[k][l]+oldVals[k+1][l];
				else						newVals[k][l]=newVals[k][l]-2
				if( l>0 )					newVals[k][l]=newVals[k][l]+oldVals[k][l-1];
				else						newVals[k][l]=newVals[k][l]-2
				if( l<oldVals.length-1 )	newVals[k][l]=newVals[k][l]+oldVals[k][l+1];
				else						newVals[k][l]=newVals[k][l]-2
			}
		}
		oldVals=newVals;
	}
	return newVals;
}

function scanBoardAi() {

	var topSize = gridSize + 1;
	var gridValues = [];

	for (var j = 1; j < topSize; j++) {
		gridValues.push([]);
		for (var i = 1; i < topSize; i++) {
			gridValues[j-1].push(0);
		}
	}
	return gridValues;
}

// this function checks if the piece is surrounded and returns true if it is
function surrounded2(_cellId) {

//	alert("thank heaven!");

	var compass = getBearings(_cellId);
	var count = 0;

	for (n=0;n<4;n++) {
		if (document.getElementById(compass[n]) &&
				($("#" + compass[n]).css('backgroundColor') != TURN) ) {
			count++;
		}
	}

	if (count < 4) echos=1;//return false
	else alert("1!");
	//else return true
	
//	return true;
}
/*
function libertyCount(_cellId) {

	var compass = getBearings(_cellId);
	var count = 0;

	for (n=0;n<4;n++) {
		var color = $("#" + compass[n]).css('backgroundColor');
		if (!color) continue;
		if (color == turn || color == EMPTY) {
			count++;
		} else count--;
	}
	return count;
}*/

// saving and loading functions ------------------------------------------------

function saveGame() {

	if($("#save").html()=="save") {
	
		var saveData=fetchSaveData()
	
		$("#dataText").css("display","block")
		$("#dataText").val(saveData.toString())
		$("#save").html("done")
		$("#load").html("")
	} else {

	$("#dataText").css("display","none")
	$("#dataText").html("")
	$("#save").html("save")
	$("#load").html("load")
	}
}

function fetchSaveData() {

		var gridData=new Array()
		if(turn==BLACK) gridData.push("d" + gridSize)
		else gridData.push("l" + gridSize)
		
		for (var j = 1; j <=gridSize; j++) {
			for (var k = 1; k <=gridSize; k++) {
				var curSpace = j + "x" + k
				if(haveBG(curSpace)) {
					if ($("#" + curSpace).css("backgroundColor") == WHITE) {
						gridData.push(j+"l"+ k)
					} else {
						gridData.push(j+"d"+ k)
					}
				}
			}
		}
		return gridData
}

function loadGame() {

	if($("#load").html()=="load") {

		$("#dataText").css("display","block")
		$("#load").html("done")
		$("#save").html("")

	} else {

		if ($("#dataText").val()) {
		
			var newData = $("#dataText").val().split(",")
			gridSize = parseInt(newData[0].split(newData[0].charAt(0))[1])
			prepGame()
			if(newData.length>1) applyLoadData(newData)
			if(newData[0].charAt(0)=='l') updateTurn()
		} else prepGame
		
		$("#dataText").css("display","none")
		$("#save").html("save")
		$("#load").html("load")
	}
}

function applyLoadData(_newData) {

	var numPoint
	var tempVar

	for(l=1;l<_newData.length;l++) {
		for(numPoint=1;numPoint<=_newData.length;numPoint++) {
			if(isNaN(_newData[l].charAt(numPoint))) break
		}
		if(_newData[l].charAt(numPoint)=="l") {
			tempVar = _newData[l].split("l")
			$("#" + tempVar[0] + "x" + tempVar[1]).css("backgroundColor", "#fff")
		} else if(_newData[l].charAt(numPoint)=="d") {
			tempVar = _newData[l].split("d")
			$("#" + tempVar[0] + "x" + tempVar[1]).css("backgroundColor", "#000")
		}
	}
	return true
}

// generic functions -----------------------------------------------------------

function tsnh(){
	a("this should never happen")
	return false
}

// simpler alert
function a(_str) {

	alert(_str)
}

// simpler alert
function aa(_str) {

	alert(_str.join("\n"))
}

// alertv
function av(_str, _var) {

	a(_str + " is >" + _var + "<")
}

function searchAry(_list, _value) {

	if (-1 != _list.toString().search(_value)) {
		return true
	} else {
		return false
	}
}



/*
function deLib(states) {

	while(true) {
		a("before"+states.join("\n"));
		var changedAnything = false;
		for(k=0;k<states.length;k++) {
			for(l=0;l<states[k].length;l++) {
				var originalNo = states[k][l];

				if( k>0 )						states[k][l]+=states[k-1][l];
				else if( k<states.length-1 ) 	states[k][l]+=states[k+1][l];
				else if( l>0 )					states[k][l]+=states[k][l-1];
				else if( l<states.length-1 )	states[k][l]+=states[k][l+1];
				
				if(states[k][l]>0) states[k][l] = 1;
				if(originalNo!=states[k][l]) changedAnything=true;
			}
		}
//		break;
		if (!changedAnything) break;
	}
	a("afta"+states.join("\n"));
//	a(states.join("\n"));
	return states;
}*/
