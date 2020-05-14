# while using recursion, the following code gives error,

gen_sub(0,[])

def gen_sub(start_idx, s):
  if start_idx == N-1:
    self.ans.append(s)
    return
  gen_sub(start_idx + 1, s.append(arr[start_idx]))
  
  # The following code snippet gives error , can't append to NoneType
  # However, the following code snippet works - 
  
 def gen_sub(start_idx, s):
  if start_idx == N-1:
    self.ans.append(s)
    return
  gen_sub(start_idx + 1, s + [arr[start_idx])
