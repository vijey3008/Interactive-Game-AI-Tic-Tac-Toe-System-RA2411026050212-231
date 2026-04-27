const sudokuEl = document.getElementById('sudoku');
const messageEl = document.getElementById('message');

function drawSudoku(grid) {
  sudokuEl.innerHTML = '';
  for (let r = 0; r < 9; r++) {
    for (let c = 0; c < 9; c++) {
      const input = document.createElement('input');
      input.maxLength = 1;
      input.inputMode = 'numeric';
      input.dataset.row = r;
      input.dataset.col = c;
      if (grid[r][c] !== 0) {
        input.value = grid[r][c];
        input.readOnly = true;
        input.className = 'prefilled';
      }
      input.oninput = () => {
        input.value = input.value.replace(/[^1-9]/g, '');
      };
      sudokuEl.appendChild(input);
    }
  }
}

function readGrid() {
  const grid = Array.from({ length: 9 }, () => Array(9).fill(0));
  document.querySelectorAll('#sudoku input').forEach(input => {
    const r = Number(input.dataset.row);
    const c = Number(input.dataset.col);
    grid[r][c] = input.value ? Number(input.value) : 0;
  });
  return grid;
}

async function solveSudoku() {
  const response = await fetch('/api/sudoku/solve', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grid: readGrid() })
  });
  const data = await response.json();
  if (data.success) {
    drawSudoku(data.solution);
    messageEl.textContent = 'Solved using CSP Backtracking!';
  } else {
    messageEl.textContent = 'No valid solution found.';
  }
}

async function checkSudoku() {
  const response = await fetch('/api/sudoku/check', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grid: readGrid() })
  });
  const data = await response.json();
  messageEl.textContent = data.valid ? 'You won!' : 'Try again.';
}

function resetSudoku() {
  drawSudoku(initialPuzzle);
  messageEl.textContent = '';
}

drawSudoku(initialPuzzle);
