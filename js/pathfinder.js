


var WIDTH = 20;
var HEIGHT = 20;
var MARGIN = 1;


class block{
    constructor(row, column, width, height, margin){
        this.color = "WHITE";
        this.obs = false;
        this.x = column*(width + margin) + (width/2 | 0) + margin;
        this.y = row*(height + margin) + (height/2 | 0) + margin;
        this.width = width;
        this.height = height;
        this.neighbor = new Array();
        this.number = null;
    }

    function draw(color, win){

    }
}

class button{
    constructor(color, x, y, width, height, text=''){
        this.color = color;
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.text = text;
    }

    draw(screen){

    }

    isOver(pos){
        if (self.x <= pos[0] <= self.x + self.width){
            if (self.y <= pos[1] <= self.y + self.height){
                return True;
            }
        }

        return False;
    }
}


function heuristic(num1, num2, grid){
    h = len(grid[0]);
    row1 = num1;
    col1 = num1 % h;
    row2 = num2;
    col2 = num2 % h;
    
    distance = abs(row1-row2)*(HEIGHT + MARGIN) + abs(col1-col2)*(WIDTH + MARGIN);

    return distance;
}
    

function neighbor(number, grid){
    var h = grid[0].length;
    var row = number;
    var col = number % h;
    var lis = [];
    if (row > 0 && grid[row-1][col].obs == False){
        lis.push(grid[row-1][col].number);
    }
    if (row < (len(grid)-1) && grid[row+1][col].obs == False){
        lis.push(grid[row+1][col].number);
    }
    if (col > 0 && grid[row][col-1].obs == False){
        lis.push(grid[row][col-1].number);
    }
    if (col < (h-1) && grid[row][col+1].obs == False){
        lis.push(grid[row][col+1].number);
    }
    return lis;
}


function curr(number, grid){
    var h = grid[0].length;
    var row = number;
    var col = number % h;
    grid[row][col].draw(LIGHTGREEN, win);
    pg.display.update();
}

function neww(number, grid){
    var h = grid[0].length;
    var row = number;
    var col = number % h;
    grid[row][col].draw(GREEN, win);
    pg.display.update();
}


function old(number, grid){
    var h = grid[0].length;
    var row = number;
    var col = number % h;
    grid[row][col].draw(RED, win);
    pg.display.update();
}


function path(number, grid){
    var h = grid[0].length;
    var row = number;
    var col = number % h;
    grid[row][col].draw(YELLOW, win);
    pg.display.update();
}















