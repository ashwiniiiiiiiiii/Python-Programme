from collections import deque

class EventProcessingSystem:
    def __init__(self):
        self.event_queue = deque()

    # Add an Event
    def add_event(self, event):
        self.event_queue.append(event)
        print(f"Event added: {event}")

    # Process the Next Event 
    def process_next_event(self):
        if not self.event_queue:
            print("No events to process.")
        else:
            event = self.event_queue.popleft()
            print(f"Processing event: {event}")

    # Display Pending Events
    def display_pending_events(self):
        if not self.event_queue:
            print("No pending events.")
        else:
            print("Pending events:", list(self.event_queue))

    # Cancel an Event
    def cancel_event(self, event):
        if event in self.event_queue:
            self.event_queue.remove(event)
            print(f"Event canceled: {event}")
        else:
            print("Event not found or already processed.")


# Demo Menu
def main():
    system = EventProcessingSystem()

    while True:
        print("\n--- Event Processing System ---")
        print("1. Add Event")
        print("2. Process Next Event")
        print("3. Display Pending Events")
        print("4. Cancel Event")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            event = input("Enter event name: ")
            system.add_event(event)
        elif choice == "2":
            system.process_next_event()
        elif choice == "3":
            system.display_pending_events()
        elif choice == "4":
            event = input("Enter event name to cancel: ")
            system.cancel_event(event)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()