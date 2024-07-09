# main.py
from langchain.agents import AgentExecutor
from langgraph.graph import Graph

from agents.fitness_agent import FitnessAgent
from agents.nutrition_agent import NutritionAgent
from agents.mental_health_agent import MentalHealthAgent
from agents.progress_tracking_agent import ProgressTrackingAgent
from agents.reminder_agent import ReminderAgent
from user_interaction import collect_user_data

from pprint import pprint
def main():
    # Collect user data
    user_data = collect_user_data()

    # Initialize agents
    fitness_agent = FitnessAgent(user_data)
    nutrition_agent = NutritionAgent(user_data)
    mental_health_agent = MentalHealthAgent(user_data)
    progress_agent = ProgressTrackingAgent(user_data)
    reminder_agent = ReminderAgent(user_data)


    # Setup langgraph
    graph = Graph()
    workout_plan = fitness_agent.start()
    meal_plan = nutrition_agent.start()
    graph.add_node("fitness", workout_plan)
    graph.add_node("nutrition", meal_plan)
    graph.add_node("mental_health", mental_health_agent.start)

    # Generate workout plan
    # workout_plan = fitness_agent.create_workout_plan()
    # print("Generated Workout Plan:", workout_plan)

    # Generate meal plan
    # meal_plan = nutrition_agent.create_meal_plan()
    # print("Generated Meal Plan:", meal_plan)

    # Provide mental wellness tips
    # wellness_tips = mental_health_agent.provide_wellness_tips()
    # print("Mental Wellness Tips:", wellness_tips)

    # Track progress and generate report
    fitness_feedback = input("Provide feedback on your fitness plan: ")
    nutrition_feedback = input("Provide feedback on your meal plan: ")
    mental_health_feedback = input("Provide feedback on your mental health tips: ")
    progress = progress_agent.track_progress(
        fitness_feedback, nutrition_feedback, mental_health_feedback
    )
    graph.add_node("progress", progress_agent.start)

    # report = progress_agent.generate_report()
    # print(report)

    # Add reminders and send them
    # reminder_agent.add_reminder("Time for your workout!", 5)
    # reminder_agent.add_reminder("Time for your meal!", 10)
    # reminder_agent.send_reminders()
    # graph.add_node("reminder", reminder_agent.send_reminders())

    # Define edges (dependencies between tasks)
    graph.add_edge("fitness", "nutrition")
    graph.add_edge("nutrition", "progress")
    graph.add_edge("mental_health", "progress")
    # graph.add_edge("progress", "reminder")
    # set up start and end nodes
    # graph.set_entry_point("fitness")
    # graph.set_finish_point("progress")
    # compile the graph
    chain = graph.compile()

    # Execute the workflow
    executor = AgentExecutor(graph=chain)
    executor.run()

if __name__ == "__main__":
    main()
