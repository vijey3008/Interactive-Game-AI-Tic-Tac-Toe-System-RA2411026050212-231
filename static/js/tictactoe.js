let board = Array(9).fill('');
let gameOver = false;
const boardEl = document.getElementById('board');
const statusEl = document.getElementById('status');
const nodesEl = document.getElementById('nodes');
const timeEl = document.getElementById('time');

function renderBoard() {
  boardEl.innerHTML = '';
  board.forEach((value, index) => {
    const cell = document.createElement('button');
    cell.className = 'cell';
    cell.textContent = value;
    cell.onclick = () => playerMove(index);
    boardEl.appendChild(cell);
  });
}

function winnerOf(b) {
  const lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
  for (const [a, c, d] of lines) {
    if (b[a] && b[a] === b[c] && b[a] === b[d]) return b[a];
  }
  if (!b.includes('')) return 'Draw';
  return null;
}

async function playerMove(index) {
  if (gameOver || board[index] !== '') return;
  board[index] = 'X';
  renderBoard();
  let winner = winnerOf(board);
  if (winner) return endGame(winner);

  statusEl.textContent = 'AI is thinking...';
  const response = await fetch('/api/tictactoe/move', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ board, method: document.getElementById('method').value })
  });
  const data = await response.json();
  board = data.board;
  nodesEl.textContent = data.nodes;
  timeEl.textContent = data.time_ms;
  renderBoard();
  if (data.winner) return endGame(data.winner);
  statusEl.textContent = 'Your turn';
}

function endGame(winner) {
  gameOver = true;
  if (winner === 'Draw') statusEl.textContent = 'Match Draw!';
  else statusEl.textContent = `${winner} wins!`;
}

function resetGame() {
  board = Array(9).fill('');
  gameOver = false;
  nodesEl.textContent = '0';
  timeEl.textContent = '0';
  statusEl.textContent = 'Your turn';
  renderBoard();
}

renderBoard();
