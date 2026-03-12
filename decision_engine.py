import json
import datetime

FILE_NAME = "decisions.json"

def load_decisions():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_decisions(decisions):
    with open(FILE_NAME, "w") as file:
        json.dump(decisions, file, indent=4)

def add_decision():
    decision = input("Enter your decision: ")
    reason = input("Reason for decision: ")
    expected = input("Expected outcome: ")

    new_decision = {
        "decision": decision,
        "reason": reason,
        "expected_outcome": expected,
        "actual_outcome": "",
        "date": str(datetime.date.today())
    }

    decisions = load_decisions()
    decisions.append(new_decision)
    save_decisions(decisions)

    print("Decision saved successfully!")

def view_decisions():
    decisions = load_decisions()

    if not decisions:
        print("No decisions recorded.")
        return

    for i, d in enumerate(decisions, start=1):
        print("\nDecision", i)
        print("Decision:", d["decision"])
        print("Reason:", d["reason"])
        print("Expected Outcome:", d["expected_outcome"])
        print("Actual Outcome:", d["actual_outcome"])
        print("Date:", d["date"])

def update_outcome():
    decisions = load_decisions()

    if not decisions:
        print("No decisions available.")
        return

    view_decisions()
    index = int(input("Select decision number to update outcome: ")) - 1

    if 0 <= index < len(decisions):
        outcome = input("Enter actual outcome: ")
        decisions[index]["actual_outcome"] = outcome
        save_decisions(decisions)
        print("Outcome updated!")
    else:
        print("Invalid choice")

def menu():
    while True:
        print("\nPersonal Decision Memory Engine")
        print("1. Add Decision")
        print("2. View Decisions")
        print("3. Update Outcome")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_decision()
        elif choice == "2":
            view_decisions()
        elif choice == "3":
            update_outcome()
        elif choice == "4":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    menu()
