from machine import Machine
import modes

myMachine = Machine(modes.NORMAL)

message = "Learning to code opens up a world of possibilities. Whether you're interested in web development, data science, or creating your own applications, programming skills can help you achieve your goals. The journey may be challenging at times, but the rewards are worth the effort. With each line of code, you gain the ability to turn ideas into reality and solve problems in creative ways."
s = myMachine.encode(message)
print(s)
decoded = myMachine.decode(s)
print(decoded)
print(decoded == message)