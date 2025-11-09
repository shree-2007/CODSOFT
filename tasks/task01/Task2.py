# CodSoft Internship Task 1: Rock-Paper-Scissors Game
# Name: Harinishree
# Domain: Python Programming
# Batch: [October to November batch B57]
# Description: A fun game where the user plays Rock-Paper-Scissors against the computer.

import random
import time

def display_intro():
    print("\n========================================")
    print(" 🎮 Welcome to Rock–Paper–Scissors Game ")
    print("========================================")
    print("Instructions:")
    print("👉 Type 'rock', 'paper', or 'scissors' to play.")
    print("👉 Type 'exit' to quit the game anytime.")
    print("----------------------------------------\n")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    display_intro()

    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

        if user_choice == "exit":
            print("\n👋 Thanks for playing, Harini!")
            print(f"🏁 Final Scores — You: {user_score} | Computer: {computer_score}")
            print("========================================\n")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("⚠️ Invalid choice! Please try again.\n")
            continue

        print("\nComputer is choosing", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)
        print("\n")

        computer_choice = get_computer_choice()
        print(f"🧑 You chose: {user_choice}")
        print(f"💻 Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("🤝 It's a Tie!\n")
        elif winner == "user":
            print("🎉 You Win this round!\n")
            user_score += 1
        else:
            print("😢 Computer Wins this round!\n")
            computer_score += 1

        print(f"📊 Current Score — You: {user_score} | Computer: {computer_score}")
        print("----------------------------------------")

        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\n🏁 Final Scores:")
            print(f"✨ You: {user_score} | 💻 Computer: {computer_score}")
            print("Thanks for playing! See you soon 👋\n")
            break

# Run the game
if __name__ == "__main__":
    main()
