const random = require('random');

class Bandit {
  constructor(mu, sigma, id) {
    this.id = id;
    this.pull = random.normal(mu, sigma);
    this.n = 0;
    this.x = 0;
  }

  learn(result) {
    this.n += 1;
    this.x = (1 - 1 / this.n) * this.x + (1 / this.n) * result;
  }
}

module.exports = Bandit;
