import pyautogui
import pygetwindow as gw
import time

# Replace 'Your Application Title' with the title of your application window
APP_TITLE = 'WhatsApp Web'

def refresh_app():
    try:
        # Get the window by title
        windows = gw.getWindowsWithTitle(APP_TITLE)
        
        if not windows: 
            print("Application not found.")
            return
        

        for window in windows:
            # Restore the window if it's minimized
            if window.isMinimized:
                window.restore()  # Restore the window
                time.sleep(1)      # Wait for a second to ensure it's restored

            # Bring the window to the foreground
            window.activate()
            time.sleep(0.5)  # Wait for a moment to ensure the window is active

            # Simulate pressing F5
            pyautogui.press('f5')
            print(f"{APP_TITLE} refreshed.")

    except IndexError:
        print("Application not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        refresh_app()
        time.sleep(600)  # Refresh every 10 minutes
