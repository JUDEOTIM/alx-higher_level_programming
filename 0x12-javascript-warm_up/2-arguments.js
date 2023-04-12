#!/usr/bin/node

// read args from the cli with process.argv
const args = process.argv.slice(2);

// store the arg length
const argLen = args.length;

// if no arg passed
if (argLen === 0) {
  console.log('No argument');
  // if arg is 1
} else if (argLen === 1) {
  console.log('Argument found');
  // else
} else {
  console.log('Arguments found');
}
