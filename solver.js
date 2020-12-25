//Test Boards
let validSudokuBoard1 = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
];
let validSudokuBoard2 = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
];
let invalidSudokuBoard1 = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 1, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
];
let invalidSudokuBoard2 = [
  [5, 3, 9, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
];

function checkRulesAtPoint(x, y, testNumber, updatedBoard) {
  //Checks rows and columns for numbers that might not work
  for (let columnOrRow = 0; columnOrRow < 9; columnOrRow++) {
    if (updatedBoard[columnOrRow][x] == testNumber) {
      return false;
    } else if (updatedBoard[y][columnOrRow] == testNumber) {
      return false;
    }
  }
  //Checks to make sure number isn't inside the box
  let boxStartingXValue = (Math.floor(x / 3) * 3);
  let boxStartingYValue = (Math.floor(y / 3) * 3);
  for (let addedYValue = 0; addedYValue < 3; addedYValue++) {
    for (let addedXValue = 0; addedXValue < 3; addedXValue++) {
      if (updatedBoard[boxStartingYValue + addedYValue][boxStartingXValue + addedXValue] == testNumber) {
        return false;
      }
    }
  }
  return true;
}

/*
Checking that the board inputted is actually a valid board
*/
//Looks  for issues with line collisions
function checkForLineIssues(orientation) {
  for (let i = 0; i < orientation.length; i++) {
    if (orientation[i] == orientation[i - 1]) {
      return false;
    }
  }
  return true;
}
//Checking no number is in the same row, column or box as any of the other numbers
function doRulesWork(arrayNum) {
  let returnValue = false;
  // Information about each number sorted
  let boxes = [0, 0, 0, 0, 0, 0, 0, 0, 0];
  let columnLocationList = [];
  let rowLocationList = [];
  // Splits the locations of rows, column and boxes into seperate lists
  for (let location of arrayNum) {
    let columnLocation = location[0];
    let rowLocation = location[1];
    columnLocationList.push(columnLocation);
    rowLocationList.push(rowLocation);
    let i = 0;
    for (let boxYValue = 0; boxYValue < 3; boxYValue++) {
      for (let boxXValue = 0; boxXValue < 3; boxXValue++) {
        if (((columnLocation >= (boxYValue * 3)) && (columnLocation < (boxYValue * 3) + 3)) && ((rowLocation >= boxXValue * 3) && (rowLocation < (boxXValue * 3) + 3))) {
          boxes[i] += 1;
        }
        i += 1;
      }
    }
  }
  //Checking the number follows the rules in terms of boxes
  for (let box of boxes) {
    if (box > 1) {
      return false;
    }
  }
  // Checking the number follows the rules in terms of row/column
  columnLocationList.sort();
  rowLocationList.sort();
  if (checkForLineIssues(columnLocationList) && checkForLineIssues(rowLocationList)) {
    returnValue = true;
  }
  return returnValue;
}

function checkForValidBoard(board) {
  //The location of each number in tuples (column, row) sorted by number in an array
  let numbers = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
  ];
  //Sorting all the numbers into respective array
  for (let row = 0; row < 9; row++) {
    for (let column = 0; column < 9; column++) {
      for (let number = 1; number < 10; number++) {
        if (board[row][column] == number) {
          numbers[number].push([column, row]);
        }
      }
    }
  }
  //Checks each number follows sudoku rules
  for (let number of numbers) {
    if (!doRulesWork(number)) {
      return false;
    }
  }
  return true;
}

/* Actually solving the sudoku board*/
// This will be done via backtracking
let returnedInformation = [[], [], [], [], [], [], [], [], []];
//Backtracking recursion loop starts
function solve(board){
  for(let y = 0; y < 9; y++){
    for(let x = 0; x < 9; x++){
      if (board[y][x] == 0){
        for(let number = 1; number < 10; number++){
          if (checkRulesAtPoint(x, y, number, board)){
            board[y][x] = number;
            // console.log(board);
            // console.log('\n');
            solve(board);
            board[y][x] = 0;
          }
        }
        return;
      }
    }
  }
  for(let x = 0; x < 9; x++){
    for(let y = 0; y < 9; y++){
      returnedInformation[y][x] = board[y][x];
    }
  }
}

function returnSolvedBoard(board){
  if(!checkForValidBoard(board)){
    return "This board is not possiable to solve";
  }
  solve(board)
  return returnedInformation;
}
