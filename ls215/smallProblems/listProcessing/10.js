// https://launchschool.com/exercises/cd69bc70

'use strict';

const isItemAvailable = (item, itemTransactions) => {
  let quantity = itemTransactions.filter(({ id }) => id === item)
                         .reduce((total, item) => {
                          if (item.movement === 'in') {
                            total += item.quantity;
                          } else {
                            total -= item.quantity;
                          }
                          return total;
                         }, 0);

  return quantity > 0;
};

const transactions = [ { id: 101, movement: 'in',  quantity:  5 },
                       { id: 105, movement: 'in',  quantity: 10 },
                       { id: 102, movement: 'out', quantity: 17 },
                       { id: 101, movement: 'in',  quantity: 12 },
                       { id: 103, movement: 'out', quantity: 15 },
                       { id: 102, movement: 'out', quantity: 15 },
                       { id: 105, movement: 'in',  quantity: 25 },
                       { id: 101, movement: 'out', quantity: 18 },
                       { id: 102, movement: 'in',  quantity: 22 },
                       { id: 103, movement: 'out', quantity: 15 }, ];

isItemAvailable(101, transactions);     // false
isItemAvailable(105, transactions);     // true

// Don't do this overkill

//   return Object.entries(listOfTransactions.reduce((obj, item) => {
//     obj[item.id] = item.id;
//     obj[item.id] = 0 ?? undefined;

//     if (item.movement === 'in') {
//       obj[item.id] += item.quantity;
//     } else {
//       obj[item.id] -= item.quantity;
//     }

//     return obj;
//   }, {})).filter(([id, quantity]) => Number(id) === itemID && quantity > 0).length > 0;
// }
