class CobotController:
    def move(self, command):
        if command == "STOP":
            print("🛑 Emergency Stop")
        elif command == "SLOW":
            print("⚠️ Slowing down")
        elif command == "MOVE":
            print("✅ Moving safely")
        else:
            print("Unknown command")


if __name__ == "__main__":
    robot = CobotController()
    robot.move("MOVE")
