import uncurl
import requests
import random

## Curl command from browser
curl_command = input("Enter curl command from browser:\n")

## Start parsing of curl string
try:
    curl_context = uncurl.parse_context(curl_command)
except:
    print("curl command failed, try again")
    exit(1)
    
## settings
tasks = input("Enter task range (taskId from URL), ex. (119089-119094): ").replace(" ", "").split("-")
answer_range = input("Enter answer range, ex. (1-30): ").replace(" ", "").split("-")
latency_range = input("Enter time range in seconds, ex. (10-60): ").replace(" ", "").split("-")
wrong_chance = int(input("Enter chance of getting question wrong, 1 in ... (leave empty for everything correct): "))

for task in range(int(tasks[0]), int(tasks[1]) + 1):
    print("Task: ", task)
    
    answer = random.randint(int(answer_range[0]), int(answer_range[1]))
    latency = random.randint(int(latency_range[0]), int(latency_range[1]))
    
    if wrong_chance is not None:
        if random.randint(1, wrong_chance) == 1:
            result = 0
        else:
            result = 100
    else:
        result = 100

    payload = f"answer=%5B%22{answer}%22%5D&assignmentNodeId={task}&result={result}&latency={latency}"

    response = requests.post(url=curl_context.url, data=payload, headers=curl_context.headers, cookies=curl_context.cookies)
    
    if response.status_code == 200:
        print(f"Success, answer: {answer}, time: {latency}")
    else:
        print("Failed task ", task)
