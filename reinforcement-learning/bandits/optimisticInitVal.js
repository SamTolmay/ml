/* eslint-disable operator-assignment */
/* eslint-disable max-classes-per-file */
const random = require('random');

class OptimisticInitialValueAgent {
  constructor(bandits, initialValue) {
    this.bandits = bandits;
    this.r01 = random.uniform();
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
    return this.bestBandit();
  }
}

module.exports = OptimisticInitialValueAgent;

// const bandit1 = new Bandit(6, 2, '1');
// const bandit2 = new Bandit(5, 2.5, '2');
// const bandit3 = new Bandit(3, 2, '3');
// const bandit4 = new Bandit(3, 1, '4');

// const agent = new OptimisticInitialValueAgent([bandit1, bandit2, bandit3, bandit4], 10);
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

// // console.log(results);
// agent.banditsMap.forEach((value, bandit) => {
//   console.log(value, bandit);
// });
