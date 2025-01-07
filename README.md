# Campus-Inkrement-Solver

## Dont use for bad :(
This project was made only for showing that this is possible. You are self responsible for what you use it for.

## How 2

### Dependencies
`pip install uncurl requests`

### Get cookies
To get the cookies needed which are pasted into the program as "curl command from browser" you need to:
1. Sign into Campus Inkrement
2. Go into a task
3. Open the network tab in inspect element
4. Submit an answer for the task your on
5. Right click the request that has appeared in the network tab and find "copy as curl"
6. Paste into the program

## Inputs

### Curl command
The network request copied from your browsers dev tools

### Task range
In the url of your task on Campus Inkrement you will se a variable called `taskId`, if its not there reload or select the task again.
The task range are what tasks will be done by the program, the range is split by a `-` and every task between + the start and end will be done

### Answer range
The program doesnt actually solve the tasks with the correct answer, so you specify a range of numbers that the program randomly selects to enter as its answer.

### Latency range
When you submit an answer how long you used on that task is sent with it, this lets you select a range where the program randomly selects a time in seconds for how long it took to solve the task.
This does not affect the speed of the program.

### Wrong chance
This number is the 1 in i, if you enter 100 one of a hundred answers submitted will be wrong.
This only serves the purpose of making it look more legit.
