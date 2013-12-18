class stack(object):
   item_list = []
   def _int_(self):
      self.item_list = []

   def pop(self):
      return self.item_list.pop(len(self.item_list) - 1)

   def push(self, x):
      self.item_list.append(x)

   def top(self):
      a = self.item_list[len(self.item_list) - 1]
      return a

  

