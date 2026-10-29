positive_words = ["good", "excellent", "helpful", "clear", "interesting"]
negative_words = ["bad", "poor", "boring", "difficult", "confusing"]

print("STUDENT FEEDBACK ANALYSIS")
print("-" * 55)

n = int(input("Enter the number of feedback sentences: "))

for i in range(n):
    feedback = input("\nEnter feedback: ")
    sentence = feedback.lower()
    for symbol in ".,!?":
        sentence = sentence.replace(symbol, "")
    words = sentence.split()
    positive_count = 0
    negative_count = 0
    for word in words:
        if word in positive_words:
            positive_count += 1
        if word in negative_words:
            negative_count += 1
    score = positive_count - negative_count
    if score > 0:
        sentiment = "Positive"
    elif score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print("\nFeedback:", feedback)
    print("Positive indicators:", positive_count)
    print("Negative indicators:", negative_count)
    print("Sentiment score:", score)
    print("Classification:", sentiment)