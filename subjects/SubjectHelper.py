def check_if_dead(human):
  if human.health <= 0:
    return True
  else:
    return False



# for human in humans:
#   if check_if_dead(human):
#     # Remove the human from the simulation
#     humans.remove(human)
# PUT THIS IN SIMULATION LOOP