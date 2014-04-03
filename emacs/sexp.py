from string import whitespace
import json

atom_end = set('().[]"\'') | set(whitespace)

def parse(sexp):
    stack, i, length = [[]], 0, len(sexp)
    while i < length:
        c = sexp[i]

        #print c, stack
        reading = type(stack[-1])
        if reading == list:
            if   c == '(': stack.append([])
            elif c == '.': pass
            elif c == ')': 
                stack[-2].append(stack.pop())
                if stack[-1][0] == ('quote',): stack[-2].append(stack.pop())
            elif c == '[': stack.append([])
            elif c == ']': 
                stack[-2].append(stack.pop())
            elif c == '"': stack.append('')
            elif c == "'": stack.append([('quote',)])
            elif c in whitespace: pass
            else: stack.append((c,))
        elif reading == str:
            if   c == '"': 
                stack[-2].append(stack.pop())
                if stack[-1][0] == ('quote',): stack[-2].append(stack.pop())
            elif c == '\\': 
                i += 1
                stack[-1] += sexp[i]
            else: stack[-1] += c
        elif reading == tuple:
            if c in atom_end:
                atom = stack.pop()
                try:
                    stack[-1].append(int(atom[0]))
                except ValueError:
                    stack[-1].append(atom[0])
                if stack[-1][0] == ('quote',): stack[-2].append(stack.pop())
                continue
            else: stack[-1] = ((stack[-1][0] + c),)
        i += 1
    return stack.pop()

nodemap = {}

nodes = []
links = []

data = parse(open("archive-contents").read())[0][1:]

def lookup(m,i):
    if i not in m:
        nodes.append({"name": i})
        nodemap[i] = len(nodemap)
    return m[i]

for i in data:
    name = i[0]
    namei = lookup(nodemap,name)
    deps = i[1][1]
    if deps == "nil": continue
    for dep in map(lambda x: x[0],deps):
        links.append({"source": lookup(nodemap,dep), "target": namei})

print json.dumps({"nodes": nodes, "links": links})
