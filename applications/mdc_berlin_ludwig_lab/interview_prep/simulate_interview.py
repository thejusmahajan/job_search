#!/usr/bin/env python3
import json
import random
import sys
import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_questions(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        sys.exit(1)

def print_header(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60 + "\n")

def simulate(questions_data, category=None):
    if category and category in questions_data:
        q_list = [(category, q) for q in questions_data[category]]
    else:
        q_list = []
        for cat, qs in questions_data.items():
            for q in qs:
                q_list.append((cat, q))
    
    random.shuffle(q_list)
    score = 0
    total = len(q_list)

    for i, (cat, item) in enumerate(q_list, 1):
        clear_screen()
        print_header(f"Question {i} of {total}  |  Category: {cat}")
        print(f"\033[1;36mQ: {item['Question']}\033[0m\n")
        
        print("=> State your answer OUT LOUD.")
        input("=> Press [ENTER] when you are finished to see the Key Points...")
        
        print("\n\033[1;33m--- Key Points you should have hit ---\033[0m")
        for point in item["Key Points"]:
            print(f"  {point}")
        
        print("\nHow did you do?")
        while True:
            resp = input("Did you hit the key points? (y/n): ").strip().lower()
            if resp in ['y', 'yes', 'n', 'no']:
                if resp in ['y', 'yes']:
                    score += 1
                break
    
    clear_screen()
    print_header("Interview Practice Complete")
    print(f"Final Self-Assessment Score: {score} / {total}")
    print(f"Percentage: {(score/total)*100:.1f}%\n")
    
    if score == total:
        print("Excellent! You are ready.")
    elif score >= total * 0.7:
        print("Good job. Review the missed points in the study guides.")
    else:
        print("Keep practicing! Read the study guides and run the simulator again.")
    print()

def main():
    q_file = os.path.join(os.path.dirname(__file__), "questions.json")
    data = load_questions(q_file)
    
    categories = list(data.keys())
    
    clear_screen()
    print_header("Ludwig Lab Interview Simulator")
    print("Choose a topic to practice:")
    print("  0. All Topics (Randomized)")
    for i, c in enumerate(categories, 1):
        print(f"  {i}. {c}")
    
    choice = input("\nEnter choice (0-{len}): ".format(len=len(categories))).strip()
    
    try:
        idx = int(choice)
        if idx == 0:
            simulate(data)
        elif 1 <= idx <= len(categories):
            simulate(data, category=categories[idx-1])
        else:
            print("Invalid choice. Exiting.")
    except ValueError:
        print("Invalid input. Exiting.")

if __name__ == "__main__":
    main()
