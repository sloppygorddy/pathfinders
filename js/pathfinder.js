function colorNormal(x, y, color) {
    var chessBoard = document.getElementById("chessBoardNormal");
    for (var i = 0; i < x; i++) {
        var row = chessBoard.appendChild(document.createElement("div"));
        for (var j = 0; j < y; j++) {
            var span = document.createElement('span');
            span.style.backgroundColor = "green";
            // if(i & 1){ // odd
            //     if(j & 1){ // white
            //     	span.style.backgroundColor = "black";
            //     	// span.style.border = "1px dashed yellow";
            //     	// span.style.width = 30 px;
            //     	// span.style.height = 30 px;
            //     } else { // black
            //         span.style.backgroundColor = "green";
            //         // span.style.border = "1px dashed yellow";
            //     }
            // } else {  // even
            //     if(j & 1){ // black
            //         span.style.backgroundColor = "green";  
            //         // span.style.border = "1px dashed yellow"; 
            //     }
            //     else {
            //     	span.style.backgroundColor = "black";
            //     	// span.style.border = "1px dashed yellow";
            //     }
            }
            
            row.appendChild(span);
        }
    }
}

function colorRandom(x, y) {
    colorNormal(8, 8, Math.random() >.5 ?'black':'#CFD65C' );
}

function getRandomHexColor() {
    return '#' + Math.floor(Math.random() * 16777215).toString(16);
}

colorNormal(8, 16, 'green');





































