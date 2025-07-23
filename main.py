from pkbots import MasterController

def main():
    # Create the controller
    controller = MasterController()
    
    # Run update forever
    while True:
        controller.update()

if __name__ == "__main__":
    main()