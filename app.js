let board = [
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
];
document.getElementById('button').addEventListener("click", () => {
  let squareID = 0
  for (let y = 0; y < 9; y++) {
    for (let x = 0; x < 9; x++) {
      ++squareID;
      board[y][x] = Number(document.getElementById(squareID).value)
    }
  }
  let xhr = new XMLHttpRequest();
  xhr.open('GET', './solver.py', true);
  xhr.onload = () => {
    if (this.status == 200) {

    }
  }
  xhr.send();
  console.log(board);
})
