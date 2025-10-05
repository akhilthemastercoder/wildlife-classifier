images = [
    "A small, white bird on ice.",
    "A large animal lounging on a rock near water.",
    "A tall bird with a long neck in a grassy area."
]

choices = {
    "1":"Penguin",
    "2":"Seal",
    "3":"Giraffe"
}

def classify_image(image):
    print("\n"+image)
    for key, value in choices.items():
        print(f"{key}. {value}")
    while True:
        user_input = input("Enter the number of your choice: ")
        if user_input in choices:
            return choices[user_input]
        print("Invalid choice. Please try again.")

answers = []

for img in images:
    label = classify_image(img)
    answers.append(label)

summary = {}
for answer in answers:
    summary[answer] = summary.get(answer, 0) + 1

print("\nSummary of your classifications:")
for animal, count in summary.items():
    print(f"{animal}: {count}")