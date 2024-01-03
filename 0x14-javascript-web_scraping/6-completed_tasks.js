#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const tasks = JSON.parse(body);

      // Filter tasks by completion status (completed === true)
      const completedTasks = tasks.filter((task) => task.completed);

      // Compute the number of completed tasks for each user
      const completedTasksByUser = completedTasks.reduce((accumulator, task) => {
        const userId = task.userId;
        accumulator[userId] = (accumulator[userId] || 0) + 1;
        return accumulator;
      }, {});

      // Print users with completed tasks in the desired format
      console.log(JSON.stringify(completedTasksByUser, null, 2));
    } catch (parseError) {
      console.error(`Error parsing JSON: ${parseError}`);
    }
  }
});

