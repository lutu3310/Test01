import gpiozero
from time import sleep
while(True):
    mcp3008 = gpiozero.MCP3008(channel=7)
    print(mcp3008.value)
    sleep(1)