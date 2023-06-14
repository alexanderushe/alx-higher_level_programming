#!/usr/bin/node
//prints specified string if it can be converted to a number
const args = process.argv;
const number = parseInt(args[2], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
