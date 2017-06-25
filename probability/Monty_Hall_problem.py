import random

class Problem(object):
  def __init__(self):
    self.doors = [0, 1, 2]
    self.ground_truth = random.choice(self.doors)  # random choice one door to put car or treasure
    self.selection = random.choice(self.doors)
    self.remain_doors = [0, 1, 2]
    self.remain_doors.remove(self.selection)

  def process(self, change_choice=False):
    # open a door that is not the ground truth
    open_door = random.choice(self.remain_doors)

    # switch another door if it is self.ground_truth
    if open_door == self.ground_truth:
      self.remain_doors = [open_door]
    else:
      self.remain_doors.remove(open_door)

    assert len(self.remain_doors) == 1

    # self.remain_doors only contain 1 door
    if change_choice:
      self.selection = self.remain_doors[0]

    # print self.selection, self.ground_truth
    return self.selection == self.ground_truth

def simulate(change=False, time=10000):
  print("simulate Monty_Hall_problem with change=%s" % str(change))
  correct = 0.0
  for i in range(time):
    if i % 1000 == 0:
      print("process %s/%s" % (str(i), str(time)))

    p = Problem()
    res = p.process(change)
    if res == True:
      correct += 1

  prob = correct / time
  return prob

if __name__ == '__main__':
  prob = simulate()
  print("probability of no change is %f" % prob)
  
  prob = simulate(change=True)
  print("probability of change is %f" % prob)
