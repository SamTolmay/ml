/* eslint-disable no-param-reassign */
/* eslint-disable max-classes-per-file */
/* eslint-disable operator-assignment */
const random = require('random');

class EpsilonGreedyAgent {
  constructor(bandits, epsilon) {
    this.bandits = bandits;
    this.epsilon = epsilon;
    this.r01 = random.uniform();
    this.rBi = random.uniformInt(0, bandits.length - 1);
  }

  randomBandit() {
    // console.log('random');
    const index = this.rBi();
    // console.log('index', index);
    return this.bandits[index];
  }

  bestBandit() {
    // console.log('bestBandit');
    const bestBandits = [];
    let maxX = 0;
    this.bandits.forEach(bandit => {
      if (bandit.x > maxX) {
        maxX = bandit.x;
      }
    });
    this.bandits.forEach(bandit => {
      // console.log(value, bandit);
      if (bandit.x === maxX) {
        bestBandits.push(bandit);
      }
    });
    // console.log(bestBandits);
    if (bestBandits.length === 1) {
      // console.log('length 1');
      return bestBandits[0];
    }
    // console.log('length > 1');
    const i = random.uniformInt(0, bestBandits.length - 1)();
    // console.log(i);
    return bestBandits[i];
  }

  choose() {
    const r = this.r01();
    // console.log(r);
    if (r < this.epsilon) {
      return this.randomBandit();
    }
    return this.bestBandit();
  }
}

module.exports = EpsilonGreedyAgent;
// const bandit1 = new Bandit(6, 2, '1');
// const bandit2 = new Bandit(5, 2.5, '2');
// const bandit3 = new Bandit(3, 2, '3');
// const bandit4 = new Bandit(3, 1, '4');

// const agent = new EpsilonGreedyAgent([bandit1, bandit2, bandit3, bandit4], 0.1);
// const numTurns = 500;

// let choice;
// let result;
// const results = [];
// // eslint-disable-next-line no-plusplus
// for (let i = 0; i < numTurns; i++) {
//   choice = agent.choose();
//   result = choice.pull();
//   agent.learn(choice, result);
//   results.push({ result, bandit: choice.id });
// }

// console.log(results);
// agent.banditsMap.forEach((value, bandit) => {
//   console.log(value, bandit);
// });
