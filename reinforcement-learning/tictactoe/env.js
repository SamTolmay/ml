/* eslint-disable class-methods-use-this */
class TicTacToeEnv {
  constructor() {
    this.state = [...Array(9)].map(() => 0);
    this.symbols = [-1, 1];
    this.winner = null;
  }

  // eslint-disable-next-line consistent-return
  isGameOver() {
    if (this.winner !== null) {
      return true;
    }
    // check rows
    [0, 1, 2].forEach(i => {
      const row = this.state.slice(i * 3, (i + 1) * 3);
      const sum = row.reduce((acc, cur) => acc + cur);
      if (sum === 3) {
        this.winner = 1;
      }
      if (sum === -3) {
        this.winner = -1;
      }
    });
    if (this.winner !== null) {
      return true;
    }
    // check cols
    [0, 1, 2].forEach(i => {
      const col = [this.state[i], this.state[i + 3], this.state[i + 6]];
      const sum = col.reduce((acc, cur) => acc + cur);
      if (sum === 3) {
        this.winner = 1;
      }
      if (sum === -3) {
        this.winner = -1;
      }
    });
    if (this.winner !== null) {
      return true;
    }
    // check diagonal
    let sum;
    const d1 = [this.state[0], this.state[4], this.state[8]];
    sum = d1.reduce((acc, cur) => acc + cur);
    if (sum === 3) {
      this.winner = 1;
    }
    if (sum === -3) {
      this.winner = -1;
    }
    const d2 = [this.state[2], this.state[4], this.state[6]];
    sum = d2.reduce((acc, cur) => acc + cur);
    if (sum === 3) {
      this.winner = 1;
    }
    if (sum === -3) {
      this.winner = -1;
    }
    if (this.winner !== null) {
      return true;
    }
    return false;
  }

  getState() {
    return Array.from(this.state);
  }

  isValidMove(i) {
    if (i < 0 || i > 8) return false;
    return this.state[i] === 0;
  }

  makeMove(i, sym) {
    if (!this.isValidMove(i)) {
      throw new Error('Invalid move');
    }
    if (!this.symbols.includes(sym)) {
      throw new Error('Invalid sym');
    }
    this.state[i] = sym;
  }

  draw() {
    const val = i => {
      if (this.state[i] === 1) return 'X';
      if (this.state[i] === -1) return 'O';
      if (this.state[i] === 0) return ' ';
    };
    console.log(`
    -------
    |${val(0)}|${val(1)}|${val(1)}|
    |${val(3)}|${val(4)}|${val(5)}|
    |${val(6)}|${val(7)}|${val(8)}|
    -------
    `);
  }
}

export default TicTacToeEnv;
