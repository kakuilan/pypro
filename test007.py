#!/usr/bin/env python3
#实例for...break
edibles = ["ham","spam","eggs","nuts"]
for food in edibles:
  if food == "spam":
    print("No more spam please!")
    break
  print("Great, delicious " + food)
else:
  print("I am so glad:No spam!")
print("Finaly, I finished stuffing myself")
