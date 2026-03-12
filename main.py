from web_agent import browse_web
from research_agent import summarize

print("AI Web Automation Agent")

while True:

    task = input("Enter a topic (exit to quit): ")

    if task == "exit":
        break

    web_data = browse_web(task)

    result = summarize(web_data)

    print("\nAI Report:\n")
    print(result)
