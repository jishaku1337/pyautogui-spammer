import pyautogui, asyncio

class csf:
  def __init__(self, message: str):
    self.message = message

  async def start(self: "csf"):
    pyautogui.write(self.message)
    pyautogui.press("enter")

async def main():
  message: str = input("message: ")
  s = csf(message)
  await asyncio.gather(*[s.start() for _ in range(100)])

if __name__ == "__main__":
  asyncio.run(main())
