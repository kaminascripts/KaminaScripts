```flow
st=>start: Start
e=>end: End
op1=>operation: Iterate over ASG with DesiredCapacity > 0
sub1=>subroutine: My Subroutine
cond=>condition: Is spot?:>http://www.google.com
io=>inputoutput: catch something...
para=>condition: Capacity > 0?
cond2=>condition: Capacity > 0?

st->op1->cond
cond(yes)->io->e
cond(no)->para
para(path1, bottom)->sub1(right)->op1
para(path2, top)->op1
para(yes)->io->e
para(no)->para
```
