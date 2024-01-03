#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const tasks = JSON.parse(body);

      const completedTasks = tasks.filter((task) => task.completed);

      const completedTasksByUser = completedTasks.reduce((accumulator, task) => {
        const userId = task.userId;
        accumulator[userId] = (accumulator[userId] || 0) + 1;
        return accumulator;
      }, {});

      for (const userId in completedTasksByUser) {
        console.log(`${userId}: ${completedTasksByUser[userId]}`);
      }
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});
