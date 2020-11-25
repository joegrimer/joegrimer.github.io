/* This javascript file finds the source of the flash game and inserts
 a link giving the ability to enjoy the flash game in fullscreen*/
var bod;
checkurl();

  if (bod == "11") {alert("Fullscreen Mode is unavailable in this game, as of yet. Miniclip Improved.");return;
  } else {getflash();}

function checkurl() {
  var links = document.location.href;
  if(links == "http://www.miniclip.com/games/runescape/en/") {
  bod = "11";
  } else if (links == "http://www.miniclip.com/games/migo-land/en/") {
  bod = "11";
  } else {return;}
}
  
function getflash() {
  var gbox = document.getElementById('gameContainer');
  var data = gbox.innerHTML
  var quote = data.split('src="');
  var srcs = quote[1].split('"');
  var end = srcs[0];
  putflash(end);
}

function putflash(end) {
  var x = document.createElement('div');
  document.getElementById('wrapper').appendChild(x);
  x.setAttribute('id','gfull');
  if (end == "gameloader.dcr"){
  document.getElementById('gfull').innerHTML="Fullscreen Mode Unavailable";
  } else {
  document.getElementById('gfull').innerHTML="<a href='" + end + "'>Play Game in Fullscreen</a>";
  }
}

/*End of javascript file*/
