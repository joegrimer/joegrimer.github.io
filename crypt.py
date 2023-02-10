import re

message = '''A Wolf had been feasting too greedily, and a bone had stuck crosswise in his throat. He could get it neither up nor down, and of course he could not eat a thing. Naturally that was an awful state of affairs for a greedy Wolf.

So away he hurried to the Crane. He was sure that she, with her long neck and bill, would easily be able to reach the bone and pull it out.

"I will reward you very handsomely," said the Wolf, "if you pull that bone out for me."

The Crane, as you can imagine, was very uneasy about putting her head in a Wolf's throat. But she was grasping in nature, so she did what the Wolf asked her to do.

When the Wolf felt that the bone was gone, he started to walk away.

"But what about my reward!" called the Crane anxiously.

"What!" snarled the Wolf, whirling around. "Haven't you got it? Isn't it enough that I let you take your head out of my mouth without snapping it off?"'''

simplified_message = re.sub("[,.\]\[:()'\" 0-9!?\n]", "", message.lower())

print(f"simpified:\n{simplified_message}")

alphabet='abcdefghijklmnopqrstuvwxyz'
la = len(alphabet)
for i in ['a','ab','abdsfdsf']:
   k = 0
   nm = ''
   for j in simplified_message:
      # print(f"j is {j}")
      nm += alphabet[(alphabet.index(j)+alphabet.index(i[k]))%la]
      k+=1
      if k >= len(i):
         k=0
   print(f"\nnewmessage:\n{nm}\n")
