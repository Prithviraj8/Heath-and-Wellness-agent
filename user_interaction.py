# user_interaction.py


def collect_user_data():
    user_data = {}

    # Collect basic information
    user_data["name"] = input("Enter your name: ")
    user_data["age"] = int(input("Enter your age: "))
    user_data["weight"] = float(input("Enter your weight (in kg): "))
    user_data["height"] = float(input("Enter your height (in cm): "))

    # Collect fitness goals
    user_data["fitness_goals"] = input(
        "Enter your fitness goals (e.g., weight loss, muscle gain): "
    )

    # Collect dietary preferences
    user_data["dietary_preferences"] = input(
        "Enter your dietary preferences (e.g., vegetarian, vegan, no restrictions): "
    )

    # Collect mental health goals
    user_data["mental_health_goals"] = input(
        "Enter your mental health goals (e.g., reduce stress, improve focus): "
    )

    return user_data


if __name__ == "__main__":
    user_data = collect_user_data()
    print("User Data Collected:", user_data)
